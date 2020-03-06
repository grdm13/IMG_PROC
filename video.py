import numpy as np
import cv2

def count_frames('C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\mirror.mp4', override=False):
	# grab a pointer to the video file and initialize the total
	# number of frames read
	video = cv2.VideoCapture('C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\mirror.mp4')
	total = 0
	# if the override flag is passed in, revert to the manual
	# method of counting frames
	if override:
		total = count_frames_manual(video)

count_frames()
print (f'frames', total)

