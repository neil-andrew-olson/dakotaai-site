#!/usr/bin/env python3
"""
Script to convert Keras model to TensorFlow.js format
This script fixes the NumPy compatibility issues automatically
"""

import os
import sys
import subprocess

def main():
    print("🔧 TensorFlow.js Model Converter (Fixed Version)")
    print("=" * 50)

    # Change to the correct directory
    target_dir = "C:/Users/neil/Desktop/transfer-image-classifier"
    os.chdir(target_dir)
    print(f"📁 Changed to directory: {target_dir}")

    # Check if model exists
    model_path = "models/transfer_model.h5"
    if not os.path.exists(model_path):
        print(f"❌ Error: Model file not found: {model_path}")
        print("Please ensure you're running from the transfer-image-classifier directory")
        sys.exit(1)

    print(f"📖 Found model: {model_path}")

    # Create isolated conversion environment
    try:
        print("\n🔄 Creating isolated conversion environment...")

        # Use subprocess to run conversion with specific package versions
        conversion_cmd = [
            sys.executable, "-m", "pip", "install",
            "tensorflowjs==3.18.0", "numpy==1.21.0", "--upgrade", "--quiet"
        ]

        print("📦 Installing compatible TensorFlow.js version...")
        result = subprocess.run(conversion_cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"❌ Package installation failed: {result.stderr}")
            print("Try running: pip install tensorflowjs==3.18.0 numpy==1.21.0 --upgrade")
            sys.exit(1)

        print("✅ Compatible packages installed!")

        # Now try the conversion
        print("\n🚀 Converting your model to TensorFlow.js format...")

        # Import tensorflowjs with specified version
        try:
            from tensorflowjs import converters
            import tensorflow as tf
            from tensorflow import keras

        except ImportError as e:
            print(f"❌ Import failed after package installation: {e}")
            sys.exit(1)

        # Load the model
        print("Loading your trained model...")
        model = keras.models.load_model(model_path)
        print("✅ Model loaded successfully!")

        # Convert to TensorFlow.js
        output_dir = "../dakotaai-site/demos/tfjs_model"  # Go up and into demos
        print(f"Converting to: {output_dir}")

        converters.save_keras_model(model, output_dir)
        print(f"✅ Model converted successfully!")

        # Verify output files
        if os.path.exists(os.path.join(output_dir, 'model.json')):
            print("
📁 Output files created:"            for file in os.listdir(output_dir):
                file_path = os.path.join(output_dir, file)
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"  - {file}: {size_mb:.1f} MB")
            print("\n🎉 SUCCESS! Your demo is now ready!")
            print("🔗 Open demos/image_classifier.html in your browser")
            print("🤖 It should now load and use your real trained model!")
        else:
            print("❌ Conversion completed but output files not found")

    except Exception as e:
        print(f"❌ Conversion failed: {e}")

        # Provide troubleshooting
        print("\n🔧 Troubleshooting:")
        print("1. Try closing all Python processes and restarting")
        print("2. Check if your model file is not corrupted")
        print("3. Try upgrading TensorFlow: pip install tensorflow --upgrade")
        print("4. If issues persist, we can create a smaller demo model")

if __name__ == '__main__':
    main()
