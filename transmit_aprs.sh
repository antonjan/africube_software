#python ./switch_beacon_on.py
#sleep 0.5
python ./send_kiss_frame.py zr6aic-14 zr6aic-6 "Africube test 1234"
sleep 0.8
python ./switch_beacon_on.py
#echo "ZR6AIC>ZR6AIC,WIDE1-1:=3807.41N/212006.78WbMESSAGE" >> ./XMIT/TX
sleep 1
python ./switch_beacon_off.py
