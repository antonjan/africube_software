#rpitx v1
sleep 50
#nc -l 8011| sudo rpitx -i - -m IQFLOAT -f 145825 
#nc -l 8011| sudo rpitx -m RF -i- -s 250000 -f 145825
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 288000 -f 145960 &
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 176400 -f 145965 &
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 125000 -f 145960 &
while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo /home/pi/rpitx/rpitx -i- -m IQFLOAT -s 88200 -f 145950 &
sleep 20
/home/pi/africube_software/top_block.py &
sleep 15
/home/pi/africube_software/sh/start_direwolf.sh &
sleep 15
/home/pi/africube_software/sh/start_aprs_kiss.sh &
sleep 15
/home/pi/africube_software/sh/transmit_aprs.sh &


