import cv2
import numpy as np
import datetime
import pathlib
import shutil

current_date = datetime.datetime.today().strftime("%d-%m-%Y")
webcam = cv2.VideoCapture(1)
# capturing two videos at same time. two cameras
auxillary_cam = cv2.VideoCapture(0)
height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
height2 = int(auxillary_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
width2 = int(auxillary_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = float(webcam.get(cv2.CAP_PROP_FPS))   #consertar fps, video muito acelerado
fps2 = float(auxillary_cam.get(cv2.CAP_PROP_FPS))

# name = input("digite o nome da crianca: ")
# movement = input("movimento: ")
# path =pathlib.Path(f"dataset/{name}/{movement}")
# if path.exists():
#     shutil.rmtree(path)
#     path.mkdir(parents=True, exist_ok=False)    
# else:
#     path.mkdir(parents=True, exist_ok=False)    # if the folder doesn't exist, create it

# writer = cv2.VideoWriter(f"num{movement}.mov", fourcc=cv2.VideoWriter_fourcc(*"DIVX"), fps=fps, frameSize=(width, height))
# writer2 = cv2.VideoWriter(f"num{movement}aux.mov", fourcc=cv2.VideoWriter_fourcc(*"DIVX"), fps=fps2, frameSize=(width2, height2))
# with open(f"dataset/{name}/{movement}/info.txt", "w") as file:
#     file.write(f"nome: {name},movimento numero: {movement}, data: {current_date}")

while True:
    ret, frame = webcam.read()
    ret2, frame2 = auxillary_cam.read()
    cv2.imshow("main", frame)
    cv2.imshow("auxillary", frame2)
    # writer.write(frame)
    # writer2.write(frame2)
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break

# shutil.move(f"num{movement}.mov", f"dataset/{name}/{movement}")
# shutil.move(f"num{movement}aux.mov", f"dataset/{name}/{movement}")
# shutil.move(f"dataset/{name}/{movement}/info.txt", f"dataset/{name}/{movement}")

webcam.release()
auxillary_cam.release()
# writer.release()
# writer2.release()

cv2.destroyAllWindows()
