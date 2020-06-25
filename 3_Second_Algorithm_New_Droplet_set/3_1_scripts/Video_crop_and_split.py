import cv2
import numpy as np

cap = cv2.VideoCapture( "/Volumes/FotoMacOs/6_PyCharm_Projects/VELOCITY VIDEOS and IMAGES/Evaluation/EtOH_100 pc_h0_220 C_1 mLpm_1.cine")
#cap = cv2.VideoCapture( "/Volumes/FotoMacOs/6_PyCharm_Projects/VELOCITY VIDEOS and IMAGES/Evaluation/Water_h0_220 C_1 mLpm_1.cine")

# (x, y, w, h) = cv2.boundingRect(c)
# cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 20)
# roi = frame[y:y+h, x:x+w]


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

i  = 0
while True:
    i = i + 1
    ret, frame = cap.read()
    sky = frame[100:600, 430:500]
    cv2.imwrite(f'frame np{i}.tif', sky)

