#!/usr/bin/python
import picamera
import datetime,time,os

camera = picamera.PiCamera()
camera.rotation = 270
camera.annotate_text_size = 16
recordtime = 60 # seconds

while True:
	# setup directory and filename
	now = datetime.datetime.now()
	day = now.strftime("%Y-%m-%d")
	dir = '/home/pi/' + day
	try:
		os.mkdir(dir)
	except:
		reason = "dir already exists"
	filename = now.strftime("%Y-%m-%d %H%M")
	filepath = dir + '/' + filename + '.h264'
	
	# start recording from camera
	camera.start_preview()
	camera.start_recording(filepath)
	t_end = time.time() + recordtime
	while time.time() < t_end:
		now = datetime.datetime.now()
		camera.annotate_text = now.strftime("%d/%m/%Y %H:%M:%S")
		time.sleep(1)
	camera.stop_recording()
	camera.stop_preview()

	filesize = os.stat(filepath)
