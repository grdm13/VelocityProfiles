import numpy as np
import time
import os
from numpy import genfromtxt
import pandas as pd
import statistics
import math
import matplotlib.pyplot as plt

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

dirName = '/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/3_Second_Algorithm_New_Droplet_set/evaluation Tamal - NB (near bottom)/NB - etoh/etoh_csv';
listOfFiles = getListOfFiles(dirName)
listOfFiles.sort()

VelocityProfile = np.zeros( (len(listOfFiles), 1), dtype=object)
Complete_list_of_V = []
total_v = []

for Main_i in range( len(listOfFiles) - 1 ): # i'm doing that because i will use triads
    word = 'Store'
    # print(listOfFiles_TIF[main_i])
    if word in listOfFiles[Main_i]:
        print("There is a .DS_Store file.")
    else:
        M0 = genfromtxt(listOfFiles[Main_i], delimiter=',', encoding='unicode_escape')
        M1 = genfromtxt(listOfFiles[(Main_i) + 1], delimiter=',', encoding='unicode_escape')
        x = [M0[0], M0[1]]
        y = [M1[0], M1[1]]
        y_x_0 = y[0] - x[0]
        y_x_1 = y[1] - x[1]
        first_second_distanse = math.sqrt((y_x_0 ** 2) + (y_x_1 ** 2))

        d = first_second_distanse *  0.0000683111954459203 # meters
        dt = (1 / 2000)  # seconds
        v = d / dt  # m/s
        if v < 1:
            print("Euclidean distance from x to y: ", first_second_distanse, "pixels")
            print("Euclidean distance from x to y: ", d, "meters")
            print("Speed: ", v, "meters/sec")
            print("=================================================================")
            total_v.append(v)
        else: pass
        print(f"the average speed is: " , sum(total_v)/len(total_v) )





print("--- %s seconds ---" % (time.time() - start_time))


