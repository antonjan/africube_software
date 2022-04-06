#!/bin/sh
sudo modprobe snd-aloop
#/home/pi/pySSTV/create_img1.sh
#sleep 3
#/home/pi/pySSTV/create_img2.sh
#sleep 3
#/home/pi/pySSTV/create_img3.sh
/usr/bin/python3 /home/pi/sh/set_sdr_low_pass_gain.py
sleep 1
/usr/bin/python3 /home/pi/sh/set_sdr_rx_rf_gain.py
sleep 1
while :
do
#	/home/pi/pySSTV/send_sstv.sh&
	/usr/bin/python3 /home/pi/sh/beacon_on_xml_rpc.py
	/usr/bin/aplay -D plughw:2,0 /home/pi/sh/aprs_tes.wav
	sleep 0.1
	/usr/bin/python3 /home/pi/sh/beacon_off_xml_rpc.py 
	sleep 3
	/usr/bin/python3 /home/pi/sh/beacon_on_xml_rpc.py
	sleep 0.1
	/usr/bin/aplay -D plughw:2,0 ./cw.wav
	sleep 0.1
	/usr/bin/python3 /home/pi/sh/beacon_off_xml_rpc.py
	sleep 3
	/usr/bin/python3 /home/pi/sh/beacon_on_xml_rpc.py
	sleep 0.1
	/usr/bin/aplay -D plughw:2,0 /home/pi/sh/africube_voice.wav
	sleep 0.1
	/usr/bin/python3 /home/pi/sh/beacon_off_xml_rpc.py
	sleep 3
	/usr/bin/python3 /home/pi/sh/beacon_on_xml_rpc.py
	sleep 0.1
	/usr/bin/aplay -D plughw:2,0 ./sstv_img1.wav
	sleep 0.1
	/usr/bin/python3 /home/pi/sh/beacon_off_xml_rpc.py
	sleep 3
done
