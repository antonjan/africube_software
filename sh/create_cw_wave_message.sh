sudo timeout 10s sudo cw -s a  -t 1000 -v 50 -f cw_text.txt| > cw8000.wav
/usr/bin/sox -v 0.9 -S /home/pi/sh/cw800.wav /home/pi/sh/cw.wav  rate -L -s 48000
#sox cw8000.wav -r 48000 cw.wav
