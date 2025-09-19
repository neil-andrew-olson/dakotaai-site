# TensorFlow.js Model Setup for Image Classifier Demo

This directory should contain your TensorFlow.js converted model files from your transfer-image-classifier repository.

## 🚀 How to Convert and Add Your Model

### Step 1: Install TensorFlow.js Converter

```bash
pip install tensorflowjs
```

### Step 2: Convert Your Trained Model

Make sure you have your trained model file (e.g., `transfer_model.h5`) from your transfer-image-classifier repository, then run:

```bash
# Navigate to your transfer-image-classifier directory
cd /path/to/your/transfer-image-classifier

# Convert the Keras model to TensorFlow.js format
tensorflowjs_converter --input_format keras transfer_model.h5 ./tfjs_export

# Copy the converted model to demos directory
cp -r ./tfjs_export ~/Desktop/AIprojects/dakotaai-site/demos/tfjs_model
```

### Step 3: Verify the Conversion

After conversion, you should have these files in the `demos/tfjs_model/` directory:
- `model.json` - Model architecture and configuration
- `group1-shard1of1.bin` - Model weights (may be multiple shards)

### Step 4: Test the Demo

Open `demos/image_classifier.html` in your browser. The demo will:
1. Load your converted TensorFlow.js model
2. Allow image uploads for real classification
3. Display actual predictions from your trained transfer learning model

## 📋 Model Specifications

Your model should be trained to recognize CIFAR-10 classes:
- Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck

**Input Shape:** 224x224x3 (RGB images)
**Output:** 10 classes with softmax probabilities

## 🔧 Troubleshooting

### Model Fails to Load
- Check that all TensorFlow.js files are in `demos/tfjs_model/`
- Ensure `tensorflowjs_converter` is version compatible with your TensorFlow version
- Verify your model architecture is compatible with TensorFlow.js

### Low Accuracy
- Make sure your model was properly trained on CIFAR-10 data
- Check that the input preprocessing matches your training preprocessing
- Verify the model architecture uses supported TensorFlow.js operations

### Performance Issues
- Consider using smaller model versions for web deployment
- Check browser console for WebGL backend issues

## 📖 More Resources

- [TensorFlow.js Model Conversion](https://www.tensorflow.org/js/tutorials/conversion/import_keras)
- [Supported Operations](https://github.com/tensorflow/tfjs/blob/master/tfjs-core/src/ops/ops.ts)
- [Model Optimization](https://www.tensorflow.org/js/guide/model_management)
