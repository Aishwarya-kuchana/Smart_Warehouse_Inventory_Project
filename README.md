# 📦 Smart Warehouse Inventory Detection

An AI-powered warehouse inventory detection system built using **YOLOv8** and **Streamlit**. The application detects warehouse inventory objects from uploaded images, draws bounding boxes around detected objects, provides an inventory summary, and allows users to download the prediction results.

---
## Live Demo

🚀 **Streamlit Application**
https://smartwarehouseinventoryproject-9k9jfskt66cgjqsyu4ttic.streamlit.app/
> Upload a warehouse image to detect inventory objects and generate an inventory summary.

---
## 🚀 Project Overview

Warehouse inventory management is an essential part of logistics and supply chain operations. Manual inventory tracking is time-consuming and prone to errors.

This project uses a custom-trained **YOLOv8 Object Detection Model** to automatically identify warehouse inventory items from images and present the results through an interactive **Streamlit** web application.

---

## ✨ Features

- Upload warehouse images
- Automatic object detection using YOLOv8
- Automatic image size selection based on uploaded image resolution
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
```
Smart_Warehouse_Inventory_Project/
│
├── app/
│   └── app.py
│
├── dataset/
│   ├── models/
│   │   ├── best.pt
│   │   └── best_640.pt
│   ├── labels/
│   └── data.yaml
│
├── notebooks/
├── output/
├── output_imgsz_640/
├── test_images/
│
├── .gitattributes
├── .gitignore
├── packages.txt
├── requirements.txt
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
## 📈 Model Performance

The YOLOv8 model was trained on a synthetic warehouse inventory dataset and evaluated on the validation set.

| Metric | Value |
|--------|-------:|
| Model | YOLOv8n |
| Image Size | 640 × 640 |
| Precision | 0.6960 |
| Recall | 0.5670 |
| mAP@0.5 | 0.6148 |

**Model Comparison**

| Image Size | Precision | Recall | mAP@0.5 |
|------------|----------:|-------:|---------:|
| 512 × 512 | 0.6569 | 0.5392 | 0.5880 |
| **640 × 640** | **0.6960** | **0.5670** | **0.6148** |

The 640×640 model achieved better detection performance across all evaluation metrics and was selected for deployment in the Streamlit application.
The deployed Streamlit application uses the **best_640.pt** model for inference.
---
## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Aishwarya-kuchana/Smart_Warehouse_Inventory_Project.git
```

### Navigate to the project directory

```bash
cd Smart_Warehouse_Inventory_Project
```

### Install dependencies

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
2. Detect warehouse inventory objects.
3. View detected objects with bounding boxes.
4. Review inventory summary and confidence scores.
5. Download the prediction image.

---

## 📸 Screenshots

### Home Page

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/651eb7a9-994d-4a2f-bd75-a800fda0fe3e" />



### Detection Result

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/e09ad917-b44b-45b6-9cd8-e917cbe35570" />


### Inventory Summary

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/a58dc6ca-2b05-4b4e-b078-350f7cccaad1" />

---
## ⚠️ Limitations

- The model was trained on a synthetic warehouse dataset.
- Performance may decrease on some real-world warehouse images because of differences in lighting, object appearance, and camera angles.
- Performance depends on the similarity between uploaded images and the training dataset.
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

If you found this project helpful, consider giving it a ⭐ on GitHub.
