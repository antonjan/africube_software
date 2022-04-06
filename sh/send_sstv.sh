#!/bin/sh
python3 /home/pi/pySSTV/camera.py 
python3 -m pysstv --mode PD180 --fskid ZR6AIC --resize ./picture.jpg /home/pi/sh/cam.wav
