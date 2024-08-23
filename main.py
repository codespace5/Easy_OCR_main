import pytesseract
import cv2

# Path to the Tesseract executable (update with your own path if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image using OpenCV
image_path = '2.JPG'  # Replace with the path to your image file

img = cv2.imread(image_path)
cv2.imshow('img', img[250:320, 150:400])
cv2.waitKey(0)
# Convert the image to grayscale for better OCR results (optional but recommended)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

oct_image = gray_img[250:320, 150:400]
# Use Tesseract to extract text from the image
# By specifying 'output_type=pytesseract.Output.DICT', you can get structured results
result = pytesseract.image_to_string(oct_image)

# Extract numbers from the recognized text
# extracted_numbers = result['text']
print(result)

# Print the extracted numbers
# print("Extracted Numbers:", extracted_numbers)