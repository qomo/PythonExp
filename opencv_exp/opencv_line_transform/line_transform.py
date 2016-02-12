import cv2
import numpy as np

img = cv2.imread('road.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 200
maxLineGap = 30
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite("road_gray.jpg", gray)
cv2.imwrite("road_edges.jpg", edges)
cv2.imwrite('road_lines.jpg', img)