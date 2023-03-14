import numpy as np 
import cv2, pafy
import time 
import telepot
import argparse
import os

# Load the cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
prev_frame_time = 0
new_frame_time = 0
nilai=0
lokasi = 'History'
if not os.path.exists(lokasi):
	print('Lokasi Cache: ', lokasi)
	os.makedirs(lokasi)

ap = argparse.ArgumentParser()
token = '5597830843:AAG4eH4zmopRdrXQAz20O9VLgY73N2skZZQ'
id_penerima = 1441844129

bot = telepot.Bot(token)

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX 
	# time when we finish processing for this frame 

	 

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        nilai= nilai + nilai
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imwrite(lokasi+'/{}.jpg'.format(nilai),img)
       # bot.sendMessage(id_penerima,"Terjadi pencurian")
       # bot.sendPhoto(id_penerima, photo=open('History/'+nilai+'.jpg','rb') )
       
        
    # Display
    new_frame_time = time.time() 
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time 
    fps = int(fps) 
    fps = str(fps)
    cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 
    out.write(img.astype('uint8'))
    cv2.imshow("img", img)


    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
# Release the VideoCapture object

cap.release()
out.release()