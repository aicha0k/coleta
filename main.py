import cv2
import numpy as np
import datetime
import pathlib
import shutil

current_date = datetime.datetime.today().strftime("%d-%m-%Y")
print( cv2.cuda.getCudaEnabledDeviceCount())
avaible_devices = []
for i in range(0,10):
    try:
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            # fps = float(cap.get(cv2.CAP_PROP_FPS))   #consertar fps, video muito acelerado
            # print(f"props camera {i}")
            # print(height, width, fps)
            avaible_devices.append(i)
        cap.release()
    except:
        continue
print(avaible_devices)
if(len(avaible_devices) != 0):
    auxillary_cam = None
    webcam = None
    for i in range(0, len(avaible_devices)):
        cam = cv2.VideoCapture(avaible_devices[i])
        ret, frame = cam.read()
        cv2.imshow(f"camera {i}", frame)
        cv2.waitKey(1)
        if(input("Essa é a camera auxiliar? (s/n)") == "s"):
            auxillary_cam = cam
            cv2.destroyAllWindows()
            continue
        if(input("Essa é a camera principal? (s/n)") == "s"):
            webcam = cam
            cv2.destroyAllWindows()
            continue
        if(auxillary_cam != None and webcam != None):
            break
        cam.release()
    
    cv2.destroyAllWindows()


    webcam = cv2.VideoCapture(avaible_devices[0])
    height = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = float(webcam.get(cv2.CAP_PROP_FPS))   #consertar fps, video muito acelerado
    print("props camera 1")
    print(height, width, fps)
    # capturing two videos at same time. two cameras
    auxillary_cam = cv2.VideoCapture(avaible_devices[1])
    height2 = int(auxillary_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width2 = int(auxillary_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps2 = float(auxillary_cam.get(cv2.CAP_PROP_FPS))
    print("props camera 2")
    print(height2, width2, fps2)

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

# while True:
#     ret, frame = webcam.read()
#     ret2, frame2 = auxillary_cam.read()
#     cv2.imshow("main", frame)
#     cv2.imshow("auxillary", frame2)
#     # writer.write(frame)
#     # writer2.write(frame2)
#     if cv2.waitKey(1) & 0xFF == ord(" "):
#         break

# # shutil.move(f"num{movement}.mov", f"dataset/{name}/{movement}")
# # shutil.move(f"num{movement}aux.mov", f"dataset/{name}/{movement}")
# # shutil.move(f"dataset/{name}/{movement}/info.txt", f"dataset/{name}/{movement}")

# webcam.release()
# auxillary_cam.release()
# # writer.release()
# # writer2.release()

# cv2.destroyAllWindows()
