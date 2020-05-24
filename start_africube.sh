#!/bin/bash
export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/home/pi/africube_software 
cd /home/pi/africube_software/
/usr/bin/python /home/pi/africube_software/top_block.py&
/usr/local/bin/direwolf -t 0 -a -d -c /home/pi/direwolf/telemetry-toolkit/telem-africube.conf &
