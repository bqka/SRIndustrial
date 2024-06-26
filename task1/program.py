import cv2 as cv
import numpy as np

#Importing color data file which has BGR values of the respective color bounds in correct order

file = open('colordata.txt', 'r')
data = file.read()

data = data.split()
data = [eval(i) for i in data]
data = np.reshape(data, (8, 2, 3))

# color order = ["orange", "violet", "blue", "brown", "red", "black", "green", "orange"]
#Now data contains an array with the values of orange colour bounds on 0 index.
        
#Image Processing        
img = cv.imread('wire.png')

#Detecting edges
imgGRAY = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgGRAY = cv.GaussianBlur(imgGRAY, (5, 5), 0)
edges= cv.Canny(imgGRAY, 50, 200)

indices = np.where(edges == [255])

coordinates = zip(indices[0], indices[1])
listing = list(coordinates)
mylist = list(dict.fromkeys(listing))
mylist = mylist[1:]

i = 0
j = 0


#Drawing contours
contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
image_copy = img.copy()

contours = contours[2:18]

cv.drawContours(image_copy, contours, -1, (0, 255, 0), 2)

no_of_edges = len(contours)

colorBounds = np.array([], dtype=np.uint8)

while i < no_of_edges:

    print("Wire " + str(j+1), end=" ")

    #Locating center point of the wire
    middle = int((mylist[i][0]) + (mylist[i + 1][1] - mylist[i][1]) / 2)

    middle_point = (20, mylist[i][1] + middle)
    cv.circle(edges, (middle_point[1], middle_point[0]), 3, (251, 3, 213), 2)

    x = middle_point[0]

    y = middle_point[1]

    #Checking if the pixel falls in the given colour range
    bgrcolor = img[x, y]
    
    if not (((data[j][0] <= bgrcolor) & (bgrcolor <= data[j][1])).all()):
        print("Not in correct order")
        break
    else:
        print("Correct")

    i += 2
    j += 1

cv.imshow("Source", edges)
cv.imshow("2", image_copy)

cv.waitKey(0)
file.close()