import numpy as np
import time
import os
from numpy import genfromtxt
import pandas as pd
import statistics
import math
import matplotlib.pyplot as plt

start_time = time.time()

def AVG_VELOCITY(array1, array2, array3):
    # the following function checks for X and Y matching dimension
    # at the first two frames
    def MATCHED(array1, array2):
        matching_HOR_VER = []
        Centroids_match = []
        for row in range(array1.shape[0]):
            if (array1[row][3] == array2[row][3] - 1) or (array1[row][3] == array2[row][3] + 1) or (
                    array1[row][3] == array2[row][3]):
                if (array1[row][2] == array2[row][2] - 1) or (array1[row][2] == array2[row][2] + 1) or (
                        array1[row][2] == array2[row][2]):
                    # print(from_56[row][2], from_56[row][3])
                    matching_HOR_VER.append((array1[row][2], array1[row][3]))
                    Centroids_match.append((array1[row][0], array1[row][1], array2[row][0], array2[row][1]))
                else:
                    pass
            else:
                pass
        return Centroids_match

    def STRIP(list):
        a = (list[3] - list[1]) / (list[2] - list[0])
        b = list[1] - (a * list[0])
        matrix = np.zeros((1000, 3), float)
        for x in range(1000):
            y1 = a * x + b
            y2 = y1 + b
            y3 = y1 - b
            matrix[x][0] = y1
            matrix[x][1] = y2
            matrix[x][2] = y3
        # plt.figure()
        # plt.plot(matrix)
        # plt.plot(list[0], list[1], color='green', marker='o')
        # plt.plot(list[2], list[3], color='red', marker='o')
        # plt.xlim(xmin=0, xmax=413)
        # plt.ylim(ymin=0, ymax = 487)
        # ax = plt.gca()  # get the axis
        # ax.set_ylim(ax.get_ylim()[::-1])  # invert the axis
        # ax.xaxis.tick_top()  # and move the X-Axis
        # plt.show()
        return a, b

    def Third_point(list1_2, array1, array2, array3):
        Last_X = list1_2[2]
        Last_Y = list1_2[3]
        New_Y = []
        New_X = []
        for row in range(array3.shape[0]):
            if (Last_X > array3[row][0]) and (Last_Y > array3[row][1]):
                New_X.append(array3[row][0])
                New_Y.append(array3[row][1])
            else:
                pass
        # now we know the smaller X n Y
        # and now we will have to find the inside the strip
        AA = (STRIP(MATCHED(array1, array2)[0]))[0]
        BB = (STRIP(MATCHED(array1, array2)[0]))[1]
        Final_Y = []
        Final_X = []
        for row in range(len(New_Y)):
            if (New_Y[row] < AA * (New_X[row]) + (2 * BB)) and (New_Y[row] > AA * (New_X[row])):
                Final_X.append(New_X[row])
                Final_Y.append(New_Y[row])
            else:
                pass

        return Final_X, Final_Y


    first_second_position = MATCHED(array1, array2)[0]
    third_position = Third_point((MATCHED(array1, array2)[0]), array1, array2, array3)

    def DISTANCES(list1, list2):
        x = [list1[0], list1[1]]
        y = [list1[2], list1[3]]
        z = list2
        # print(x)
        # print(y)
        # print(z)
        first_second_distanse = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
        second_third_distanse = math.sqrt(sum([(a - b) ** 2 for a, b in zip(y, z)]))
        first_third_distanse = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, z)]))
        # print("Euclidean distance from x to y: ", first_second_distanse)
        # print("Euclidean distance from x to y: ", second_third_distanse)
        # print("Euclidean distance from x to y: ", first_third_distanse)
        return first_second_distanse, second_third_distanse, first_third_distanse

    # distances
    d1 = DISTANCES(first_second_position, third_position)[0] * 6.75531915 / 1000000
    d2 = DISTANCES(first_second_position, third_position)[1] * 6.75531915 / 1000000
    d3 = DISTANCES(first_second_position, third_position)[2] * 6.75531915 / 1000000
    # time scale
    dt = (1 / 3200)  # secondds
    double_dt = (2 / 3200)  # seconds
    # velocities
    v1 = d1 / dt  # m/s
    v2 = d2 / dt  # m/s
    v3 = d3 / double_dt  # m/s

    print("the average velocity of the droplet is:", round(statistics.mean([v1, v2, v3]), 2), "m/s")


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
dirName = '/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/tamalCSV';
listOfFiles = getListOfFiles(dirName)
listOfFiles.sort()


for i in range( (len(listOfFiles)) - 2 ): # i'm doing that because i will use triads
    M0 = genfromtxt(listOfFiles[i], delimiter=',', encoding= 'unicode_escape')
    M1 = genfromtxt(listOfFiles[i+1], delimiter=',', encoding= 'unicode_escape')
    M2 = genfromtxt(listOfFiles[i+2], delimiter=',', encoding= 'unicode_escape')
    AVG_VELOCITY(M0, M1, M2)

print("--- %s seconds ---" % (time.time() - start_time))