import streamlit as st
import cv2
import cvzone
import math
from ultralytics import YOLO
import base64

# Load the model
confidence = 0.6
model = YOLO("best.pt")
classNames = ["fake", "real"]

# Initialize variables
run_detection = False
cap = None

def run_attendance():
    global run_detection, cap

    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Real-time object detection
    stframe = st.empty()
    while run_detection:
        success, img = cap.read()
        if not success:
            break
        else:
            # Flip the image horizontally to avoid mirrored effect
            img = cv2.flip(img, 1)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            results = model(img, stream=True, verbose=False)

            # Draw bounding boxes and labels
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    w, h = x2 - x1, y2 - y1
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    cls = int(box.cls[0])
                    if conf > confidence:
                        if classNames[cls] == 'real':
                            color = (0, 255, 0)
                        else:
                            color = (0, 0, 255)
                        cvzone.cornerRect(img, (x1, y1, w, h), colorC=color, colorR=color)
                        cvzone.putTextRect(img, f'{classNames[cls].upper()} {int(conf*100)}%',
                                           (max(0, x1), max(35, y1)), scale=2, thickness=4, colorR=color,
                                           colorB=color)

            # Draw a beautiful boundary around the webcam feed
            border_color = (0, 255, 255)  # Yellow color
            border_thickness = 20
            img = cv2.copyMakeBorder(img, border_thickness, border_thickness, border_thickness, border_thickness,
                                     cv2.BORDER_CONSTANT, value=border_color)

            # Display the output image
            stframe.image(img, channels="RGB", use_column_width=True)

    if cap:
        cap.release()

def run():
    st.set_page_config(page_title="Real vs Fake Face Detection", page_icon=":camera:")

    # Add a background image
    main_bg = "C:/Users/ha/AppData/Local/Programs/Python311/Antispoofing/background.jpg"
    main_bg_ext = "jpeg"

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/{main_bg_ext};base64,{get_base64(main_bg)}");
            background-size: cover;
        }}
        .main-container {{
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: flex-start;
            margin-left: 0;
            padding-left: 0;
        }}
        .main-header {{
            text-align: left;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='main-header'>Real vs Fake Face Detection</h1>", unsafe_allow_html=True)

    # Attendance section
    st.markdown("<h2 class='main-header'>Attendance</h2>", unsafe_allow_html=True)
    start_button = st.button("Start Attendance")
    stop_button = st.button("Stop Attendance")

    global run_detection
    if start_button:
        run_detection = True
        run_attendance()
    if stop_button:
        run_detection = False

# Function to read image data as base64
@st.cache_data()
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

if __name__ == "__main__":
    run()