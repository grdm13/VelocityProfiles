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

dirName = '/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/3_Second_Algorithm_New_Droplet_set/csv_PRO_editing';
listOfFiles = getListOfFiles(dirName)
listOfFiles.sort()
L = (len(listOfFiles) - 1)
max=0.0
container = np.empty(((L+1),1), dtype=object)
'''
#i did that to delete the empty csv files 
for i in range(L+1):
    df = pd.read_csv(listOfFiles[i], delimiter=',', encoding='unicode_escape')
    if df.empty == True:
        print(f'{listOfFiles[i]} is empty')
'''


for i in range(len(listOfFiles)-1):
    M = genfromtxt(listOfFiles[i], delimiter=',', encoding= 'unicode_escape')
    #print(M)
    #print(M.shape[0])
    #print(f" ", i, " / ", (len(listOfFiles)))
    container[i] = M.shape[0]

for i in range(len(container)):
    if container[i].any():
        pass
    else:
        container[i] = 0

#print(container)
max = np.max(container)
#print(max)
dummy = np.array(([0, 0, 0, 0, 0, 0]), float)

for i in range(L+1):
    M = genfromtxt(listOfFiles[i], delimiter=',', encoding= 'unicode_escape')
    while M.shape[0] < max:
        M = np.vstack((M, dummy))
        my_df = pd.DataFrame(M)
        my_df.to_csv(f'Edited matrix from {i}.csv', header=False, index=False)  # save as csv

# issues with tuple

print("--- %s seconds ---" % (time.time() - start_time))



