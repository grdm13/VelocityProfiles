import numpy as np
import statistics
import math
import matplotlib.pyplot as plt

from_62 = np.array(
    (
[143, 116, 14, 17, 125],
[145, 45, 20, 20, 66],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ), float)

from_63 = np.array(
    (
[12, 62, 14, 17, 125],
[45, 5, 20, 20, 66],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ), float)

from_64 = np.array(
    (
[1, 61, 14, 17, 125],
[4, 1, 20, 20, 66],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ), float)


def AVG_VELOCITY(array1, array2, array3):
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

    #print(MATCHED(array1, array2))
    matched_array = np.array(MATCHED(array1,array2))
    for i in range(matched_array.shape[0]):
        if matched_array[i][0] == 0:
            print("dummy line")
        else:
            d1 = 0
            d2 = 0
            d3 = 0
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

            dummy = int(-1)

            def Third_point(list1_2, array1, array2, array3):
                New_Y = 0
                New_X = 0
                for row in range(array3.shape[0]):
                    if (array3[row][0] > 0) and (list1_2[2] > array3[row][0]) and (list1_2[3] > array3[row][1]):
                        New_X = (array3[row][0])
                        New_Y = (array3[row][1])
                    else:
                        break
                print("new X and Y are: ", New_X, New_Y)
                # now we know the smaller X n Y
                # and now we will have to find the inside the strip
                AA = (STRIP(MATCHED(array1, array2)[0]))[0]
                BB = (STRIP(MATCHED(array1, array2)[0]))[1]
                print("the A and B are:", AA, BB)
                Final_Y = 0
                Final_X = 0
                if (New_Y < AA * (New_X) + (4 * BB)) and (New_Y > AA * (New_X) - (2 * BB)):
                    Final_X = New_X
                    Final_Y = New_Y
                else:
                    pass
                return Final_X, Final_Y


            first_second_position = MATCHED(array1, array2)[i]
            third_position = Third_point((MATCHED(array1, array2)[i]), array1, array2, array3)
            print("the first and second point are:", first_second_position)
            print("the third point has dimensions:", third_position)


            if third_position == (0,0):
                print("dummy line vol2")
                print(f"---------------------------------------")
            else:
                def DISTANCES(list1, list2):
                    x = [list1[0], list1[1]]  # ie 143 116
                    y = [list1[2], list1[3]]  # ie 12 62
                    z = [list2[0], list2[1]]  # ie 1 61
                    y_x_0 = y[0] - x[0]
                    y_z_0 = y[0] - z[0]
                    z_x_0 = z[0] - x[0]
                    y_x_1 = y[1] - x[1]
                    y_z_1 = y[1] - z[1]
                    z_x_1 = z[1] - x[1]
                    first_second_distanse = math.sqrt((y_x_0 ** 2) + (y_x_1 ** 2))
                    second_third_distanse = math.sqrt((y_z_0 ** 2) + (y_z_1 ** 2))
                    first_third_distanse = math.sqrt((z_x_0 ** 2) + (z_x_1 ** 2))
                    # print("Euclidean distance from x to y: ", first_second_distanse)
                    # print("Euclidean distance from x to y: ", second_third_distanse)
                    # print("Euclidean distance from x to y: ", first_third_distanse)
                    return first_second_distanse, second_third_distanse, first_third_distanse

                # distances
                d1 = DISTANCES(first_second_position, third_position)[0] * 6.75531915 / 1000000
                d2 = DISTANCES(first_second_position, third_position)[1] * 6.75531915 / 1000000
                d3 = DISTANCES(first_second_position, third_position)[2] * 6.75531915 / 1000000
                # time
                dt = (1 / 3200)  # secondds
                double_dt = (2 / 3200)  # seconds
                # velocities
                v1 = d1 / dt  # m/s
                v2 = d2 / dt  # m/s
                v3 = d3 / double_dt  # m/s

                print(f"the average velocity of the {i} droplet is:", round(statistics.mean([v1, v2, v3]), 2), "m/s")
                print(f"---------------------------------------")



AVG_VELOCITY(from_62, from_63, from_64)







