# Butterfly Image Classifier - Srav's Edition

This project focuses on building a robust image classification model using Transfer Learning (VGG16) to identify 75 species of butterflies. Developed as part of an AI/ML Virtual Internship under SmartBridge.

------------------------------------------------------------

PROJECT OVERVIEW:

- Model: VGG16 (Transfer Learning)
- Dataset: 6499 butterfly images (75 species)
- Framework: TensorFlow + Keras
- Deployment: Flask Web App
- Goal: Upload butterfly image → Predict species → Display output

------------------------------------------------------------

PROJECT FLOW:

1. Data Collection:
   - Dataset link: https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species

2. Preprocessing:
   - Resize images
   - Normalize data
   - Augment dataset

3. Model Building:
   - Base model: VGG16 (pretrained, frozen layers)
   - Custom dense layers added
   - Trained with EarlyStopping + ModelCheckpoint
   - Output layer: 75-class softmax
   - Model saved as: butterfly_model_sravs.h5

4. Prediction & Deployment:
   - Model integrated into Flask app
   - HTML frontend collects image input
   - Predicted label shown on UI

------------------------------------------------------------

TECH STACK:

- Python
- TensorFlow / Keras
- Flask
- NumPy, Pandas, Matplotlib
- GitHub

------------------------------------------------------------

PROJECT FILES:

- app_sravs.py              → Flask backend code
- butterfly_model_sravs.h5  → Saved trained model
- sravs_model_train.ipynb   → Jupyter Notebook (training)
- sravs_predict.ipynb       → Jupyter Notebook (testing)
- class_list/               → Contains class labels
- templates/index.html      → Web UI for image input
- templates/output.html     → Prediction result page

------------------------------------------------------------

HOW TO RUN:

1. Install dependencies (Anaconda preferred):
   pip install tensorflow flask numpy pandas matplotlib

2. Run Flask app:
   python app_sravs.py

3. Open browser:
   http://127.0.0.1:5000

------------------------------------------------------------

AUTHOR:

Sravan (Srav's)  
AI/ML Internship Project - SmartBridge

------------------------------------------------------------

IMPORTANT LINKS:

- GitHub Repo: https://github.com/sravan0937/butterfly-classifier-sravs
- Dataset: https://www.kaggle.com/datasets/gpiosenka/butterfly-images40-species

