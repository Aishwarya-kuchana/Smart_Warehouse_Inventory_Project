# 📦 Smart Warehouse Inventory Detection

An AI-powered warehouse inventory detection system built using **YOLOv8** and **Streamlit**. The application detects warehouse inventory objects from uploaded images, draws bounding boxes around detected objects, provides an inventory summary, and allows users to download the prediction results.

---
## Live Demo

🚀 **Streamlit App:https://smartwarehouseinventoryproject-9k9jfskt66cgjqsyu4ttic.streamlit.app/
---
## 🚀 Project Overview

Warehouse inventory management is an essential part of logistics and supply chain operations. Manual inventory tracking is time-consuming and prone to errors.

This project uses a custom-trained **YOLOv8 Object Detection Model** to automatically identify warehouse inventory items from images and present the results through an interactive **Streamlit** web application.

---

## ✨ Features

- Upload warehouse images
- Automatic object detection using YOLOv8
- Adjustable confidence threshold
- Dynamic image size selection
- Bounding box visualization
- Inventory summary with object counts
- Detection confidence scores
- Download prediction results
- Fast and interactive Streamlit interface

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Deep Learning | YOLOv8 (Ultralytics) |
| Computer Vision | OpenCV |
| Web Framework | Streamlit |
| Image Processing | Pillow (PIL) |
| Data Handling | NumPy, Pandas |
| Visualization | Matplotlib |
| Development | VS Code |

---

## 📂 Project Structure

```text
Smart-Warehouse-Inventory-Detection/
│
├── app/
│   └── app.py
│
├── dataset/
│   ├── models/
│   │   └── best.pt
│   ├── labels/
│   └── data.yaml
│
├── notebooks/
│
├── output/
│
├── test_images/
│
├── utils/
│
├── requirements.txt
├── train.py
├── predict.py
├── .gitignore
└── README.md
```

---

## 📊 Dataset

- Warehouse Inventory Object Detection Dataset
- YOLO Annotation Format
- Multiple warehouse object categories
- Custom-trained YOLOv8 model

> **Note:** The original training images are not included in this repository due to their large size.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-github-username>/Smart-Warehouse-Inventory-Detection.git
```

Navigate to the project directory

```bash
cd Smart-Warehouse-Inventory-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

## 📷 Application Workflow

1. Upload a warehouse image.
2. Adjust the confidence threshold if required.
3. Detect warehouse inventory objects.
4. View detected objects with bounding boxes.
5. Review inventory summary and confidence scores.
6. Download the prediction image.

---

## 📸 Screenshots

### Home Page

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/651eb7a9-994d-4a2f-bd75-a800fda0fe3e" />



### Detection Result

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/e09ad917-b44b-45b6-9cd8-e917cbe35570" />


### Inventory Summary

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/a58dc6ca-2b05-4b4e-b078-350f7cccaad1" />

---

## 📈 Future Enhancements

- Real-time webcam detection
- Video object detection
- Warehouse analytics dashboard
- Barcode & QR code integration
- Inventory tracking with database
- Cloud deployment

---

## 👩‍💻 Author

**Aishwarya Kuchana**

GitHub: https://github.com/Aishwarya-kuchana

LinkedIn: https://www.linkedin.com/in/aishwarya-kuchana/

---

## ⭐ If you found this project useful
