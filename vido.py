import easyocr
import numpy as np
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

reader = easyocr.Reader(['en'])

vid = cv2.VideoCapture('stuff.mp4')

while(1):
    _, img  = vid.read()
    img = cv2.resize(img, (800, 600))
    img_ocr = img[450:580, :]
    cv2.imshow('test', img_ocr)
    # cv2.waitKey(1)
    cv2.imshow("123",img_ocr)
    # img_ocr = cv2.medianBlur(img_ocr,7)
    # b, g, r = cv2.split(img_ocr)
    img_gray = cv2.cvtColor(img_ocr, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image", img_ocr)

    res = reader.readtext(image=img_gray, text_threshold=0.3)
    print("121111",res)
    text1 = res[0][1]
    print(text1)

    # print('___________________________')
    cv2.putText(img, text1, (200, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)
    cv2.imshow('result', img)
    # print(res)
    cv2.waitKey(1)


# img = cv2.imread('ocr2.jpg')
# # img = cv2.resize(img, (800, 600))
# # img_ocr = img[500:600, 100:700]
# cv2.imshow("123",img)
# b, g, r = cv2.split(img)
# cv2.imshow("image", r)

# res = reader.readtext(image=r, allowlist="$0123456789")
# # print(res[0][1])
# text1 = res[0][1]
# print('$'+ text1[1:-2] + '.' + text1[-2:])
# text2 = res[1][1]
# print('$'+ text2[1:-2] + '.' + text2[-2:])
# text3 = res[2][1]
# print('$'+ text3[1:-2] + '.' + text3[-2:])