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
import seaborn as sns


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

dirName_CSV = "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/tamal_Dense_Flow_CSV_velocities"
listOfFiles_CSV = getListOfFiles(dirName_CSV)
dirName_PNG = "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/tamal_Dense_Flow_Snipets_to_male_Velocities"
listOfFiles_PNG = getListOfFiles(dirName_PNG)

for i in range(len(listOfFiles_CSV)):
    img = cv2.imread(listOfFiles_PNG[i])
    df = pd.read_csv((listOfFiles_CSV[i]))

    fig = plt.figure()
    plt.subplot(3, 1, 1)
    ax1 = sns.heatmap(df)
    plt.subplot(3, 1, 2)
    ax2 = sns.distplot(df)
    plt.subplot(3, 1, 3)
    ax3 = plt.imshow(img)
    fig.savefig(f'full_figure_Tamal_{i+1} .png')
    plt.tight_layout()
    #plt.show()