python ./switch_beacon_on.py
#sleep 0.5
#python ./send_kiss_frame.py zr6aic-14 zr6aic-6 "Africube test 1234"
#sleep 0.8
#python ./switch_beacon_on.py
#echo "ZR6AIC>MORSE:AFRICUBE CQ CQ" >> ./XMIT/TX
echo "ZR6AIC>SPEECH:CQ CQ De Africube Satellite!" >> ./XMIT/TX 
sleep 12
python ./switch_beacon_off.py
