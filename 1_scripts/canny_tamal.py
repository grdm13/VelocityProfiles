import cv2
import numpy as np

img = cv2.imread('/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/binary_by_tamal/test_0057.png',0)
edges = cv2.Canny(img,100,100, apertureSize = 3)
result = np.hstack((img,edges))


def CC(img):
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(img)
    label_hue = np.uint8(179 * labels / np.max(labels))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    labeled_img[label_hue == 0] = 0
    return labeled_img, nlabels, labels, stats, centroids

kernel = np.ones((2, 2), np.uint8)
erosion = cv2.erode(img, kernel, iterations=3)
dilation = cv2.dilate(erosion, kernel, iterations=1)
components, nlabels, labels, stats, centroids = CC(dilation)

#print(stats)

final_stats =[]
for row in range(stats.shape[0]):
    if (stats[row][0] == 0) or (stats[row][2] < 10):
        pass
    else:
        final_stats.append(stats[row])

#print(final_stats)
Perimeter = [] #in pixels
Area = [] #in pixels

for row in range(len(final_stats)):
    crop_img = img[
               (final_stats[row][1]-5):(final_stats[row][1] + final_stats[row][3]),
               (final_stats[row][0]-5):(final_stats[row][0] + final_stats[row][2])
               ]
    crop_img_edges = edges[
               (final_stats[row][1]-5):(final_stats[row][1] + final_stats[row][3]),
               (final_stats[row][0]-5):(final_stats[row][0] + final_stats[row][2])
               ]
    new_black_image = np.zeros((img.shape), dtype=float)
    big_crop = np.zeros((img.shape), dtype=float)
    big_crop_edges = np.zeros((img.shape), dtype=float)
    l1 = len(crop_img)
    l2 = len(crop_img[1])
    L1 = len(new_black_image)
    L2 = len(new_black_image[1])
    for i in range(L1):
        for j in range(L2):
            if (i > l1-1) or (j > l2-1):
                big_crop[i][j] = new_black_image[i][j]
                big_crop_edges[i][j] = new_black_image[i][j]
            else:
                big_crop[i][j] = crop_img[i][j]
                big_crop_edges[i][j] = crop_img_edges[i][j]

    white_pixels = 0
    white_pixels_edges = 0
    for i in range(L1):
        for j in range(L2):
            if big_crop[i][j] == 255:
                white_pixels += 1
            if big_crop_edges[i][j] == 255:
                white_pixels_edges += 1

    Perimeter.append(white_pixels_edges)
    Area.append(white_pixels)
    #print(f'area of the {row+1} droplet: ', white_pixels)
    #print(f'perimeter of the {row+1} droplet: ', white_pixels_edges)

    #cv2.imshow(f"crop from {row+1} droplet", crop_img)
    #cv2.waitKey()
    #cv2.imshow(f"big crop from {row+1} droplet", big_crop)
    #cv2.waitKey()
    #cv2.imshow(f"big crop from {row+1} droplet", big_crop_edges)
    #cv2.waitKey()
    #cv2.destroyAllWindows()


Area1 = np.array(Area)
Perimeter1 = np.array(Perimeter)
Final_stats1 = np.array(final_stats)

final_matrix = np.empty((Final_stats1.shape[0], 6), np.uint8)
for row in range(Final_stats1.shape[0]):
    final_matrix[row][0] = Final_stats1[row][0]
    final_matrix[row][1] = Final_stats1[row][1]
    final_matrix[row][2] = Final_stats1[row][2]
    final_matrix[row][3] = Final_stats1[row][3]
    final_matrix[row][4] = Perimeter1[row]
    final_matrix[row][5] = Area1[row]

print(final_matrix)

