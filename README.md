✅ README.md
# 🫁 Sleep Apnea Detection Using CNN-BiLSTM (ECG Spectrogram Analysis)

This project detects **Sleep Apnea** using ECG signals by converting them into **spectrogram images**, which are then classified using a trained **CNN + BiLSTM hybrid deep learning model**.

---

## 📌 Project Overview

Sleep apnea is a serious sleep disorder where breathing repeatedly stops and starts.  
Our approach uses:

- ECG signal preprocessing
- Spectrogram transformation (64×64 grayscale)
- CNN + BiLSTM classification model

The model outputs:

✅ **Normal Breathing**  
❌ **Apnea Detected**

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| Model | CNN + BiLSTM Hybrid |
| Input | Spectrogram image (64×64) |
| Output | Binary — Apnea / Normal |
| Framework | Flask (Python backend) |
| Frontend | HTML + CSS |
| Model File | `sleep_apnea_model_streaming.h5` |

---

## 📂 Project Structure



sleep_apnea/
│── app.py # Flask backend
│── requirements.txt # Dependencies
│── sleep_apnea_model_streaming.h5
│
├── templates/
│ ├── index.html
│ └── result.html
│
└── static/
└── style.css


---

## 📥 Dataset Used

PhysioNet **Apnea-ECG Database**

🔗 Download dataset here:  
https://physionet.org/content/apnea-ecg/1.0.0/

---

## ✅ How to Run the Project Locally

### 1️⃣ Create virtual environment (recommended)

```sh
python -m venv venv


Activate it:

OS	Command
Windows	venv\Scripts\activate
Mac/Linux	source venv/bin/activate
2️⃣ Install dependencies
pip install -r requirements.txt


If requirements.txt file not available, install manually:

pip install flask tensorflow pillow numpy

3️⃣ Run the Flask app
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000/


Upload a spectrogram image and the model will classify:

Normal Breathing

Sleep Apnea Detected

🧠 Model Architecture
Input (64x64 Spectrogram)
        ↓
Conv2D → MaxPool2D
        ↓
Conv2D → MaxPool2D
        ↓
Reshape → Bi-LSTM
        ↓
Dense → Sigmoid Output


Total Parameters: 146,433

Accuracy: 96.51%

AUC: 0.9937

🛠 Tech Stack
Component	Technology
Backend	Python (Flask)
Deep Learning	TensorFlow / Keras
Frontend	HTML + CSS
Data Processing	NumPy, Pillow
📌 Git Commands to Push Project
git init
git add .
git commit -m "Initial commit - sleep apnea detection"
git branch -M main
git remote add origin https://github.com/Jagadhish3/sleep_apnea.git
git push -u origin main



⭐ If you found this useful, consider giving the repo a star!
---

### ✅ Done

You can now copy-paste the above as `README.md` into GitHub.

If you want, I can also:

- Generate a **demo video script** for your project presentation
- Add **screenshots** section in README
- Deploy to **Render / AWS / Azure**

Just tell me: **"Add deployment instructions"** or **"Generate video script"**.
