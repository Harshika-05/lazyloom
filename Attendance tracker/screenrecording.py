import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np 
import time
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height)# dimension decide kri =>
f = cv2.VideoWriter_fourcc(*"mp4") #format decide kiya 
output = cv2.VideoWriter("first.mp4",f,32.0,dim) #output main save kra name diya , format diya , frame per second btaya ,dimension btayi 

start_time = time.time() #strt time diya 
duration = 10 # video ki duration di 
end_time = start_time + duration #video ki end time diA 
#VIDEO KI RECORDING KAISE HGI?==>
while True:
    image = pyautogui.screenshot() #screenshot liye 
    frame_1 = np.array(image) #array bnake saari images ko aray me store kraya 
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB) #frame ka color original set kiya 
    
    output.write(frame)
    
    current_time = time.time()
    if current_time > end_time: #current time ki value end time se jyada hote hi loop ruk jaayega 
        break
    
    output.release() #jo video bnayi thi usee release krdiya 
    
    print("--- END---")
