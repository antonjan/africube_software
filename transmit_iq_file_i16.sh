cp ../iqtool/iq_tone_int16_iq.iq ./
sudo sendiq -l -s 250000 -f 145950000 -t i16 -i iq_tone_int16_iq.iq 
