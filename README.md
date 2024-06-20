# Image Component Analysis with YOLOv8 using Streamlit

This project is a Streamlit application that allows users to upload an image and perform object detection using the YOLOv8 model. Upon clicking the "Analyse Image" button, the application detects components in the uploaded image and displays a list of the names of each detected component along with their counts. It also displays an annotated image with bounding boxes around detected components.

## Features

- **Image Upload**: Users can upload images in common formats such as JPEG, PNG, etc.
- **Object Detection**: Uses the YOLOv8 model from Ultralytics to detect various objects in the uploaded image.
- **Results Display**: Shows a list of detected components and their counts.
- **Annotated Image**: Displays the uploaded image with bounding boxes and labels around detected components.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sousannah/Image-Component-Analysis-with-YOLOv8-using-Streamlit.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Navigate into the project directory:

   ```bash
   cd your-repository
   ```

2. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to `localhost:8501` to access the application.

4. Upload an image using the file uploader.
   
5. Click on the "Analyse Image" button to perform object detection.

## Dependencies

- Streamlit
- PIL (Pillow)
- NumPy
- OpenCV (cv2)
- Ultralytics YOLOv8 (automatically installed with Ultralytics library)

## Folder Structure

```
- app.py         # Main Streamlit application script
- requirements.txt  # List of Python dependencies
- README.md      # Project documentation
- Test           #Contains images for testing
- yolov8n.pt     #YOLOv8 Model
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - For the Streamlit framework.
- [Ultralytics](https://github.com/ultralytics/ultralytics) - The YOLOv8 model used for object detection.
