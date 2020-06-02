import time
import pandas as pd
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

################## start the timer #######################
start_time = time.time()

################## read the image #######################
# Read image
img = cv2.imread('/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/working_directory/image_145.jpg', cv2.IMREAD_GRAYSCALE);
crop_img = img[250:450, 100:500]

# Threshold, Set values equal to or above 220 to 0, Set values below 220 to 255.
th, im_th = cv2.threshold(crop_img, 65, 255, cv2.THRESH_BINARY_INV);

def CC(img):
        nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
        label_hue = np.uint8(179 * labels / np.max(labels))
        blank_ch = 255 * np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
        labeled_img[label_hue == 0] = 0
        return labeled_img, nlabels, labels, stats, centroids

kernel = np.ones((3, 5), np.uint8)
erosion = cv2.erode(im_th, kernel, iterations=2)
dilation = cv2.dilate(erosion, kernel, iterations=2)
components, nlabels, labels, stats, centroids = CC(dilation)

# creating the matrices
CC_Stats = np.hsplit(stats, 5)
horizontal = CC_Stats[2]
vertical = CC_Stats[3]
area = CC_Stats[4]

CC_Centroids = np.hsplit(centroids, 2)
x_centr = CC_Centroids[0]
y_centr = CC_Centroids[1]

# Logic check if something is DROPLET or NOT
d = 0
droplet_counter = 0
Not_Droplet = np.empty(nlabels, dtype=object)
for i in range(nlabels):
    if area[i] > 2000 and area[i] < 500  :
        Not_Droplet[i] = "NOT a droplet"
    else:
        Not_Droplet[i] = "ok"
        droplet_counter = droplet_counter + 1

# here we draw the circles, the boxes and the numbers
image = components
out = image.copy()
kk = 0
for row in range(1, nlabels, 1):
    for column in range(5):
        if Not_Droplet[row] == "ok":
            cv2.putText(out, ('%d' % (row)), (x_centr[row], y_centr[row]), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (255, 255, 255), 2)


cv2.putText(out, ('%d droplets' % droplet_counter), (5, 30), cv2.FONT_ITALIC, 1.0, (220, 220, 220), 2)

# show the images
cv2.imshow("Initial", crop_img)
cv2.imshow("Final", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

