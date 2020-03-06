import numpy as np
import cv2

# read the video
video = cv2.VideoCapture('C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\mirror.mp4')

# measure the video frames
frames = 0
frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(f'The total number of frames is:', frames, 'frames')

# measure the duration of the video
duration = 0
#Checking shows that this sets the point after the last frame (not before it), so the timestamp is indeed the exact total length of the stream
d = video.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
print(f'Are we at the last frame?', d)
duration = int(video.get(cv2.CAP_PROP_POS_MSEC))
duration_sec = duration / 1000
print(f'The total duration of the video is:', duration_sec, 'sec')

#finding out the fps of the video
fps = 0
fps = int(frames / duration_sec)
print(f'The FPS of the video is:', fps)

