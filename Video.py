import picamera
import datetime as dt
from time import sleep
import os
import socket


# resolution
height = 1280
width = 720

# framerate
fps = 30

# file location
save_name = "/"
filename = dt.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
completed_video_name = os.path.join(save_name, filename + ".h264")

# camera initialization
camera = picamera.PiCamera()
camera.resolution = (height, width)
camera.framerate = fps
camera.vflip = True

# start recoding
camera.start_recording(completed_video_name, quality=30)

# tests to see if there is a valid connection
is_connected = True
while is_connected:
    try:
        socket.create_connection(("www.google.com", 80))
        sleep(1)
    # ends the loop when the internet disconnects
    except OSError:
        is_connected = False

# stop recording
camera.stop_recording()

# wraps h264 file in mp4
exec_cmd = 'MP4Box -add $s.h264 $s.mp4'.replace('$s', filename)
command = os.popen(exec_cmd)

# removes h264 file
del_cmd = "rm " + filename + ".h264"
os.popen(completed_video_name)
