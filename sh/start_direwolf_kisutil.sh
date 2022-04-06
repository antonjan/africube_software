/usr/local/bin/direwolf -c /home/pi/direwolf/build/direwolf.conf &
sleep 6
echo "direwolf started"
/usr/local/bin/kissutil -o /home/pi/sh/aprs_tx_rx/REC -f /home/pi/sh/aprs_tx_rx/XMIT &
echo "kissutil started"
sleep 5
echo "ZR6AIC>APDR15,WIDE1-1:=3807.41N/212006.78WbMESSAGE" > /home/pi/sh/aprs_tx_rx/XMIT/send
echo "send test aprs message"
