import cv2
import numpy as np
import streamlit as st
from process_qcm import process_qcm

# Interface Streamlit
st.title("Correction automatique des QCM")
st.header("Définir les réponses correctes")

# Étape 1 : Entrer les réponses correctes
st.subheader("Étape 1 : Définir les réponses correctes")
answer_key = []
for i in range(1, 21):
    answer = st.selectbox(
        f"Réponse correcte pour la question {i}", 
        ["A", "B", "C", "D"], 
        key=f"q{i}"
    )
    answer_key.append(answer)

# Étape 2 : Correction des QCM
st.subheader("Étape 2 : Corriger un QCM")

# Entrée pour le nom et le prénom de l'étudiant
student_name = st.text_input("Entrez le nom de l'étudiant :", key="student_name")
student_firstname = st.text_input("Entrez le prénom de l'étudiant :", key="student_firstname")

# Chargement de l'image du QCM
uploaded_file = st.file_uploader("Choisissez une image de QCM", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Sauvegarder temporairement l'image téléchargée
    image_path = f"temp_{uploaded_file.name}"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(image_path, caption="Image du QCM chargée", use_column_width=True)

    # Ajouter un bouton pour corriger
    if st.button("Corriger"):
        try:
            # Calculer le score et les questions correctes
            score, correct_questions, detected_answers = process_qcm(image_path, answer_key)
            

            # Afficher le message final
            if student_name and student_firstname:
                correct_questions_str = ", ".join(map(str, correct_questions))
                st.write(f"Réponses détectées : {detected_answers}")
                st.success(
                    f"L'étudiant {student_firstname} {student_name} a obtenu un score de {score}/20.\n"
                    f"Questions correctes : {correct_questions_str}"
                )
            else:
                st.warning("Veuillez entrer le nom et le prénom de l'étudiant avant de corriger.")
        except Exception as e:
            st.error(f"Une erreur est survenue lors du traitement : {str(e)}")
else:
    st.info("Veuillez télécharger une image pour commencer la correction.")
