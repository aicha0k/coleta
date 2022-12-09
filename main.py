import cv2
import numpy as np
import datetime
import pathlib
import shutil

from multiprocessing import Process
capturando = [True, True]


def handle_read_camera(cam_id, movement,id_capturando):
    global capturando
    print(f"camera {cam_id} iniciada")
    cam = cv2.VideoCapture(cam_id)
    height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps = float(cam.get(cv2.CAP_PROP_FPS))   #consertar fps, video muito acelerado
    writer = cv2.VideoWriter(f"num{movement}.mov", fourcc=cv2.VideoWriter_fourcc(*"DIVX"), fps=fps, frameSize=(width, height))
    while True:
        ret, frame = cam.read()
        cv2.imshow(f'Camera {cam_id}', frame)
        writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord(" "):
            break
    cam.release()
    writer.release()
    capturando[id_capturando] = False
if __name__ == "__main__":
    current_date = datetime.datetime.today().strftime("%d-%m-%Y")
    avaible_devices = []
    for i in range(0,10):
        try:
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
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
            if(float(cam.get(cv2.CAP_PROP_FPS)) == 14.999992):
                webcam = avaible_devices[i]
                continue
            if(float(cam.get(cv2.CAP_PROP_FPS)) == 5.0):
                auxillary_cam = avaible_devices[i]
                continue
            if(auxillary_cam != None and webcam != None):   #if both cameras are found,
                break
            cam.release()

        
        # print("props camera 1")
        # print(height, width, fps)
        # # capturing two videos at same time. two cameras
        # height2 = int(auxillary_cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # width2 = int(auxillary_cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        # fps2 = float(auxillary_cam.get(cv2.CAP_PROP_FPS))
        # print("props camera 2")
        # print(height2, width2, fps2)

    name = input("digite o nome da crianca: ")
    movement = input("movimento: ")
    path =pathlib.Path(f"dataset/{name}/{movement}")
    if path.exists():
        shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=False)    
    else:
        path.mkdir(parents=True, exist_ok=False)    # if the folder doesn't exist, create it


    with open(f"dataset/{name}/{movement}/info.txt", "w") as file:
        file.write(f"nome: {name},movimento numero: {movement}, data: {current_date}")

    p1 = Process(target=handle_read_camera, args=(webcam, movement,0))
    p2 = Process(target=handle_read_camera, args=(auxillary_cam,str(movement)+"aux",1))
    # p3 = Process(target=handle_end_capture, args=(movement, name))
    p1.start()
    p2.start()
    # p3.start()
    p1.join()
    p2.join()
    # p3.join()

    while(capturando[0] or capturando[1]):
        print(capturando)
    print("captura finalizada")
    shutil.move(f"num{movement}.mov", f"dataset/{name}/{movement}")
    shutil.move(f"num{movement}aux.mov", f"dataset/{name}/{movement}")
    shutil.move(f"dataset/{name}/{movement}/info.txt", f"dataset/{name}/{movement}")
    print("movimentacoes finalizadas finalizada")
    # while True:
    #     ret, frame = webcam.read()
    #     ret2, frame2 = auxillary_cam.read()
    #     cv2.imshow("main", frame)
    #     cv2.imshow("auxillary", frame2)
    #     writer.write(frame)
    #     writer2.write(frame2)
    #     if cv2.waitKey(1) & 0xFF == ord(" "):
    #         break

    

    # webcam.release()
    # auxillary_cam.release()
    # writer.release()
    # writer2.release()

    cv2.destroyAllWindows()


        
