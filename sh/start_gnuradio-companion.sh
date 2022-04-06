sleep 3
#sudo /home/pi/sh/resett_all_usb.sh
sleep 3
sudo /home/pi/sh/stop_sdrplay_service.sh
sleep 3
sudo /home/pi/sh/start_sdrplay_service.sh
sleep 3
sudo /home/pi/sh/check_sdrplay_sopy_connector.sh
sleep 3
sudo /home/pi/sh/check_sdrplay_sopy_connector.sh
sleep 3
sudo modprobe snd-aloop
sleep 3
#sudo /usr/local/bin/SoapySDRUtil --probe="driver=sdrplay"
sleep 3
export XDG_RUNTIME_DIR=/run/user/0
#usbreset 1df7:2500
sleep 10
#export XAUTHORITY=/home/pi/.Xauthority 
#export DISPLAY=localhost:11.0
export PATH=/usr/local/bin:/root/.local/bin:$PATH
export PYTHONPATH=/usr/local/lib/python3/dist-packages:/usr/local/lib/python2.7/dist-packages/construct
:$PYTHONPATH
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib/python2.7/dist-packages/construct:$LD_LIBRARY_CONFIG
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/home/pi/.local/lib/python3.7/site-packages/construct:$PKG_CONFIG_PATH
/usr/local/bin/gnuradio-companion
