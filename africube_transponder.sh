#!/bin/sh

#You need a rtl-sdr dongle in order to run this
echo "FREQ_IN=value-in_MHz GAIN=value-0_to_45 FREQ_OUT=value-in_MHz transponder"
GAIN=0
FREQ_IN=435100000
FREQ_OUT=145825000
rtl_sdr -s 250000 -g "$GAIN" -f "$FREQ_IN" - | buffer \
  | sudo ./sendiq -s 250000 -f "$FREQ_OUT" -t u8 -i -
