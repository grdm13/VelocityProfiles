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

dirName = '/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/3_Second_Algorithm_New_Droplet_set/Evaluation CSV/EtOH';
listOfFiles = getListOfFiles(dirName)
listOfFiles.sort()

VelocityProfile = np.zeros( (len(listOfFiles), 1), dtype=object)
Complete_list_of_V = []

for Main_i in range( len(listOfFiles) - 1 ): # i'm doing that because i will use triads
    #print(f"-----------------")
    #print(f"iteration no{Main_i}")
    #print(f"-----------------")
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
        print("Euclidean distance from x to y: ", first_second_distanse, "pixels")

        d = first_second_distanse * 0.0000683111954459203  # meters
        print("Euclidean distance from x to y: ", d, "meters")
        dt = (1 / 3200)  # seconds
        v = d / dt  # m/s
        print("Speed: ",v, "meters/sec")
        print("=================================================================")


'''
#print("--------MAIN--#-1----")
#print("MAIN #1: the Maximum velocities of each frame to frame profile are:")
#print( AVG_VELOCITY(M0, M1)[0])
#print("--------MAIN--#-2----")
#print("MAIN #2: all the measured velocities are:")

temp = np.array(Complete_list_of_V)
#print( temp )
VelocityProfile_1D = []
for i in range(temp.shape[0]):
    for j in range( len(temp[i]) ):
        VelocityProfile_1D.append( temp[i][j] )

print(VelocityProfile_1D)

my_df = pd.DataFrame(VelocityProfile_1D)
my_df.to_csv(f'ONE ARRAY (1D) for EtOH.csv', header=False, index=False)  # save as csv
'''

print("--- %s seconds ---" % (time.time() - start_time))


