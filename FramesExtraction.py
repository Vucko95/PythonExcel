import cv2

video = cv2.VideoCapture("video.mp4")
# print(video.read())
success, frame = video.read()
count = 1
while success:
    cv2.imwrite(f'frames/{count}.jpeg', frame)
    success, frame = video.read()
    count += 1

# width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
# nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
# fps = video.get(cv2.CAP_PROP_FPS)
# print(width, height, nr_frames, fps)
