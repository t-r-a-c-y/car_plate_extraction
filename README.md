# 🚗 Car Number Plate Extraction Pipeline

A complete **end-to-end number plate recognition system** built using classical computer vision techniques, inspired by:

📘 *"Car Number Plate Extraction in Three Steps.pdf"*

---

## ✨ Features

✔️ Real-time number plate detection  
✔️ Perspective correction (alignment)  
✔️ OCR-based text extraction (Tesseract)  
✔️ Format validation (Rwandan plates 🇷🇼)  
✔️ Temporal smoothing for accuracy  
✔️ Automatic logging to CSV  
✔️ Duplicate suppression  

---

## 🧠 Pipeline Overview

The system processes input frames through the following stages:

### 🔍 1. Detection (`detect.py`)
- Convert image to grayscale  
- Apply Gaussian blur  
- Perform Canny edge detection  
- Detect contours  
- Filter by:
  - Area
  - Aspect ratio  

---

### 🧭 2. Alignment (`align.py`)
- Applies **perspective transformation**
- Converts detected plate into a clean rectangular view  
- Improves OCR accuracy  

---

### 🔤 3. OCR (`ocr.py`)
- Uses **Tesseract OCR**
- Optimized for:
  - Single-line text
  - Character whitelisting  

---

### ✅ 4. Validation (`validate.py`)
- Uses regex to validate Rwandan plates:

```regex
[A-Z]{3}[0-9]{3}[A-Z]


🔁 5. Temporal Smoothing (temporal.py)

Maintains a buffer of detected plates

Uses majority voting to improve reliability

💾 6. Logging (temporal.py)

Saves results to:

data/plates.csv

Includes:

->Plate number

->Timestamp

->Prevents duplicate entries

📁 Project Structure

.
├── data/
│   └── plates.csv          # Extracted plate logs
├── screenshots/            # Output samples
├── src/
│   ├── align.py            # Perspective correction
│   ├── camera.py           # Camera test
│   ├── detect.py           # Plate detection
│   ├── ocr.py              # OCR processing
│   ├── temporal.py         # Main pipeline
│   └── validate.py         # Regex validation
├── README.md
└── requirements.txt


⚙️ Installation
📌 Prerequisites

Python 3.x

Tesseract OCR

Install Tesseract:
OS	Command
Linux	sudo apt install tesseract-ocr
macOS	brew install tesseract
Windows	Install from UB Mannheim build
📦 Install Dependencies
pip install -r requirements.txt

🚀 Usage
🎥 1. Test Camera
python src/camera.py

🔍 2. Run Detection Only
python src/detect.py

⚡ 3. Run Full Pipeline
python src/temporal.py

📸 Results
🔍 Detection

🧭 Alignment

🚀 Full Pipeline

🧪 Example Output
Plate, Timestamp
RAB123C, 2026-03-18 14:32:10
RAC456D, 2026-03-18 14:35:42

🛠️ Technologies Used

Python 🐍

OpenCV 👁️

Tesseract OCR 🔤

NumPy 🔢

📈 Future Improvements

🔥 Deep learning-based detection (YOLO, SSD)

🌙 Night-time plate enhancement

📱 Web dashboard for monitoring

☁️ Cloud storage integration

🎯 Multi-country plate support

🤝 Contributing

Contributions are welcome!

# Fork the repo
# Create your feature branch
git checkout -b feature/AmazingFeature

# Commit your changes
git commit -m "Add some AmazingFeature"

# Push to branch
git push origin feature/AmazingFeature

📜 License

This project is for educational purposes.

💡 Author

Tracy
🚀 Software Engineer | AI & Computer Vision Enthusiast

⭐ If you like this project, consider giving it a star!


---

## 🔥 What I improved (so you learn)

- Better **visual hierarchy** (emojis + sections)
- Clear **pipeline explanation**
- Cleaner **code blocks**
- Added **features & future improvements**
- More **professional GitHub style**

---

If you want, I can also:
- Make it look like a **top GitHub trending repo**
- Add **badges (build, version, license)**
- Or create a **portfolio-level README (next level 🔥)**