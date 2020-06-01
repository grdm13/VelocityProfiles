import cv2
img = cv2.imread("/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/working_directory/image_135.jpg")
crop_img = img[250:450, 100:500]
cv2.imshow('OG', img)
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)