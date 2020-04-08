#rpitx v1
#nc -l 8011| sudo rpitx -i - -m IQFLOAT -f 145825 
#nc -l 8011| sudo rpitx -m RF -i- -s 250000 -f 145825
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 288000 -f 145960 &
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 176400 -f 145965 &
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 125000 -f 145960 &
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo /home/pi/rpitx/rpitx -i- -m IQFLOAT -s 88200 -f 145960 &
#while true; do (nc 192.168.x.x 1234; dd if=/dev/zero bs=4096 count=30); done | sudo ./sendiq -s 250000 -f 434e6 -t u8 -i -
while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo ./sendiq -s 88200 -f 145.96e6 -t u8 -i - #transmitter

