#!/bin/bash
#/home/pi/.bashrc
cd /home/pi/sh
/usr/bin/sleep 10
export PATH=/home/pi/.local/bin:/home/pi/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:$PATH
/usr/bin/sudo /usr/sbin/modprobe snd-aloop
/usr/bin/sleep 5
/usr/bin/sudo /home/pi/sh/stop_sdrplay_service.sh
/usr/bin/sleep 5
/usr/bin/sudo /home/pi/sh/start_sdrplay_service.sh
/usr/bin/sleep 4
/usr/bin/sudo /home/pi/sh/check_sdrplay_sopy_connector.sh
/usr/bin/sleep 3
/usr/bin/sudo /home/pi/sh/check_sdrplay_sopy_connector.sh
sleep 5
export XDG_RUNTIME_DIR=/run/user/0
#usbreset 1df7:2500
sleep 10
#export XAUTHORITY=/home/pi/.Xauthority 
#export DISPLAY=localhost:11.0
export PATH=/usr/local/bin:/root/.local/bin:/usr/sbin:/usr/sbin:/usr/bin:/usr/lib:/root/.local/lib/python3.7/site-packages:$PATH
export PYTHONPATH=/usr/local/lib/python3/dist-packages:/usr/local/lib/python2.7/dist-packages/construct:/usr/local/lib/python3.7/dist-packages:/home/pi/.local/lib/python3.7/site-packages:/home/pi/sh:$PYTHONPATH
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib/python2.7/dist-packages/construct:$LD_LIBRARY_CONFIG
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/home/pi/.local/lib/python3.7/site-packages/construct:$PKG_CONFIG_PATH
#/usr/local/bin/gnuradio-companion
#/home/pi/rptx_trasnsmitter.py
#/usr/bin/python3 -u /home/pi/gnuradio_radios/SDRPlay.py
#/usr/bin/python3 -u /home/pi/africube_software/africube_top_block.py
#/usr/bin/python3 -u /home/pi/gnuradio_radios/test_rpitx.py
/usr/bin/sleep 4
#/usr/bin/python3 -u  /home/pi/gnuradio_radios/working_africube_transponder_and_beacon.py &
/usr/bin/python3 -u /home/pi/gnuradio_radios/africube_v1_with_beacon_xml_rpc.py &
#/usr/bin/python3 -u /home/pi/gnuradio_radios/test_rpitx.py &
/usr/bin/sleep 5
#/usr/bin/python3 -u /home/pi/gnuradio_radios/test_rpitx.py
#/usr/bin/python3 -u /home/pi/sh/get_python_paths.py
#sleep 10
#sudo /home/pi/sh/start_africube_transponder.sh.work
echo "*************************** transponder on ****************************"
/home/pi/sh/send_aprs_to_loopback.sh
