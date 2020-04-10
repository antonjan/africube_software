#rpitx v1
#nc -l 8011| sudo rpitx -i - -m IQFLOAT -f 145825 
#nc -l 8011| sudo rpitx -m RF -i- -s 250000 -f 145825
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 288000 -f 145960 &
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 176400 -f 145965 &
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 125000 -f 145960 &
<<<<<<< HEAD
#while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo /home/pi/rpitx_v1/rpitx-1/rpitx -i- -m IQFLOAT -s 88200 -f 145960 &
while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo /home/pi/rpitx_v2/rpitx -i- -m IQFLOAT -s 88200 -f 145950 &
=======
while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 88200 -f 145950 
>>>>>>> c443ce7bd25daf7dd9ed4d22bc24d673762e6ce6

