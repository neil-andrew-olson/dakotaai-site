#!/usr/bin/env python3
"""Simple TensorFlow.js model converter"""

import subprocess
import sys

print("=" * 50)
print("Fixing NumPy/TensorFlow.js compatibility...")
print("=" * 50)

# Step 1: Install compatible versions
print("\n1. Installing compatible TensorFlow.js...")
cmd = [sys.executable, "-m", "pip", "install", "tensorflowjs==3.18.0", "numpy==1.21.0", "--quiet"]
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    print("Compatible packages installed!")
else:
    print("Package installation failed")
    print(result.stderr)
    sys.exit(1)

# Step 2: Try the conversion with the compatible versions
print("\n2. Converting model...")
conversion_script = '''
import tensorflow as tf
from tensorflow import keras
from tensorflowjs import converters
import os
os.chdir("C:/Users/neil/Desktop/transfer-image-classifier")
model = keras.models.load_model("models/transfer_model.h5")
print("Model loaded!")
converters.save_keras_model(model, "../dakotaai-site/demos/tfjs_model")
print("Model converted successfully!")
'''

conversion_cmd = [sys.executable, "-c", conversion_script]
result = subprocess.run(conversion_cmd, capture_output=True, text=True)

if result.returncode == 0:
    print("\nSUCCESS! Conversion completed!")
    print("You can now open demos/image_classifier.html to use your real AI model!")
else:
    print("Conversion failed:")
    print(result.stderr)
