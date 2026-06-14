# 🧠 AI Handwritten Digit Recognition System

A Deep Learning-based web application that recognizes handwritten digits using a Convolutional Neural Network (CNN). The system is trained on the MNIST dataset and provides real-time predictions through an interactive Flask web interface.

---

## 📌 Project Overview

The AI Handwritten Digit Recognition System is designed to identify handwritten numerical digits (0–9) from uploaded images. The application uses a trained CNN model to analyze the image and predict the most likely digit along with its confidence score and top predictions.

This project demonstrates the practical implementation of Deep Learning, Computer Vision, and Web Development using TensorFlow and Flask.

---

## 🚀 Features

* Upload handwritten digit images
* Real-time digit prediction
* Confidence score visualization
* Top-3 prediction probabilities
* Image preview before prediction
* Drag & Drop image upload
* Modern responsive UI
* Flask-based web application
* CNN model trained on MNIST dataset

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning & Deep Learning

* TensorFlow
* Keras
* NumPy

### Web Development

* Flask
* HTML5
* CSS3
* JavaScript

### Image Processing

* Pillow (PIL)

### Dataset

* MNIST Handwritten Digit Dataset

---

## 🧠 Model Architecture

The project uses a Convolutional Neural Network (CNN) consisting of:

* Input Layer (28×28 grayscale image)
* Convolution Layer (32 Filters)
* Max Pooling Layer
* Convolution Layer (64 Filters)
* Max Pooling Layer
* Flatten Layer
* Dense Layer (128 Neurons)
* Output Layer (10 Classes)

---

## 📊 Model Performance

| Metric              | Value    |
| ------------------- | -------- |
| Training Accuracy   | ~99%     |
| Validation Accuracy | ~99%     |
| Dataset             | MNIST    |
| Classes             | 10 (0–9) |

---
## 📸 Screenshots

Home Page
<img width="1918" height="842" alt="Screenshot 2026-06-14 082720" src="https://github.com/user-attachments/assets/fb259e5f-1045-4e79-8b99-aaa85507329c" />

Prediction Result
<img width="1918" height="862" alt="Screenshot 2026-06-14 082732" src="https://github.com/user-attachments/assets/684f63bb-5db2-4289-98ea-a2b163a4058a" />

---
## 🎥 Demo Video
Watch the project demonstration here:
https://drive.google.com/file/d/1sSY5oYyQjvmCgHUNWpAq0fPNsm2x7s7W/view?usp=sharing

---
## 📂 Project Structure

```text
CodeAlpha_Handwritten_Recognition/
│
├── app.py
├── train.py
├── predict.py
├── requirements.txt
├── README.md
│
├── model/
│   └── handwritten_model.keras
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── uploads/
│
└── templates/
    ├── index.html
    └── result.html
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/CodeAlpha_Handwritten_Recognition.git
```

### Navigate to Project

```bash
cd CodeAlpha_Handwritten_Recognition
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 📷 Application Workflow

1. Upload a handwritten digit image.
2. Preview the selected image.
3. Click "Predict Digit".
4. CNN model processes the image.
5. Predicted digit and confidence score are displayed.
6. Top prediction probabilities are shown.

---

## 🎯 Future Enhancements

* Recognition of handwritten alphabets
* Multi-digit number recognition
* Real-time webcam prediction
* Mobile-friendly PWA version
* Model deployment on cloud platforms
* Support for custom datasets

---

## 🎓 Internship Information

This project was developed as part of the **CodeAlpha Machine Learning Internship Program**.

Task: **Handwritten Character Recognition**

---

## 👨‍💻 Author

Shashank Srivastava

Machine Learning Intern | Python Developer | AI Enthusiast

---

## 📜 License

This project is developed for educational and internship purposes.
