import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import time
import os
from os import listdir
from os.path import isfile, join
from numpy.core._multiarray_umath import ndarray


start_time = time.time()

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

dirName = "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/binary_by_tamal"
listOfFiles = getListOfFiles(dirName)

for i in range(len(listOfFiles)):
    img = cv2.imread(listOfFiles[i], 0)

    def CC(img):
        nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
        label_hue = np.uint8(179 * labels / np.max(labels))
        blank_ch = 255 * np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
        labeled_img[label_hue == 0] = 0
        return labeled_img, nlabels, labels, stats, centroids

    kernel = np.ones((2, 2), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=3)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
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

    for row in range(nlabels):
        if (horizontal[row] > 400) or (area[row] < 90):
            Not_Droplet[row] = "NOT a droplet"
        else:
            Not_Droplet[row] = "ok"
            droplet_counter = droplet_counter + 1

    # here we draw the circles, the boxes and the numbers
    image = components
    out = image.copy()

    for row in range(nlabels):
        if Not_Droplet[row] == "ok":
            cv2.putText(out, ('%d' % (row)), (x_centr[row], y_centr[row]), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255, 255, 255), 2)
        else:
            x_centr[row] = -1
            y_centr[row] = -1
            horizontal[row] = -1
            vertical[row] = -1
            area[row] = -1

    cv2.putText(out, ('%d droplets' % (droplet_counter)), (5, 30), cv2.FONT_ITALIC, 1.0, (220, 220, 220), 2)

    final_matrix = np.empty((nlabels, 5), np.uint8)
    for row in range(nlabels):
        final_matrix[row][0] = x_centr[row]
        final_matrix[row][1] = y_centr[row]
        final_matrix[row][2] = horizontal[row]
        final_matrix[row][3] = vertical[row]
        final_matrix[row][4] = area[row]
    final_matrix = final_matrix[final_matrix[:, 2] != 255]

    #print(final_matrix)

    # show the images
    #cv2.imshow("Initial", img)
    #cv2.imshow("Final", out)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    my_df = pd.DataFrame(final_matrix)
    my_df.to_csv(f'matrix from {i+39} TAMAL frame.csv', header=False, index=False)  # save as csv

print("--- %s seconds ---" % (time.time() - start_time))