echo "AFRICUBE DE ZR6AIC R1T1"| /usr/bin/cw -s a -t 1000 -v 50 -f /home/pi/sh/cw_text.txt > cw8000.wav
sleep 1
sudo /usr/bin/sox -v 0.9 -S /home/pi/sh/cw8000.wav /home/pi/sh/cw.wav  rate -L -s 48000
sleep 1
