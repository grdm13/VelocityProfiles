import cv2
import math
videoFile = "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/trimmed.mp4"
imagesFolder = "/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/split_images_from_video"
cap = cv2.VideoCapture(videoFile)
frameRate = cv2.CAP_PROP_FPS  #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print("Done!")