import numpy as np
import cv2

# read the video
video = cv2.VideoCapture('C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\mirror.mp4')

# measure the video frames
frames = 0
frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'the total number of frames is:', frames)

