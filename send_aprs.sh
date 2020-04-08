#!/bin/bash
# -M, --mark {mark_freq}
# -S, --space {space_freq}

while true

	echo "Press [CTRL+C] to stop.."
do
#	cat aprs_telemetry.txt | minimodem --tx --tx-carrier  --alsa=plughw:Loopback,0,0 1200
	cat aprs_telemetry.txt | minimodem --tx --tx-carrier -S 1290 -M 2090 --alsa=plughw:Loopback,0,0 1200
	sleep 3
	
done
