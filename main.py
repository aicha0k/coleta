import cv2
import numpy as np
import datetime as dt
import pathlib
import shutil

current_date = dt.datetime.today().strftime('%d-%m-%Y')
#checking in which usb cameras are connected
connected_cameras = []
for i in range(0,5):
    try:
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            connected_cameras.append(i)
        cap.release()
    except:
        continue
#deciding which one is the main camera
cam1 = None
cam2 = None
print(connected_cameras)
for i in range(len(connected_cameras)):
    cap = cv2.VideoCapture(connected_cameras[i])
    my_fps = float(cap.get(cv2.CAP_PROP_FPS))
    print(cap.get(cv2.CAP_PROP_FPS))
    if (my_fps == 14.999992):
        cam1 = connected_cameras[i]
        continue
    if (my_fps== 1.0):
        cam2 = connected_cameras[i]
        continue
    cap.release()

webcam = cv2.VideoCapture(cam1)
auxiliary_cam = cv2.VideoCapture(cam2)
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = float(webcam.get(cv2.CAP_PROP_FPS))   #consertar fps, video muito acelerado
    # capturing two videos at same time. two cameras
height2 = int(auxiliary_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
width2 = int(auxiliary_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
fps2 = float(auxiliary_cam.get(cv2.CAP_PROP_FPS))
print(f'fps da camera principal: {fps} fps da camera auxiliar: {fps2}')

while True:
    ret, frame = webcam.read()
    ret2, frame2 = auxiliary_cam.read()
    if ret:
        cv2.imshow("main", frame)
    if ret2:
        cv2.imshow("auxillary", frame2)
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break

webcam.release()
auxiliary_cam.release()

cv2.destroyAllWindows()