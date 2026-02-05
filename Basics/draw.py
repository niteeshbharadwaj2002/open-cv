import cv2 as cv
import numpy as np

# img = cv.imread("Photos/cat.jpg")
# cv.imshow("Cat",img) 
blank = np.zeros((500,500,3), dtype="uint8")

#DRAW A RECTANGLE
cv.rectangle(blank, (0,0), (250,250), (0,255,255), thickness=2)

#DRAW A CIRCLE
cv.circle(blank, (250,250), 40, (0,255,0), thickness=3)

#DRAW A LINE
cv.line(blank, (0,0), (250,250), (255,0,0), thickness=3)

#WRITE A TEXT
cv.putText(blank, "Hello", (225,225), cv.FONT_HERSHEY_DUPLEX, 1.0, (0,0,255), thickness=2)

cv.imshow("Circle",blank)


cv.waitKey(0)