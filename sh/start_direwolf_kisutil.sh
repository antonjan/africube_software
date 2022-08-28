#Save received frames to files
#When the -o (output) option is specified, each received frame will be stored in its own file in the
#specified directory. The file name is based on the date and time. For example,
# mkdir REC
# kissutil -o REC
#mkdir XMIT
#kissutil -f XMIT
/usr/local/bin/direwolf -c /home/pi/direwolf/build/direwolf.conf &
sleep 6
echo "direwolf started"
/usr/local/bin/kissutil -o /home/pi/sh/aprs_tx_rx/REC -f /home/pi/sh/aprs_tx_rx/XMIT &
echo "kissutil started"
sleep 5
echo "ZR6AIC>APDR15,WIDE1-1:=3807.41N/212006.78WbMESSAGE" > /home/pi/sh/aprs_tx_rx/XMIT/send
echo "send test aprs message"
