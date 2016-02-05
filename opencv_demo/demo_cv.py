import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.jpeg', 0)
# print type(img)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()