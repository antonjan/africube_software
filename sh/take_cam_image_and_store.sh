#!/bin/sh
while:
	name = $(date "+%Y.%m.%d-%H.%M.%S")
	raspistill -o /home/pi/Images/$name.jpg
	sleep(180)
done
