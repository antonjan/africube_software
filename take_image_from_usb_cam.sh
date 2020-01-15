#!/bin/bash
#sudo apt-get install fswebcam
#sudo usermod -a -G video pi 
mkdir /home/pi/webcam
DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --png --no-banner /home/pi/webcam/$DATE.jpg
