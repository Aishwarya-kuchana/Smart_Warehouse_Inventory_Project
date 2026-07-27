import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
from pathlib import Path
import io
from collections import Counter
import time
# page configuration
st.set_page_config(
    page_title="Smart Warehouse Inventory Detection",
    page_icon="📦",
    layout="wide"
)
# page title
st.title("📦 Smart Warehouse Inventory Detection")

st.markdown("""
### YOLOv8-Based Warehouse Object Detection System

This application detects warehouse inventory objects from uploaded images using a custom-trained YOLOv8 model and provides an inventory summary with confidence scores.
""")
# Load YOLO Model

MODEL_PATH = Path(__file__).resolve().parent.parent/"dataset" / "models" / "best_100epochs.pt"
@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))

model = load_model()
st.success("YOLOv8 Model Loaded Successfully!")
# Upload Image

uploaded_file = st.file_uploader(
    "Upload Warehouse Image",
    type=["jpg","jpeg","png"]
)


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    # Get uploaded image size
    width, height = image.size

# Automatically choose image size
    if max(width, height) <= 1000:
        imgsz = 640
    else:
        imgsz = 1280


# Show image information
    st.info(f"""
            Image Resolution : {width} × {height}
            YOLO Image Size : {imgsz}
            """
            )
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

# Save uploaded image temporarily

    temp_path = Path(__file__).parent / "temp_upload.png"
    image.save(temp_path)

# Run YOLO Prediction

    try:
        with st.spinner("🔍 Detecting warehouse objects..."):
            start_time = time.time()

            results = model.predict(
             source=str(temp_path),
             imgsz=imgsz,
             conf=0.25,
             verbose=False
            )

            end_time = time.time()

    except Exception as e:

        st.error(f"Prediction failed: {e}")
        st.stop()

    result = results[0]
    if temp_path.exists():
        temp_path.unlink()
    processing_time = end_time - start_time
    predicted_image=result.plot()

    # Convert OpenCV image to PIL Image
    predicted_image_rgb = cv2.cvtColor(
        predicted_image,
        cv2.COLOR_BGR2RGB
    )
    prediction_pil = Image.fromarray(
        predicted_image_rgb
    )
    buffer = io.BytesIO()
    prediction_pil.save(
        buffer,
        format="PNG"
    )
    image_bytes = buffer.getvalue()
    st.download_button(
    label="📥 Download Prediction Image",
    data=image_bytes,
    file_name="prediction.png",
    mime="image/png"
    )
    with col2:
        st.subheader("Prediction Result")
        st.image(
            predicted_image_rgb,
            caption="Detected Objects",
            use_container_width=True
        )
    # Number of detected objects
    total_objects = len(result.boxes)
    st.subheader("Detection Summary")

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric(
        "Total Objects Detected",
        total_objects
    )

    with metric2:
        st.metric(
        "Processing Time",
        f"{processing_time*1000:.0f} ms"
    )

    if total_objects > 0:

        object_names = []

        for box in result.boxes:
            class_id = int(box.cls[0])
            object_names.append(model.names[class_id])
        object_counts = Counter(object_names)
        st.subheader("📦 Inventory Summary")

        summary_data = []

        for obj, count in object_counts.items():
            summary_data.append({
                "Object": obj,
                "Quantity": count
            })

        st.dataframe(
         summary_data,
         use_container_width=True,
         hide_index=True
        )
      
    if total_objects > 0:
        st.subheader("Detected Objects")
        detection_data = []
        for i, box in enumerate(result.boxes, start=1):
            class_id = int(box.cls[0])
            box_confidence = float(box.conf[0])
            class_name = model.names[class_id]

            detection_data.append({
                "S.No": str(i),
                "Object": class_name,
                "Confidence": f"{box_confidence:.2f}"
            })

        st.dataframe(
        detection_data,
        use_container_width=True,
        hide_index=True
    )

    else:
        st.warning("No objects detected.")