import numpy as np
import time
import os
from numpy import genfromtxt
import pandas as pd
import statistics
import math
import matplotlib.pyplot as plt

start_time = time.time()

def AVG_VELOCITY(array1, array2):
    def MATCHED(array1, array2):
        matching_HOR_VER_PER_AREA = []
        Centroids_match = []
        for row in range(array1.shape[0]):
            if array1[row][0] == 0:
                pass
            else:
                if ((array1[row][2] > array2[row][2] - 5) and (array1[row][2] < array2[row][2] + 5)):
                    if ((array1[row][3] > array2[row][3] - 5) and (array1[row][3] < array2[row][3] + 5)):
                        if ((array1[row][4] > array2[row][4] - 10) and (array1[row][4] < array2[row][4] + 10)):
                            if ((array1[row][5] > array2[row][5] - 35) and (array1[row][5] < array2[row][5] + 35)):
                                matching_HOR_VER_PER_AREA.append((array1[row][2], array1[row][3]))
                                Centroids_match.append((array1[row][0], array1[row][1], array2[row][0], array2[row][1]))
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        return Centroids_match

    MATCHED(array1, array2)
    matched_array = np.array(MATCHED(array1, array2))
    #print(matched_array)
    VelocityProfile_per_row = []

    for i in range(matched_array.shape[0]):
        first_second_position = MATCHED(array1, array2)[i]
        print(first_second_position)
        def DISTANCES(list):
            x = [list[0], list[1]]
            y = [list[2], list[3]]
            y_x_0 = y[0] - x[0]
            y_x_1 = y[1] - x[1]
            first_second_distanse = math.sqrt((y_x_0 ** 2) + (y_x_1 ** 2))
            print("Euclidean distance from x to y: ", first_second_distanse)
            return first_second_distanse

        d = DISTANCES(   first_second_position   ) * 6.75531915 / 1000000  # meters
        dt = (1 / 3200)  # secondds
        v = d / dt  # m/s
        # print(v1)

        print(f"the average velocity of the {Main_i} droplet is:", round(v, 3),
                  "m/s")
        VelocityProfile_per_row.append(round(v, 3))
       # VelocityProfile[Main_i] = VelocityProfile_per_row


    #return VelocityProfile



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

dirName = '/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/3_Second_Algorithm_New_Droplet_set/csv_AFTER_editing';
listOfFiles = getListOfFiles(dirName)
listOfFiles.sort()

VelocityProfile = np.zeros( (len(listOfFiles), 1), dtype=object)

for Main_i in range( len(listOfFiles) - 1 ): # i'm doing that because i will use triads
    print(f"-----------------")
    print(f"iteration no{Main_i}")
    print(f"-----------------")
    M0 = genfromtxt(listOfFiles[Main_i], delimiter=',', encoding= 'unicode_escape')
    M1 = genfromtxt(listOfFiles[(Main_i)+1], delimiter=',', encoding= 'unicode_escape')
    print( AVG_VELOCITY(M0, M1) )

#print("MAIN : the final velocity profile is:")
#print( AVG_VELOCITY(M0, M1))

print("--- %s seconds ---" % (time.time() - start_time))


