import numpy as np
import cv2

# read the video
video = cv2.VideoCapture('C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\mirror.mp4')


#show basic staff about the video
def BasicVideoStats():
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = video.get(cv2.cv2.CAP_PROP_POS_MSEC)
    fps = video.get(cv2.CAP_PROP_FPS)
    print(f'The total number of frames is:', frames, 'frames', ', the total duration of the video is:', duration,
      'msec and the FPS of the video is:', fps)


# show video --- to stop showing you have to press the letter q
def PlayVideo():
    while (True):
        ret, frame = video.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

#Capture images per 40 frame
def imagesplitter():
    video_images = 'C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\VideoImages'
    frameFrequency=40
# iterate all frames
    total_frame = 0
    id = 0
    while True:
        ret, frame = video.read()
        if ret is False:
            break
        total_frame += 1
        if total_frame % frameFrequency == 0:
            id += 1
            image_name = video_images + str(id) + '.jpg'
            cv2.imwrite(image_name, frame)
            print(image_name)
    video.release()

def FirstImage():
    image = cv2.imread('C:\\Users\\Dino\\PycharmProjects\\IMG_PROC\\VideoImages1.jpg')
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

FirstImage()
