sudo timeout 10s arecord -c1 -t wav -r 48000  --vumeter=mono -D hw:Loopback,1,0 -fS16_LE /home/pi/sh/direwalf.wav &
sudo timeout 9s direwolf -c /home/pi/africube_software/telem-balloon.conf
sleep 1
sudo sox -v 0.3 -S /home/pi/sh/direwalf.wav /home/pi/sh/direwalf_sox.wav  rate -L -s 48000
sleep 1
#sudo /home/pi/Downloads/rpitx_new/rpitx/pifm  /home/pi/sh/direwalf_sox.wav /home/pi/sh/direwalf_sox.wav.ft
sleep 1
sudo rpitx -i /home/pi/sh/direwalf.wav -m RF -f 145950 -s 48000
#rpitx [-i File Input][-m ModeInput] [-f frequency output] [-s Samplerate] [-l] [-p ppm] [-h] 
#-m            {IQ(FileInput is a Stereo Wav contains I on left Channel, Q on right channel)}
#              {IQFLOAT(FileInput is a Raw float interlaced I,Q)}
#              {RF(FileInput is a (double)Frequency,Time in nanoseconds}
#       	      {RFA(FileInput is a (double)Frequency,(int)Time in nanoseconds,(float)Amplitude}
#	      {VFO (constant frequency)}
#-i            path to File Input 
#-f float      frequency to output on GPIO_4 pin 7 in khz : (130 kHz to 750 MHz),
#-l            loop mode for file input
#-p float      frequency correction in parts per million (ppm), positive or negative, for calibration, default 0.
#-h            help (this help).

