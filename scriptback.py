import base64
from flask import Flask, request, jsonify
from io import BytesIO
from PIL import Image
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        # Récupérer le contenu brut de la requête
        raw_data = request.get_data(as_text=True)  # Récupère les données brutes en tant que texte
        print(f"Texte brut reçu (premiers 100 caractères) : {raw_data[:100]}...")  # Débogage

        # Décoder la chaîne Base64 pour reconstruire l'image
        img_data = base64.b64decode(raw_data)
        print("Image décodée avec succès en données binaires.")

        # Convertir les données binaires en une image OpenCV
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Erreur lors du décodage de l'image avec OpenCV.")

        # Redimensionner l'image si sa hauteur est supérieure à 800 pixels
        height, width = img.shape[:2]
        if height > 800:
            scale_ratio = 800 / height  # Calculer le ratio de réduction
            new_width = int(width * scale_ratio)
            new_height = 800
            img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
            print(f"L'image a été redimensionnée à {new_width}x{new_height} pixels.")

        # Afficher l'image avec OpenCV
        cv2.imshow('Image Reçue', img)
        cv2.waitKey(0)  # Attendre qu'une touche soit pressée
        cv2.destroyAllWindows()

        # Répondre avec une confirmation
        return jsonify({'message': 'Image reçue, redimensionnée et affichée avec succès'}), 200
    except Exception as e:
        print(f"Erreur lors de la réception ou du traitement des données : {e}")
        return jsonify({'error': 'Erreur lors du traitement de l\'image', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
