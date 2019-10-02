#rpitx -2.0
#Usage:
#rpitx [-i File Input][-m ModeInput] [-f frequency output] [-s Samplerate] [-l] [-p ppm] [-h] 
#-m            {IQ(FileInput is a Stereo Wav contains I on left Channel, Q on right channel)}
#              {IQFLOAT(FileInput is a Raw float interlaced I,Q)}
#              {RF(FileInput is a (double)Frequency,Time in nanoseconds}
#      	      {RFA(FileInput is a (double)Frequency,(int)Time in nanoseconds,(float)Amplitude}
#	      {VFO (constant frequency)}
#-i            path to File Input 
#-f float      frequency to output on GPIO_4 pin 7 in khz : (130 kHz to 750 MHz),
#-l            loop mode for file input
#-p float      frequency correction in parts per million (ppm), positive or negative, for calibration, default 0.
#-h            help (this help).

sudo aprs -o - --callsign ZR6AIC --output - "Africube transponder 500mw Beacon de ZR6AIC" | csdr convert_i16_f | csdr gain_ff 9000 | csdr convert_f_samplerf 20833 | sudo rpitx -m RF -i- -f 145950 
#sudo aprs --callsign ZR6AIC --output - "10mw Beloon Beacon de ZR6AIC" | csdr convert_i16_f | csdr gain_ff 7000 |  sudo rpitx -m RF -i - -f 145950

#(while true; do cat sampleaudio.wav; done) | csdr convert_i16_f \
#  | csdr gain_ff 7000 | csdr convert_f_samplerf 20833 \
#  | sudo ./rpitx -i- -m RF -f "$1"
#sudo aprs -o - --callsign ZR6AIC --output - "Africube transponder 500mw Beacon de ZR6AIC" | csdr convert_i16_f | csdr gain_ff 4000 | csdr convert_f_samplerf 20833 | sudo rpitx -m RF -i- -f 145950

#sudo direwolf -x - | csdr convert_i16_f | csdr gain_ff 4000 | csdr convert_f_samplerf 20833 | sudo rpitx -m RF -i- -f 145950

