#!/usr/bin/env python3
"""
AI Image Classifier Demo Backend
Based on the transfer-image-classifier repository

This script provides a Flask API for image classification using transfer learning.
For demonstration purposes, this is a simplified version showing the architecture.
"""

import numpy as np
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import base64
from io import BytesIO
from PIL import Image
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# CIFAR-10 classes
CIFAR_CLASSES = [
    'Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
    'Dog', 'Frog', 'Horse', 'Ship', 'Truck'
]

@app.route('/')
def home():
    """Home page with demo information."""
    return """
    <h1>AI Image Classifier Backend</h1>
    <p>This is the backend API for the AI Image Classifier demo.</p>
    <p>Upload an image to /classify to get predictions.</p>
    """

@app.route('/classify', methods=['POST'])
def classify_image():
    """
    Classify uploaded image using transfer learning model.

    For this demo version, returns mock predictions.
    In production, this would use the actual TensorFlow model.
    """
    try:
        # Get uploaded file
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Read and process image
        logger.info(f"Processing image: {file.filename}")

        # In a real implementation, load the image and process it:
        # image = Image.open(BytesIO(file.read()))
        # image = image.resize((224, 224))
        # image_array = np.array(image) / 255.0

        # Load model and predict:
        # predictions = model.predict(np.expand_dims(image_array, axis=0))
        # top_classes = predictions.argsort()[0][-3:][::-1]
        # confidences = predictions[0][top_classes]

        # For demo, simulate predictions
        import random
        top_class = random.randint(0, 9)
        confidence = random.uniform(0.75, 0.95)

        # Create mock predictions for top 3
        predictions = []
        used_classes = {top_class}

        # Add top prediction
        predictions.append({
            'class_index': top_class,
            'class_name': CIFAR_CLASSES[top_class],
            'confidence': float(confidence)
        })

        # Add 2 more predictions
        while len(predictions) < 3:
            rand_class = random.randint(0, 9)
            if rand_class not in used_classes:
                predictions.append({
                    'class_index': rand_class,
                    'class_name': CIFAR_CLASSES[rand_class],
                    'confidence': float(random.uniform(0.1, confidence - 0.1))
                })
                used_classes.add(rand_class)

        # Sort by confidence
        predictions.sort(key=lambda x: x['confidence'], reverse=True)

        response = {
            'success': True,
            'predictions': predictions,
            'top_prediction': {
                'class': CIFAR_CLASSES[predictions[0]['class_index']],
                'confidence': predictions[0]['confidence']
            },
            'model_info': {
                'architecture': 'VGG16',
                'base_model': 'VGG16 (pre-trained on ImageNet)',
                'fine_tuned_dataset': 'CIFAR-10',
                'input_size': '224x224x3',
                'classes': len(CIFAR_CLASSES)
            }
        }

        logger.info(f"Classification complete: {response['top_prediction']}")
        return jsonify(response)

    except Exception as e:
        logger.error(f"Error classifying image: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Failed to classify image',
            'details': str(e)
        }), 500

@app.route('/model_info')
def get_model_info():
    """Get information about the classification model."""
    return jsonify({
        'model_name': 'Transfer Learning Image Classifier',
        'base_model': 'VGG16',
        'pre_trained_on': 'ImageNet',
        'fine_tuned_on': 'CIFAR-10',
        'num_classes': 10,
        'classes': CIFAR_CLASSES,
        'input_shape': [224, 224, 3],
        'framework': 'TensorFlow/Keras',
        'features': [
            'Transfer Learning',
            'Fine-tuning',
            'Data Augmentation',
            'Dropout Regularization',
            'Batch Normalization'
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting AI Image Classifier backend on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
