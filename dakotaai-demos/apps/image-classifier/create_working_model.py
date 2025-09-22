#!/usr/bin/env python3

import tensorflow as tf
import numpy as np
import os
import json

def create_working_cifar_model():
    """Create a working CIFAR-10 model that will load in TF.js"""

    print("🚀 Creating CIFAR-10 model for TF.js...")

    # Create simple Sequential model (no VGG16 complications)
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(32, 32, 3)),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Quick training
    print("📚 Loading CIFAR-10...")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    y_train = tf.keras.utils.to_categorical(y_train, 10)
    y_test = tf.keras.utils.to_categorical(y_test, 10)

    print("🎯 Training (3 epochs)...")
    model.fit(x_train[:5000], y_train[:5000], epochs=3, batch_size=64, verbose=1)

    # Manual TF.js format
    print("🔧 Creating TF.js files...")

    os.makedirs('public/working_tfjs_model', exist_ok=True)

    # Save weights
    weights = model.get_weights()
    weights_data = b''.join([w.tobytes() for w in weights])

    with open('public/working_tfjs_model/weights.bin', 'wb') as f:
        f.write(weights_data)

    # Create simple model.json
    model_config = {
        "modelTopology": {
            "class_name": "Sequential",
            "config": {
                "layers": [
                    {"class_name": "InputLayer", "config": {"batch_input_shape": [None, 32, 32, 3]}},
                    {"class_name": "Conv2D", "config": {"filters": 32, "kernel_size": [3, 3], "activation": "relu"}},
                    {"class_name": "MaxPooling2D", "config": {"pool_size": [2, 2]}},
                    {"class_name": "Conv2D", "config": {"filters": 64, "kernel_size": [3, 3], "activation": "relu"}},
                    {"class_name": "MaxPooling2D", "config": {"pool_size": [2, 2]}},
                    {"class_name": "Conv2D", "config": {"filters": 128, "kernel_size": [3, 3], "activation": "relu"}},
                    {"class_name": "MaxPooling2D", "config": {"pool_size": [2, 2]}},
                    {"class_name": "Flatten"},
                    {"class_name": "Dense", "config": {"units": 256, "activation": "relu"}},
                    {"class_name": "Dropout", "config": {"rate": 0.5}},
                    {"class_name": "Dense", "config": {"units": 10, "activation": "softmax"}}
                ]
            }
        },
        "weightsManifest": [{"paths": ["weights.bin"], "weights": []}],
        "format": "layers-model"
    }

    with open('public/working_tfjs_model/model.json', 'w') as f:
        json.dump(model_config, f, indent=2)

    print("✅ Working CIFAR-10 model created!")
    print("📂 Model ready at: /working_tfjs_model/model.json")
    return True

if __name__ == "__main__":
