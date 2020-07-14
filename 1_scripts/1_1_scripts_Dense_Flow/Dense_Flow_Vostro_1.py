import cv2
import pandas as pd
import numpy as np
import time

################### start the clock ###################
start_time = time.time()


# Get a VideoCapture object from video and store it in vs
vc = cv2.VideoCapture("/Volumes/FotoMacOs/6_PyCharm_Projects/VELOCITY VIDEOS and IMAGES/Evaluation/Water_h0_220 C_1 mLpm_1.cine")
# Read first frame
ret, first_frame = vc.read()
# Scale and resize image
resize_dim = 600
max_dim = max(first_frame.shape)
scale = resize_dim / max_dim
first_frame = cv2.resize(first_frame, None, fx=scale, fy=scale)
print("size of resized first frame is : ", first_frame.shape)
# Convert to gray scale
prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
# Create mask
mask = np.zeros_like(first_frame)
# Sets image saturation to maximum
mask[..., 1] = 255
out = cv2.VideoWriter('video.mp4', -1, 1, (600, 600))
width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
print('VC: width, height:', width, height)
#widthOUT = out.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
#heightOUT = out.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
#print('OUT: width, height:', widthOUT, heightOUT)
fps = vc.get(cv2.CAP_PROP_FPS)
print('fps:', fps)  # float
frame_count = vc.get(cv2.CAP_PROP_FRAME_COUNT)
print('frames count:', frame_count)  # float


i=0
while (vc.isOpened()):
    i=i+1
    # Read a frame from video
    ret, frame = vc.read()
    # Convert new frame format`s to gray scale and resize gray frame obtained
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=scale, fy=scale)
    print("size of the thing that goes inside the Dense flow algorithm : ", gray.shape)
    print("the final i =", i)
    cv2.imwrite("frame number {0}.jpg".format(i), gray)
    # Calculate dense optical flow by Farneback method
    # https://docs.opencv.org/3.0-beta/modules/video/doc/motion_analysis_and_object_tracking.html#calcopticalflowfarneback
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, pyr_scale=0.5, levels=5, winsize=11, iterations=5,
                                        poly_n=5, poly_sigma=1.1, flags=0)
    # Compute the magnitude and angle of the 2D vectors
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])

########## additions ######
    # 5 frames per second
    # means that the time needed per frame is 1/5
    dt = (1 / fps)  # secondds
    # after measurements 1 pixel = 8.164*10-8
    pxToMeters = (6.75531915 / 1000000) / scale
    magnitudeMeters = pxToMeters * magnitude
    velocity = magnitudeMeters / dt


    df = pd.DataFrame((velocity))
    df.to_csv(f'velocity matrix from {i} frame.csv', index=False)  # save as csv
    print("new csv printed", i)

    # Set image hue according to the optical flow direction
    mask[..., 0] = angle * 180 / np.pi / 2
    # Set image value according to the optical flow magnitude (normalized)
    mask[..., 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    # Convert HSV to RGB (BGR) color representation
    rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
    # Resize frame size to match dimensions
    frame = cv2.resize(frame, None, fx=scale, fy=scale)
    # Open a new window and displays the output frame
    dense_flow = cv2.addWeighted(frame, 1, rgb, 2, 0)

    #cv2.imshow("Dense optical flow", dense_flow)


    out.write(dense_flow)
    # Update previous frame
    prev_gray = gray
    # Frame are read by intervals of 1 millisecond. The programs breaks out of the while loop when the user presses the 'q' key
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
# The following frees up resources and closes all windows
vc.release()
cv2.destroyAllWindows()
print("the final i =", i)
print("--- %s seconds ---" % (time.time() - start_time))