import numpy as np
import statistics
import math
import matplotlib.pyplot as plt

from_55 = np.array(
    ([99, 70, 13, 17, 127],
    [233, 165, 12, 14, 119],
    [212, 165, 1, 1, 119]), float)

from_56 = np.array(
    ([56, 47, 13, 17, 140],
     [123, 219, 16, 16, 185],
     [243, 365, 1, 1, 119]), float)

from_57 = np.array(
    ([10, 24, 20, 16, 176],         #<----- it must find this guy here
    [ 55, 0, 33, 19, 52],
    [129, 35, 25, 13, 142],
    [119, 109, 16, 15, 150]), float)

#the following function checks for X and Y matching dimension
# at the first two frames
def MATCHED(array1, array2):
    matching_HOR_VER = []
    Centroids_match = []
    for row in range(array1.shape[0]):
        if (array1[row][3] == array2[row][3] - 1) or (array1[row][3] == array2[row][3] + 1) or (
                array1[row][3] == array2[row][3]):
            if (array1[row][2] == array2[row][2] - 1) or (array1[row][2] == array2[row][2] + 1) or (
                    array1[row][2] == array2[row][2]):
                #print(from_56[row][2], from_56[row][3])
                matching_HOR_VER.append((array1[row][2], array1[row][3]))
                Centroids_match.append((array1[row][0], array1[row][1],array2[row][0], array2[row][1]))
            else:pass
        else:pass
    return Centroids_match

# the following function creates a strip
# in which strip we will search for the
# next the third point
# returns the a and b from the line equation
def STRIP(list):
    a = (list[3] - list[1]) / (list[2] - list[0])
    b = list[1] - (a * list[0])
    matrix = np.zeros((1000,3), float)
    for x in range(1000):
        y1 = a*x + b
        y2 = y1 + b
        y3 = y1 - b
        matrix[x][0] = y1
        matrix[x][1] = y2
        matrix[x][2] = y3

    #plt.figure()
    #plt.plot(matrix)
    #plt.plot(list[0], list[1], color='green', marker='o')
    #plt.plot(list[2], list[3], color='red', marker='o')
    ##plt.plot(10, 24, color='yellow', marker='o') #this is only for this test
    #plt.xlim(xmin=0, xmax=413)
    #plt.ylim(ymin=0, ymax = 487)
    #ax = plt.gca()  # get the axis
    #ax.set_ylim(ax.get_ylim()[::-1])  # invert the axis
    #ax.xaxis.tick_top()  # and move the X-Axis
    #plt.show()
    return a, b

#STRIP(MATCHED(from_55, from_56)[0])
#print(STRIP(MATCHED(from_55, from_56)[0]))

# he have already build the strip
# now we will search on the strip coordinates for something with smaller x
# and y values of the second point inside the strip

def Third_point(list1_2, array_3, array_2, array_1):
    #initially we will weed out the larger X and Y from the
    # second point
    Last_X = list1_2[2]
    Last_Y = list1_2[3]
    New_Y = []
    New_X = []

    for row in range(array_3.shape[0]):
        if (Last_X > array_3[row][0]) and (Last_Y > array_3[row][1]):
            New_X.append(array_3[row][0])
            New_Y.append(array_3[row][1])
        else:
            pass
    # now we know the smaller X n Y
    # and now we will have to find the inside the strip
    AA = (STRIP(MATCHED(array_1, array_2)[0]))[0]
    BB = (STRIP(MATCHED(array_1, array_2)[0]))[1]
    Final_Y = []
    Final_X = []
    for row in range(len(New_Y)):
        if ( New_Y[row] < AA * (New_X[row]) + (2* BB)) and ( New_Y[row] > AA * (New_X[row]) ):
            Final_X.append(New_X[row])
            Final_Y.append(New_Y[row])
        else:
            pass

    return Final_X, Final_Y


#print(Third_point((MATCHED(from_55, from_56)[0]), from_57, from_56, from_55))

first_second_position = MATCHED(from_55, from_56)[0]
third_position = Third_point((MATCHED(from_55, from_56)[0]), from_57, from_56, from_55)

#print(first_second_position)
#print(third_position)

def DISTANCES(list1, list2):
    x = [ list1[0], list1[1] ]
    y = [ list1[2], list1[3] ]
    z = list2
   # print(x)
   # print(y)
   # print(z)
    first_second_distanse = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    second_third_distanse = math.sqrt(sum([(a - b) ** 2 for a, b in zip(y,z)]))
    first_third_distanse = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, z)]))
    #print("Euclidean distance from x to y: ", first_second_distanse)
    #print("Euclidean distance from x to y: ", second_third_distanse)
    #print("Euclidean distance from x to y: ", first_third_distanse)
    return first_second_distanse, second_third_distanse, first_third_distanse

#print( DISTANCES(first_second_position, third_position) )

d1 = DISTANCES(first_second_position, third_position)[0] * 1.4803 / 10000000
d2 = DISTANCES(first_second_position, third_position)[1] * 1.4803 / 10000000
d3 = DISTANCES(first_second_position, third_position)[2] * 1.4803 / 10000000

# velocities
dt = (1 / 3200)  # secondds
double_dt = (2 / 3200)  # seconds

v1 = d1 / dt # m/s
v2 = d2 / dt # m/s
v3 = d3 / double_dt # m/s

print("the average velocity of the droplet is:" , round(statistics.mean( [v1, v2, v3] ), 2), "m/s" )




