import base64
from flask import Flask, request, jsonify
from io import BytesIO
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        # Récupérer le contenu brut de la requête
        raw_data = request.get_data(as_text=True)
        print(f"Texte brut reçu (premiers 100 caractères) : {raw_data[:100]}...")

        # Décoder la chaîne Base64 pour reconstruire l'image
        img_data = base64.b64decode(raw_data)
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Erreur lors du décodage de l'image avec OpenCV.")

        # Répondre avec une confirmation
        return jsonify({'message': 'Image reçue avec succès'}), 200
    except Exception as e:
        return jsonify({'error': 'Erreur lors du traitement de l\'image', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
