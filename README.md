# Skin Disease Classification

![Skin Disease Classification](https://img.shields.io/badge/Medical%20AI-Skin%20Disease%20Classification-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey)
![Python](https://img.shields.io/badge/Python-3.8+-informational)

An AI-powered web application that uses convolutional neural networks (CNNs) to accurately classify skin diseases from uploaded images.

## 📋 Overview

This project leverages deep learning to classify skin disease images into one of eight categories:
- Cellulitis
- Impetigo
- Athlete's Foot
- Nail Fungus
- Ringworm
- Cutaneous Larva Migrans
- Chickenpox
- Shingles

Built with a modern tech stack including TensorFlow, Flask, and Tailwind CSS, this project demonstrates the practical application of CNNs in healthcare.

## ✨ Features

- **Easy-to-use interface**: Simple drag-and-drop or click-to-upload functionality
- **Real-time processing**: Instant analysis of uploaded skin images
- **Responsive design**: Works seamlessly on both desktop and mobile devices
- **High accuracy**: Trained on a diverse dataset to ensure reliable disease classification

## 🛠️ Technologies Used

- **TensorFlow/Keras**: Deep learning library used to build and train the CNN model
- **Flask**: Lightweight web framework for the backend
- **Tailwind CSS**: Utility-first CSS framework for modern UI design
- **Python**: Core programming language for the project
- **PIL/Pillow**: Image processing library for Python

## 🔧 Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/skin-disease-classification.git
   cd skin-disease-classification
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Open your browser and navigate to**
   ```
   http://127.0.0.1:5000/
   ```

## 📊 Model Architecture

The project uses a Convolutional Neural Network (CNN) architecture specifically designed for image classification tasks. The model was trained on a dataset of skin disease images from Kaggle.

Key aspects of the model:
- Multiple convolutional layers for feature extraction
- Max pooling layers to reduce spatial dimensions
- Dropout layers to prevent overfitting
- Dense layers for classification
- Trained with data augmentation techniques to improve generalization

## 📁 Project Structure

```
Skin-Disease-Prediction/
├── main.py                      # Flask application entry point
├── README.md                    # Project documentation
├── requirements.txt             # Dependencies
├── Skin_Disease_Classification.ipynb  # Model training notebook
├── skin_disease_model.h5        # Trained CNN model
├── static/                      # Static files
│   ├── index.js                 # Frontend JavaScript
│   └── style.css                # CSS styles
└── templates/                   # HTML templates
    └── index.html               # Main application page
```

## ⚠️ Disclaimer

This application is intended for educational and research purposes only. It should not replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

## 🔮 Future Improvements

- Add more disease categories to the classification model
- Implement additional visualization tools for model interpretation
- Develop a mobile application version
- Add user accounts to track diagnostic history
- Implement model confidence scores for predictions

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


Made with ❤️ for advancing AI in healthcare

## Project History

Initial commit for skin disease classification project.