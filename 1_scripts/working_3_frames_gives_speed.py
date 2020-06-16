import numpy as np
import statistics
import math
import matplotlib.pyplot as plt

from_62 = np.array(
    (
        [143, 116, 14, 17, 125],
        [50, 135, 12, 12, 104],
        [66, 156, 15, 17, 130],
        [251, 209, 20, 21, 24],
        [85, 21, 13, 15, 97],
        [78, 95, 22, 24, 121],
        [213, 98, 11, 16, 101],
    ), float)

from_63 = np.array(
    (
        [102, 99, 15, 17, 127],
        [13, 125, 16, 27, 253],
        [207, 188, 22, 21, 255],
        [41, 195, 12, 14, 92],
        [18, 18, 12, 15, 110],
        [164, 92, 11, 14, 101],
        [36, 99, 24, 23, 68],
        [151, 131, 13, 16, 155],
    ), float)

from_64 = np.array(
    (
        [60, 82, 14, 17, 129],
        [220, 94, 30, 29, 46],
        [161, 169, 21, 21, 56],
        [142, 169, 20, 24, 120],
        [249, 176, 11, 16, 97],
        [110, 89, 14, 15, 125],
        [250, 101, 21, 24, 45],
        [99, 133, 12, 17, 106],
        [149, 137, 14, 17, 135],
        [121, 206, 16, 16, 133],
    ), float)


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

    # the following function creates a strip
    # in which strip we will search for the
    # next the third point
    # returns the a and b from the line equation
    # for i in len()
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
        ##plt.plot(10, 24, color='yellow', marker='o') #this is only for this test
        # plt.xlim(xmin=0, xmax=413)
        # plt.ylim(ymin=0, ymax = 487)
        # ax = plt.gca()  # get the axis
        # ax.set_ylim(ax.get_ylim()[::-1])  # invert the axis
        # ax.xaxis.tick_top()  # and move the X-Axis
        # plt.show()
        return a, b

    # print( STRIP(MATCHED(from_62, from_63)[0]) )

    # he have already build the strip
    # now we will search on the strip coordinates for something with smaller x
    # and y values of the second point inside the strip

    def Third_point(list1_2, array1, array2, array3):
        # initially we will weed out the larger X and Y from the
        # second point
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

    # print(Third_point((MATCHED(from_55, from_56)[0]), from_57, from_56, from_55))

    first_second_position = MATCHED(array1, array2)[1]
    third_position = Third_point((MATCHED(array1, array2)[0]), array1, array2, array3)

    # print(first_second_position)
    # print(third_position)

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

    # print( DISTANCES(first_second_position, third_position) )

    d1 = DISTANCES(first_second_position, third_position)[0] * 1.4803 / 10000000
    d2 = DISTANCES(first_second_position, third_position)[1] * 1.4803 / 10000000
    d3 = DISTANCES(first_second_position, third_position)[2] * 1.4803 / 10000000

    # velocities
    dt = (1 / 3200)  # secondds
    double_dt = (2 / 3200)  # seconds

    v1 = d1 / dt  # m/s
    v2 = d2 / dt  # m/s
    v3 = d3 / double_dt  # m/s

    print("the average velocity of the droplet is:", round(statistics.mean([v1, v2, v3]), 2), "m/s")


AVG_VELOCITY(from_62, from_63, from_64)







