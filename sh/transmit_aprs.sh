#!/bin/bash
while true
do
/usr/bin/python /home/pi/africube_software/sh/switch_beacon_on.py
sleep 1.5
/usr/bin/python /home/pi/africube_software/sh/send_kiss_frame.py zr6aic-14 zr6aic-6 "Africube test 1234567890"
sleep 6.0
#python ./switch_beacon_on.py
#echo "ZR6AIC>ZR6AIC,WIDE1-1:=3807.41N/212006.78WbMESSAGE" >> ./XMIT/TX
sleep 1
/usr/bin/python /home/pi/africube_software/sh/switch_beacon_off.py
sleep 60
done
