#!/bin/sh
sudo modprobe snd-aloop
/home/pi/pySSTV/create_img1.sh
sleep 3
/home/pi/pySSTV/create_img2.sh
sleep 3
/home/pi/pySSTV/create_img3.sh
sleep 3
while :
do
	/home/pi/pySSTV/send_sstv.sh&
	aplay -D plughw:2,0 ./img1.wav
	sleep 3
	aplay -D plughw:2,0 ./aprs_tes.wav
	sleep 3
	aplay -D plughw:2,0 ./cw.wav
	sleep 3
	aplay -D plughw:2,0 ./camera.wav
	sleep 3
	/home/pi/pySSTV/send_sstv.sh&
	aplay -D plughw:2,0 ./aprs_tes.wav
	sleep 3
	aplay -D plughw:2,0 ./cw.wav
	sleep 3
	aplay -D plughw:2,0 ./img2.wav
	sleep 3
	aplay -D plughw:2,0 ./aprs_tes.wav
	sleep 3
	aplay -D plughw:2,0 ./cw.wav
	sleep 3
	aplay -D plughw:2,0 ./camera.wav
	sleep 3
	/home/pi/pySSTV/send_sstv.sh&
	aplay -D plughw:2,0 ./aprs_tes.wav
	sleep 3
	aplay -D plughw:2,0 ./cw.wav
	sleep 3
	aplay -D plughw:2,0 ./img3.wav
	sleep 3
	aplay -D plughw:2,0 ./aprs_tes.wav
	sleep 3
	aplay -D plughw:2,0 ./cw.wav
	sleep 3
	aplay -D plughw:2,0 ./camera.wav
	sleep 3
	aplay -D plughw:2,0 ./aprs_tes.wav
	sleep 3
	aplay -D plughw:2,0 ./cw.wav
done
