import cv2

cap = cv2.VideoCapture( "/Volumes/FotoMacOs/6_PyCharm_Projects/VELOCITY VIDEOS and IMAGES/Evaluation/EtOH_100 pc_h0_220 C_1 mLpm_1.cine")
#cap = cv2.VideoCapture("/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/3_Second_Algorithm_New_Droplet_set/3_1_scripts/output.avi")

# (x, y, w, h) = cv2.boundingRect(c)
# cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 20)
# roi = frame[y:y+h, x:x+w]

while True:
    ret, frame = cap.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == 27: exit(0)