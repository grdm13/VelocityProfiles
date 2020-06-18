import numpy as np
import time
import os
from numpy import genfromtxt
import pandas as pd


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

dirName = '/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/tamalCSV_beforeEdit';
listOfFiles = getListOfFiles(dirName)
listOfFiles.sort()
L = (len(listOfFiles) - 1)
max=0

container = np.empty(((L+1),1), dtype=object)
for i in range(L+1):
    M = genfromtxt(listOfFiles[i], delimiter=',', encoding= 'unicode_escape')
    container[i] =M.shape[0]

max = np.max(container)
dummy = np.array(([0,0,0,0,0,0]), float)

for i in range(L+1):
    M = genfromtxt(listOfFiles[i], delimiter=',', encoding= 'unicode_escape')
    while M.shape[0] < max:
        M = np.vstack((M, dummy))
        my_df = pd.DataFrame(M)
        my_df.to_csv(f'Edited matrix from {i}.csv', header=False, index=False)  # save as csv

print("--- %s seconds ---" % (time.time() - start_time))