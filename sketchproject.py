import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('sketch')

cv2.createTrackbar('LTC','sketch',0,255,nothing)
cv2.createTrackbar('UTC','sketch',0,255,nothing)


while True:
    ret, frame = cap.read()

    image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image,(7,7),0)
    
    ltc = cv2.getTrackbarPos('LTC','sketch')
    utc = cv2.getTrackbarPos('UTC','sketch')

    image = cv2.Canny(image,ltc,utc)
    ret,image = cv2.threshold(image,50,255,cv2.THRESH_BINARY_INV)

    cv2.imshow("Original", frame)
    cv2.imshow("sketch",image)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyallwindows()