cp ../iqtool/iq_tone_int8_iq.iq ./
sudo sendiq -s 250000 -f 145950000 -t u8 -i iq_tone_int8_iq.iq 
