#!/usr/bin/python
import picamera
import datetime,time,os

# setup directory and filename

now = datetime.datetime.now()
day = now.strftime("%Y-%m-%d")
dir = day
try:
	os.mkdir(dir)
except:
	reason = "dir already exists"

filename = now.strftime("%Y-%m-%d %H%M")
filepath = dir + '/' + filename + '.h264'

# start recording from camera

camera = picamera.PiCamera()
camera.rotation = 270
camera.annotate_text_size = 16
camera.start_preview()
camera.start_recording(filepath)

recordtime = 600 # seconds
t_end = time.time() + recordtime
while time.time() < t_end:
	now = datetime.datetime.now()
	camera.annotate_text = now.strftime("%d/%m/%Y %H:%M:%S")
	time.sleep(1)

camera.stop_recording()
camera.capture(dir + '/image.jpg')
camera.stop_preview()

filesize = os.stat(filepath)
print (filesize.st_size // 10000 // recordtime)

