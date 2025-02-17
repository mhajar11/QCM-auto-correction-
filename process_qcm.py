import cv2
import numpy as np

def process_qcm(image_path, answer_key):
    """
    :param image_path: Chemin de l'image d'entrée (QCM scanné).
    :param answer_key: Liste (ou tuple) des réponses correctes, 
                       ex. ["A", "B", "C", "D", ...] pour 20 questions.
    :return: (score, correct_questions)
    """
    # Charger l'image en niveaux de gris
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Impossible de charger l'image : {image_path}")

    # Afficher l'image originale
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyWindow("Original Image")

    # On crée une version en BGR (couleur) pour dessiner ensuite dessus
    annotated_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # --- 1) Binarisation / Inversion ---
    _, binary_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)
    # Afficher l'image binaire
    cv2.namedWindow("Binary Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Binary Image", binary_image)
    cv2.waitKey(0)
    cv2.destroyWindow("Binary Image")

    # Inversion
    inverted = cv2.bitwise_not(binary_image)
    # Afficher l'image inversée
    cv2.namedWindow("Inverted Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Inverted Image", inverted)
    cv2.waitKey(0)
    cv2.destroyWindow("Inverted Image")

    # --- 2) Extraction des composantes connexes ---
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        inverted,
        connectivity=8
    )

    # --- 3) Afficher la taille de l'image ---
    height, width = image.shape
    print(f"Taille de l'image : {height} x {width}")

    # --- 4) Définition des bornes de surface ---
    min_area = height * width / 3868.706
    max_area = height * width / 2813.60436364

    # --- 5) Conserver uniquement les composantes 
    #        dont l'aire est dans [min_area, max_area] ---
    filtered = np.zeros_like(inverted, dtype=np.uint8)
    for label_id in range(1, num_labels):
        area = stats[label_id, cv2.CC_STAT_AREA]
        if min_area <= area <= max_area:
            filtered[labels == label_id] = 255

    # Afficher l'image filtrée
    cv2.namedWindow("Filtered Components", cv2.WINDOW_NORMAL)
    cv2.imshow("Filtered Components", filtered)
    cv2.waitKey(0)
    cv2.destroyWindow("Filtered Components")

    # --- 6) Récupérer la bounding box englobant toutes ces composantes ---
    x, y, w, h = cv2.boundingRect(filtered)
    region_of_interest = filtered[y:y+h, x:x+w]


    # --- 7) Diviser en 20 questions (lignes) × 4 colonnes ---
    nb_questions = 20
    nb_choices = 4  # A, B, C, D
    choice_letters = ["A", "B", "C", "D"]  # mapping des colonnes vers A/B/C/D

    sub_w = w // nb_choices     # largeur d'une case
    sub_h = h // nb_questions   # hauteur d'une case

    # On va stocker ici les réponses détectées, sous forme de lettre.
    detected_answers = ["" for _ in range(nb_questions)]

    # Seuil (pour décider si c'est coché ou non).
    threshold_cocher = min_area

    # --- 8) Parcours des 80 cases (20x4) ---
    for row in range(nb_questions):
        for col in range(nb_choices):
            # Coordonnées de la sous-région
            x0 = x + col * sub_w
            y0 = y + row * sub_h
            x1 = x0 + sub_w
            y1 = y0 + sub_h

            # Extraire la sous-image de la case
            sub_region = filtered[y0:y1, x0:x1]


            # Compter les pixels blancs (valeur > 0)
            num_white = cv2.countNonZero(sub_region)

            # Appliquer la règle :
            # "si num_white > threshold_cocher => NON cochée
            #  sinon => COCHÉE"
            if num_white <= threshold_cocher:
                # On considère que cette case est cochée
                detected_answers[row] = choice_letters[col]
                # Si on n'accepte qu'une seule case cochée par question,
                # on brise la boucle sur les colonnes.
                break

            # ---- DESSIN DES RECTANGLES SUR L'IMAGE ANNOTÉE ----
            # On dessine un rectangle rouge autour de la sous-zone
            cv2.rectangle(
                annotated_image,
                (x0, y0),  # coin supérieur-gauche
                (x1, y1),  # coin inférieur-droit
                (0, 0, 255),  # couleur BGR (rouge)
                1  # épaisseur du trait
            )

    # --- 9) Calcul du score ---
    score = 0
    correct_questions = []

    for i in range(nb_questions):
        if detected_answers[i] == answer_key[i]:
            score += 1
            correct_questions.append(i + 1)

    # Affiche les réponses détectées et le score
    print("Réponses détectées :", detected_answers)
    print("Score =", score, "/", nb_questions)
    print("Questions correctes :", correct_questions)

    # --- 10) Enregistrer l'image annotée ---
    output_path = "annotated_qcm.png"
    cv2.imwrite(output_path, annotated_image)
    print(f"Image annotée enregistrée sous : {output_path}")

    # Afficher l'image annotée
    cv2.namedWindow("Annotated Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Annotated Image", annotated_image)
    cv2.waitKey(0)
    cv2.destroyWindow("Annotated Image")

    return score, correct_questions, detected_answers
