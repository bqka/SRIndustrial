import cv2 as cv
import numpy as np

img = cv.imread('wire3.png')

imgGRAY = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgGRAY = cv.GaussianBlur(imgGRAY, (5, 5), 0)
edges= cv.Canny(imgGRAY, 50, 200)

indices = np.where(edges == [255])

coordinates = zip(indices[0], indices[1])
listing = list(coordinates)
mylist = list(dict.fromkeys(listing))
mylist = mylist[1:]

i = 0
j = 1

x = 100

contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
image_copy = img.copy()

contours = contours[2:18]


cv.drawContours(image_copy, contours, -1, (0, 255, 0), 2)
print(len(contours), "objects were found in this image.")

number_of_egdes = len(contours)

while i < number_of_egdes:

    print("Wire " + str(j))

    middle = int((mylist[i][0]) + (mylist[i + 1][1] - mylist[i][1]) / 2)

    middle_point = (20, mylist[i][1] + middle)
    cv.circle(edges, (middle_point[1], middle_point[0]), 3, (251, 3, 213), 2)

    x = middle_point[0]

    y = middle_point[1]

    bgrcolor = img[x, y]

    print("BGR color : " + str(bgrcolor))

    i += 2
    j += 1

cv.imshow("Source", edges)
cv.imshow("2", image_copy)
# cv.imshow('', res)

cv.waitKey(0)