#!/usr/bin/env python3
"""
Manual TensorFlow.js model conversion script
Run this in the transfer-image-classifier directory
"""

import os
import sys
import tensorflow as tf
from tensorflow import keras

def main():
    print("🔄 TensorFlow.js Model Converter")
    print("=" * 40)

    # Check if we're in the right directory
    expected_files = ['models/transfer_model.h5']
    for file in expected_files:
        if not os.path.exists(file):
            print(f"❌ Required file not found: {file}")
            print("Please run this script from the transfer-image-classifier directory")
            return

    try:
        # Load your trained model
        model_path = "models/transfer_model.h5"
        print(f"📖 Loading model from: {model_path}")
        model = keras.models.load_model(model_path)
        print("✅ Model loaded successfully!")
        print("📊 Model summary:")
        model.summary()

        # Check model compatibility
        print("\n🔍 Checking TensorFlow.js compatibility...")
        incompatible_layers = check_tfjs_compatibility(model)

        if incompatible_layers:
            print("⚠️  Warning: Found potentially incompatible layers:")
            for layer in incompatible_layers:
                print(f"  - {layer}")
            print("\nSome layers might need modification for TensorFlow.js compatibility")
        else:
            print("✅ All layers appear TensorFlow.js compatible")

        # Try the conversion
        print("\n🚀 Converting model to TensorFlow.js format...")

        try:
            import tensorflowjs as tfjs

            output_dir = "./tfjs_model_converted"
            tfjs.converters.save_keras_model(model, output_dir)
            print(f"✅ Model converted successfully to {output_dir}/")

            # Verify output files
            model_json = os.path.join(output_dir, 'model.json')
            if os.path.exists(model_json):
                print(f"📁 Output files created:")
                for file in os.listdir(output_dir):
                    file_path = os.path.join(output_dir, file)
                    size_mb = os.path.getsize(file_path) / (1024 * 1024)
                    print(f"  - {file}: {size_mb:.1f} MB")
                print("\n📝 Next steps:")
                print("1. Check the converted model: tfjs_model_converted/")
                print("2. Copy files to demo: copy *.json & *.bin files to your demo's tfjs_model directory")
                print("3. Refresh the browser to load the real AI model!")
        except ImportError:
            print("❌ TensorFlow.js not installed. Please run: pip install tensorflowjs")
        except Exception as e:
            print(f"❌ Conversion failed: {e}")
            print("\n🔧 Troubleshooting suggestions:")
            print("1. Try TensorFlow version 2.13-2.15 for better compatibility")
            print("2. Advanced layers might need custom conversion")
            print("3. Consider simplifying model architecture")

    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        print("Please ensure you have a trained transfer_model.h5 file")

def check_tfjs_compatibility(model):
    """Check if model is compatible with TensorFlow.js"""
    unsupported_layers = []

    for layer in model.layers:
        layer_type = type(layer).__name__
        # Comprehensive list of TensorFlow.js supported layer types
        supported_types = [
            'InputLayer', 'Dense', 'Conv2D', 'MaxPooling2D', 'AveragePooling2D',
            'GlobalAveragePooling2D', 'GlobalMaxPooling2D', 'BatchNormalization',
            'Activation', 'Dropout', 'Flatten', 'Reshape', 'Concatenate',
            'Add', 'Multiply', 'Subtract', 'Rescaling', 'ZeroPadding2D',
            'ReLU', 'LeakyReLU', 'ELU', 'Softmax', 'Sigmoid', 'Tanh'
        ]

        if layer_type not in supported_types:
            unsupported_layers.append(f"{layer_type}: {layer.name}")

    return unsupported_layers

if __name__ == '__main__':
    main()
