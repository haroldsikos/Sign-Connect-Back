# app/routes.py
from flask import Blueprint, request, jsonify
import cv2
import numpy as np
import mediapipe as mp
import base64

bp = Blueprint('routes', __name__)

mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic()

def process_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = holistic.process(image)
    return results

@bp.route('/translate-sign', methods=['POST'])
def translate_sign():
    data = request.get_json()
    image_data = data.get('image')
    image = np.frombuffer(base64.b64decode(image_data), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    results = process_image(image)
    # Aquí puedes procesar `results` para extraer las características de las señas y traducirlas a texto
    translated_text = "Translated text from sign language"

    return jsonify({'translated_text': translated_text})

@bp.route('/translate-voice', methods=['POST'])
def translate_voice():
    data = request.get_json()
    voice = data.get('voice')

    # Lógica para traducir la voz a lenguaje de señas
    translated_sign = "Translated sign language from voice"

    return jsonify({'translated_sign': translated_sign})
