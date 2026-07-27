# 📦 Smart Warehouse Inventory Detection

An AI-powered warehouse inventory detection system built using **YOLOv8n** and **Streamlit**. The application automatically detects warehouse inventory objects from uploaded images, draws bounding boxes around detected items, generates an inventory summary, and allows users to download the annotated prediction results.

The project demonstrates the application of **Deep Learning** and **Computer Vision** for warehouse inventory monitoring by leveraging a custom-trained YOLOv8n object detection model optimized through multiple training experiments.

---

# 🌐 Live Demo

🚀 **Streamlit Application**

> https://smartwarehouseinventoryproject-xe9vamchwuawtt4y3k3qed.streamlit.app/

---

# 🚀 Project Overview

Warehouse inventory management is a critical component of logistics and supply chain operations. Traditional inventory inspection is often manual, time-consuming, and prone to human error, especially in large warehouses containing thousands of items.

This project addresses these challenges by using a **custom-trained YOLOv8n object detection model** capable of automatically detecting multiple warehouse inventory objects from uploaded images.

To improve detection performance, multiple experiments were conducted by varying image resolution and training duration. The final model was selected based on comprehensive evaluation using **Precision, Recall, mAP@0.5, and mAP@0.5:0.95** metrics.

The trained model has been integrated into an interactive **Streamlit web application**, allowing users to upload warehouse images, visualize detected objects, review inventory summaries, and download annotated prediction results.

---

# ✨ Features

- Upload warehouse inventory images
- Automatic object detection using a custom-trained YOLOv8n model
- Automatic image resizing based on uploaded image resolution
- Bounding box visualization with class labels
- Inventory summary with detected object counts
- Detection confidence scores
- Download annotated prediction images
- Optimized YOLOv8n model obtained through multiple training experiments
- Fast and interactive Streamlit interface

---

# 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Deep Learning | YOLOv8n (Ultralytics) |
| Computer Vision | OpenCV |
| Web Framework | Streamlit |
| Image Processing | Pillow (PIL) |
| Data Handling | NumPy, Pandas |
| Visualization | Matplotlib |
| Development Environment | VS Code |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
Smart_Warehouse_Inventory_Project/
│
├── app/
│   └── app.py
│
├── dataset/
│   ├── images/
│   ├── labels/
│   ├── models/
│   │   ├── best.pt                # 512×512 model (20 epochs)
│   │   ├── best_640.pt            # 640×640 model (20 epochs)
│   │   ├── best_100epochs.pt      # Final deployed model (640×640, 100 epochs)
│   │   ├── last.pt
│   │   ├── last_640.pt
│   │   ├── last_100epochs.pt
│   │   └── yolov8n.pt
│   └── data.yaml
│
├── notebooks/
│
├── output/                 # Prediction outputs
│
├── output_imgsz_640/       # Results from 640×640 (20 epochs)
│
├── output_100epochs/       # Results from final 100-epoch model
│
├── test_images/
│
├── requirements.txt
├── packages.txt
├── README.md
├── .gitignore
└── .gitattributes
```
---

# 📊 Dataset

The project uses a **synthetic Warehouse Inventory Object Detection Dataset** containing warehouse scenes with object annotations in **YOLO format**. The dataset includes multiple categories of commonly found warehouse objects such as pallets, boxes, forklifts, barrels, containers, safety signs, shelves, and other inventory items.

### Dataset Details

| Property | Value |
|----------|-------|
| Dataset Type | Object Detection |
| Annotation Format | YOLO |
| Number of Classes | 25 |
| Image Resolution | 512 × 512 pixels |
| Framework | Ultralytics YOLOv8 |

> **Note:** The original dataset images are not included in this repository due to their large size. Only the trained models and project code are provided.

---

# 🎯 Model Training Experiments

To improve object detection performance, three different training experiments were conducted using the same YOLOv8n architecture. Each experiment modified either the input image size or the number of training epochs.

The objective was to analyze how these changes affected the model's Precision, Recall, and mAP scores, and then select the best-performing model for deployment.

---

# 📈 Model Performance

## 🥇 Final Deployed Model

The final Streamlit application uses the **best_100epochs.pt** model.

| Metric | Value |
|--------|-------:|
| Model | YOLOv8n |
| Image Size | **640 × 640** |
| Epochs | **100** |
| Precision | **0.7493** |
| Recall | **0.7096** |
| mAP@0.5 | **0.7631** |
| mAP@0.5:0.95 | **0.6813** |

---

## 📊 Training Experiment Comparison

| Experiment | Model File | Image Size | Epochs | Precision | Recall | mAP@0.5 |
|------------|------------|-----------:|--------:|----------:|-------:|---------:|
| Experiment 1 | `best.pt` | 512 × 512 | 20 | 0.6569 | 0.5392 | 0.5880 |
| Experiment 2 | `best_640.pt` | 640 × 640 | 20 | 0.6960 | 0.5670 | 0.6148 |
| ✅ Final Model | `best_100epochs.pt` | **640 × 640** | **100** | **0.7493** | **0.7096** | **0.7631** |

---

# 🧪 Model Optimization

Rather than selecting the first trained model, multiple experiments were performed to systematically improve detection performance.

### ✅ Experiment 1 – Baseline Model

- Model: YOLOv8n
- Image Size: **512 × 512**
- Epochs: **20**
- Output Model: **best.pt**

This experiment established the baseline performance for the project. While the model detected warehouse objects successfully, there was room for improvement in localization accuracy and detection confidence.

---

### ✅ Experiment 2 – Higher Image Resolution

- Model: YOLOv8n
- Image Size: **640 × 640**
- Epochs: **20**
- Output Model: **best_640.pt**

Increasing the image resolution allowed the model to capture finer object details, resulting in improvements across Precision, Recall, and mAP compared to the baseline model.

---

### ✅ Experiment 3 – Extended Training (Final Model)

- Model: YOLOv8n
- Image Size: **640 × 640**
- Epochs: **100**
- Output Model: **best_100epochs.pt**

The final experiment retained the higher image resolution while increasing the training duration from **20 epochs to 100 epochs**. This enabled the model to learn more robust feature representations and significantly improved overall detection performance.

This model achieved the highest evaluation metrics and was selected as the final deployment model for the Streamlit application.

---

# 📌 Experiment Summary

The progressive optimization strategy led to consistent improvements in object detection performance.

| Improvement | Result |
|------------|--------|
| Increased Image Size | Improved object localization and detection accuracy |
| Increased Training Epochs | Better feature learning and higher validation performance |
| Final Model Selection | Highest Precision, Recall, and mAP values among all experiments |

The final deployed model (**best_100epochs.pt**) demonstrated the best balance between accuracy and generalization, making it the most suitable choice for warehouse inventory detection.

---

# ⚙️ Installation

Follow the steps below to set up and run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/Aishwarya-kuchana/Smart_Warehouse_Inventory_Project.git
```

---

## 2. Navigate to the Project Directory

```bash
cd Smart_Warehouse_Inventory_Project
```

---

## 3. Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

---

## 4. Run the Streamlit Application

```bash
streamlit run app/app.py
```

After running the command, Streamlit will automatically open the application in your default web browser.

---

# ▶️ Application Workflow

The workflow of the Smart Warehouse Inventory Detection application is shown below.

### Step 1 – Upload Image

Upload a warehouse image using the Streamlit interface.

⬇️

### Step 2 – Object Detection

The custom-trained **YOLOv8n** model processes the uploaded image and detects warehouse inventory objects.

⬇️

### Step 3 – Bounding Box Visualization

Detected objects are highlighted with:

- Bounding Boxes
- Class Labels
- Confidence Scores

⬇️

### Step 4 – Inventory Summary

The application generates an inventory summary showing:

- Total detected objects
- Individual object counts
- Confidence values

⬇️

### Step 5 – Download Prediction

Users can download the annotated prediction image for future reference.

---

# 📸 Application Screenshots

> **Note:** Replace the placeholders below with your latest screenshots after deploying the final version of the application.

---

## 🏠 Home Page

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/2fade3d3-beb1-45ef-8a04-0c9b7b50c2c6" />


---

## 📤 Upload Image

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/da3f1aac-6c64-4d89-9ee4-eb97e11e17cd" />


---

## 🎯 Detection Result

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/e472a298-6659-43f5-a708-f509a74c5566" />


---

## 📊 Inventory Summary

<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/5f4780c5-94ec-44af-9a61-ae937a88c5d5" />


---

# 💡 Key Highlights

- Developed an end-to-end warehouse inventory detection system using YOLOv8n.
- Conducted multiple experiments to optimize model performance.
- Improved object detection accuracy by increasing image resolution and training duration.
- Integrated the final model into a Streamlit web application.
- Supports image upload, object detection, inventory summarization, and prediction download.
- Designed a user-friendly interface for warehouse inventory monitoring.
---

# ⚠️ Limitations

Although the model demonstrates strong performance on the evaluation dataset, it has several limitations:

- The model was trained on a **synthetic warehouse dataset**, which may differ from real-world warehouse environments.
- Detection accuracy may decrease under challenging conditions such as poor lighting, heavy occlusion, motion blur, or unusual camera angles.
- Small or partially visible objects may occasionally be missed.
- Performance depends on the similarity between uploaded images and the training dataset.
- The application currently performs inference on static images only.

---

# 🚀 Future Enhancements

Several improvements can be made to extend the capabilities of this project:

- Real-time webcam object detection
- Video-based warehouse inventory monitoring
- Warehouse analytics dashboard
- Barcode and QR code integration
- Inventory management with database integration
- Automatic inventory report generation
- Hyperparameter optimization for further performance improvement
- Data augmentation to improve detection of underrepresented object classes
- Support for custom warehouse datasets
- Docker containerization
- Cloud deployment using AWS, Azure, or Google Cloud Platform

---

# 📚 Learning Outcomes

This project provided hands-on experience with:

- Object Detection using YOLOv8n
- Computer Vision using OpenCV
- Deep Learning model training and evaluation
- Dataset preprocessing and annotation analysis
- Model performance evaluation using Precision, Recall, mAP@0.5, and mAP@0.5:0.95
- Hyperparameter experimentation
- Streamlit web application development
- Model deployment
- Git and GitHub version control

---

# 🎯 Conclusion

This project demonstrates an end-to-end AI-powered warehouse inventory detection system using **YOLOv8n** and **Streamlit**.

Multiple experiments were conducted to improve model performance by increasing the input image size and training duration. The final model achieved significant improvements in Precision, Recall, and mAP compared to the baseline model and was selected for deployment.

The completed application provides an intuitive interface for warehouse inventory detection, making it a practical demonstration of Deep Learning and Computer Vision techniques for inventory monitoring.

---

# 👩‍💻 Author

**Aishwarya Kuchana**

Aspiring AI & Data Analyst | Python | SQL | Machine Learning | Deep Learning | Computer Vision

**GitHub**

https://github.com/Aishwarya-kuchana

**LinkedIn**

https://www.linkedin.com/in/aishwarya-kuchana/

---

# 🙏 Acknowledgements

Special thanks to:

- **Ultralytics** for providing the YOLOv8 framework.
- **Streamlit** for enabling rapid development of interactive web applications.
- The creators of the warehouse object detection dataset used for training and evaluation.
- The open-source Python community for the libraries and tools that made this project possible.

---

# ⭐ Support

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.

Your support is appreciated and motivates future improvements and open-source contributions.
