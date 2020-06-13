import numpy as np
import matplotlib.pyplot as plt

from_56 = np.array(
    ([99, 70, 13, 17, 127],
    [233, 165, 12, 14, 119],
     [212, 165, 1, 1, 119]), float
)

from_57 = np.array(
    ([ 56  ,47  ,13 , 17, 140],
     [123 ,219  ,16  ,16, 185],
     [243, 365, 1, 1, 119]), float)




def check_for_HOR_VER_matchups(array1, array2):
    matching_HOR_VER = []
    Centroids_match = []
    for row in range(from_56.shape[0]):
        if (from_56[row][3] == from_57[row][3] - 1) or (from_56[row][3] == from_57[row][3] + 1) or (
                from_56[row][3] == from_57[row][3]):
            if (from_56[row][2] == from_57[row][2] - 1) or (from_56[row][2] == from_57[row][2] + 1) or (
                    from_56[row][2] == from_57[row][2]):
                #print(from_56[row][2], from_56[row][3])
                matching_HOR_VER.append((from_56[row][2], from_56[row][3]))
                Centroids_match.append((from_56[row][0], from_56[row][1],from_57[row][0], from_57[row][1]))
            else:pass
        else:pass
    return Centroids_match

random_1 = check_for_HOR_VER_matchups(from_56, from_57)[0]
#print(check_for_HOR_VER_matchups(from_56, from_57))
print(random_1)

def create_3_lines(list):
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

    plt.figure()
    plt.plot(matrix)
    plt.plot(list[0], list[1], color='green', marker='o')
    plt.plot(list[2], list[3], color='red', marker='o')
    plt.plot(10, 24, color='yellow', marker='o') #this is only for this test
    plt.xlim(xmin=0, xmax=413)
    plt.ylim(ymin=0, ymax = 487)
    ax = plt.gca()  # get the axis
    ax.set_ylim(ax.get_ylim()[::-1])  # invert the axis
    ax.xaxis.tick_top()  # and move the X-Axis
    plt.show()












create_3_lines(check_for_HOR_VER_matchups(from_56, from_57)[0])


#from 55
#[[ 99  70  13  17 127] <------
# [233 165  12  14 119]]

#from 56
#[[ 56  47  13  17 140] <------
 #[123 219  16  16 185]
 #[ 88 132  16  16 140]]

 #from 57
#[[ 10  24  20  16 176]<----- it must find this guy here
# [ 77 199  33  19  52]
# [129  35  25  13 142]
# [119 109  16  15 150]]