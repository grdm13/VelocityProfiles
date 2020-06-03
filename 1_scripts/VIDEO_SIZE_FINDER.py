import cv2

vcap = cv2.VideoCapture('/Users/georgedamoulakis/PycharmProjects/VelocityProfiles/2_videos/spray_highmag.avi') # 0=camera

if vcap.isOpened():
    width  = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
    height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    #print(cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT) # 3, 4

    # or
   # width  = vcap.get(3) # float
   # height = vcap.get(4) # float

    print('width, height:', width, height)

    fps = vcap.get(cv2.CAP_PROP_FPS)
    print('fps:', fps)  # float
    #print(cv2.CAP_PROP_FPS) # 5

    frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
    print('frames count:', frame_count)  # float
    #print(cv2.CAP_PROP_FRAME_COUNT) # 7