code  ![image](https://github.com/user-attachments/assets/d28dacb5-9378-4df3-ae20-924f9425fab2)
output ![image](https://github.com/user-attachments/assets/d0023ba4-41d3-446b-996f-9111ab07e990)
explanation
import streamlit as st
→ Imports the Streamlit library to build the interactive web app.

import cv2
→ Imports OpenCV, a powerful library for image and video processing.

import numpy as np
→ Imports NumPy, a library for numerical operations (used here to handle images).

Streamlit Title
st.title("Real-Time Webcam Capture with OpenCV")
→ Sets the title of the app as "Real-Time Webcam Capture with OpenCV".

Webcam Control (Checkbox)
run = st.checkbox('Start Webcam')
→ Adds a checkbox to the Streamlit app that allows the user to start or stop the webcam capture.

Set Up Image Display Area
FRAME_WINDOW = st.image([])
→ Initializes an empty image placeholder in the app to display webcam frames.

Video Capture Initialization
camera = cv2.VideoCapture(0)
→ Initializes the webcam using OpenCV. The 0 refers to the default webcam on your system.

Start Webcam Capture (If Checkbox is Checked)
if run:
→ Begins the webcam capture process only if the user checks the "Start Webcam" checkbox.

while True:
→ This loop continuously reads frames from the webcam until it's stopped. Note: This will cause issues with Streamlit, as it doesn't support infinite loops in its normal behavior.

Read Webcam Frame
ret, frame = camera.read()
→ Reads a single frame from the webcam. ret indicates whether the frame was successfully captured, and frame contains the image data.

if not ret:
→ Checks if the frame was not successfully captured.

st.error("Failed to grab frame")
→ Displays an error message in the Streamlit app if the frame capture fails.

break
→ Exits the loop if the frame capture fails.

Convert Image Color Format
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
→ Converts the frame from OpenCV’s default color format (BGR) to the RGB format required by Streamlit for correct color rendering.

Display the Frame
FRAME_WINDOW.image(frame)
→ Displays the converted frame in the FRAME_WINDOW placeholder (a st.image widget).

Stop the Webcam
else:
→ Executes when the "Start Webcam" checkbox is unchecked.

st.write("Webcam stopped.")
→ Displays a message indicating that the webcam has been stopped.

Release the Camera
camera.release()
→ Releases the webcam resource once the app stops, ensuring that the camera is no longer in use.


