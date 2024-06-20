import streamlit as st
from PIL import Image
import numpy as np
import cv2
from ultralytics import YOLO

def main():
    st.title("Image Component Analysis with YOLOv8")

    # Upload image widget
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Analyse Image"):
            analyze_image(image)

def analyze_image(image):
    st.write("Analyzing the image...")

    # Convert PIL image to numpy array
    image_np = np.array(image)

    # Load YOLOv8 model
    model = YOLO('yolov8n.pt')

    # Perform inference
    results = model(image_np)

    # Create a dictionary to keep count of each detected class
    detected_objects = {}

    # Update the dictionary with detected objects
    for result in results[0].boxes:
        class_id = int(result.cls)
        class_name = model.names[class_id]
        if class_name in detected_objects:
            detected_objects[class_name] += 1
        else:
            detected_objects[class_name] = 1

    # Display the results
    st.write("Detected components and their counts:")
    for class_name, count in detected_objects.items():
        st.write(f"{class_name}: {count}")

    # Annotate the image
    annotated_image = results[0].plot()

    # Convert annotated image from BGR to RGB
    annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    annotated_image_pil = Image.fromarray(annotated_image_rgb)

    # Display the annotated image
    st.image(annotated_image_pil, caption='Annotated Image', use_column_width=True)

if __name__ == "__main__":
    main()
