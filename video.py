import numpy as np
import cv2

# read the video
video = cv2.VideoCapture('C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\mirror.mp4')


#show basic staff about the video
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
duration = video.get(cv2.cv2.CAP_PROP_POS_MSEC)
fps = video.get(cv2.CAP_PROP_FPS)
print(f'The total number of frames is:', frames, 'frames', ', the total duration of the video is:', duration,
      'msec and the FPS of the video is:', fps)


# show video --- to stop showing you have to press the letter q
while (True):
    ret, frame = video.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

#reading and showing the first frame
