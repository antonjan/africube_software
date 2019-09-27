sudo /usr/bin/timeout 11s /usr/bin/arecord -c1 -t wav -r 48000  --vumeter=mono -D hw:Loopback,1,0 -fS16_LE /home/pi/africube_software/sh/africube_cw.wav &
sudo /usr/bin/timeout 10s /usr/bin/cw -s a -d hw:Loopback,1,0 -t 1000 -v 50 -f /home/pi/africube_software/sh/cw_text.txt
#sudo aplay -D hw:1,0,0 /home/pi/africube_software/sh/africube_cw.wav 
