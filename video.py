import easyocr
import numpy as np
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

reader = easyocr.Reader(['en'])

vid = cv2.VideoCapture('stuff.mp4')

# Initialize variables to keep track of changes in text
prev_text = None
current_text = None
text_change_detected = False

# Initialize a counter for the video clips
clip_counter = 0

while True:
    ret, img = vid.read()
    if not ret:
        break

    img = cv2.resize(img, (800, 600))
    img_ocr = img[450:580, :]
    img_gray = cv2.cvtColor(img_ocr, cv2.COLOR_BGR2GRAY)

    res = reader.readtext(image=img_gray, text_threshold=0.3)

    if res:
        current_text = res[0][1]

        print("test___", current_text)

        if current_text != prev_text:
            text_change_detected = True
        else:
            text_change_detected = False

        if text_change_detected:
            if clip_counter > 0:
                out.release()  # Release the previous video writer

            # Define a new filename based on the detected text
            filename = f"{clip_counter}_{current_text}.mp4"

            # Initialize the video writer for the new clip
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(filename, fourcc, 20.0, (800, 600))

            clip_counter += 1

        # Write the frame to the current clip
        out.write(img)

        # Update the previous text
        prev_text = current_text

    cv2.imshow('result', img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press Esc key to exit
        break

# Release the video writer for the last clip
if clip_counter > 0:
    out.release()

vid.release()
cv2.destroyAllWindows()