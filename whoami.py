import cv2 
import pyfiglet
import os

appname = 'who am i'

def capture():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    
    result, image = cam.read()
    while True:
        cv2.imshow(appname, image)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow(appname)
  
def clear_screen():
    name = os.name;
    if name == 'nt':
        _ = os.system('cls')
  
    else:
        _ = os.system('clear')
def look_at_me():
    clear_screen()

    result = pyfiglet.figlet_format("Look at me !!")
    print(result)

look_at_me()
capture()
