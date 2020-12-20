import cv2 as cv
import sys

path_to_image = '~/Desktop/ef6d9a11-2c73-43cb-a704-494526e1c250.jpg'
img = cv.imread(path_to_image)
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
