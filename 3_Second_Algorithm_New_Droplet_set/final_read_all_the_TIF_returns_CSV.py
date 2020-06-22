'''

'''

'''
ss
'''

import cv2
import numpy as np
import pandas as pd
import time
import os

start_time = time.time()

image_counter=0
def components_n_Canny(im_in):
    th, im_th = cv2.threshold(im_in, 70, 255, cv2.THRESH_BINARY_INV);
    # print(listOfFiles_TIF[i])
    edges = cv2.Canny(im_th, 100, 100, apertureSize=3)
    # result = np.hstack((img, edges))

    def CC(img):
        nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
        label_hue = np.uint8(179 * labels / np.max(labels))
        blank_ch = 255 * np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
        labeled_img[label_hue == 0] = 0
        return labeled_img, nlabels, labels, stats, centroids


    kernel = np.ones((2, 2), np.uint8)
    erosion = cv2.erode(im_th, kernel, iterations=4)
    dilation = cv2.dilate(erosion, kernel, iterations=2)
    components, nlabels, labels, stats, centroids = CC(dilation)

    # print(stats)

    final_stats = []
    f_stat_counter = 0
    for row in range(stats.shape[0]):
        if (stats[row][0] == 0) or (stats[row][2] < 10) or (stats[row][2] > 50):
            pass
        else:
            final_stats.append(stats[row])
            f_stat_counter = f_stat_counter + 1

    # print(final_stats)
    final_stats_array = np.array(final_stats, dtype=object)
    #print(f"the artifacts for the {main_i} frame are:", nlabels, " but the droplets are:", f_stat_counter)
    #print(f"the stats for {main_i} frame are (X, Y, horizontal, vertical, area) are:")
    #print(final_stats_array)

    Perimeter = []  # in pixels
    Area = []  # in pixels

    for row in range(len(final_stats)):
        crop_img = im_th[
                   (final_stats[row][1] - 5):(final_stats[row][1] + final_stats[row][3]),
                   (final_stats[row][0] - 5):(final_stats[row][0] + final_stats[row][2])
                   ]
        crop_img_edges = edges[
                         (final_stats[row][1] - 5):(final_stats[row][1] + final_stats[row][3]),
                         (final_stats[row][0] - 5):(final_stats[row][0] + final_stats[row][2])
                         ]
        #print(crop_img)
        if crop_img.any():
            l1 = len(crop_img)
            l2 = len(crop_img[1])
        else:
            break

        white_pixels = 0
        white_pixels_edges = 0
        for i in range(l1):
            for j in range(l2):
                if crop_img[i][j] == 255:
                    white_pixels += 1
                if crop_img_edges[i][j] == 255:
                    white_pixels_edges += 1

        Perimeter.append(white_pixels_edges)
        Area.append(white_pixels)

    Area_array = np.array(Area)
    Perimeter_array = np.array(Perimeter)
    Final_stats_array = np.array(final_stats)


    print(Perimeter_array)
    #print(Final_stats_array)
        #print("---------")

    if Perimeter_array.any():
        pass
    else:
        Perimeter_array=[0]

    final_matrix = np.empty((Final_stats_array.shape[0], 6), np.uint8)
    #print(Final_stats_array.shape[0])

    for row in range(Final_stats_array.shape[0]):
        final_matrix[row][0] = Final_stats_array[row][0]
        final_matrix[row][1] = Final_stats_array[row][1]
        final_matrix[row][2] = Final_stats_array[row][2]
        final_matrix[row][3] = Final_stats_array[row][3]
        final_matrix[row][4] = Perimeter_array[row]
        final_matrix[row][5] = Area_array[row]

    # print(final_matrix)
    my_df = pd.DataFrame(final_matrix)
    # image_counter = image_counter + 1
    my_df.to_csv(f' TIF_to_CSV_from_ {main_i}_frame.csv', header=False, index=False)  # save as csv

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

dirName_TIF = "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/3_Second_Algorithm_New_Droplet_set/reduced from 140 to 82 TIF files"
listOfFiles_TIF = getListOfFiles(dirName_TIF)
listOfFiles_TIF.sort()

for main_i in range(len(listOfFiles_TIF)):
    image_counter = image_counter + 1
    im_in = cv2.imread(listOfFiles_TIF[main_i], cv2.IMREAD_GRAYSCALE);
    components_n_Canny(im_in)


print("--- %s seconds ---" % (time.time() - start_time))

