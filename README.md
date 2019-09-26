# Africube_software
This repository will have the Transponder and Telemetry software applications.

# Exsample for rpitx V2
## Send Audio from svxlink
in svxlink.conf, [Tx1]<br>
AUDIO_DEV=udp:127.0.0.1:1233<br>
arecord -c1 -r48000 -fS16_LE - | nc -l -u 1233 | csdr convert_i16_f | csdr gain_ff 7000 | csdr convert_f_samplerf 20833 | sudo rpitx -i - -m RF -s 48000 -f YOUR_FREQ
## Sending from Gnuradio
In Gnuradio use the block "TCP sink" and select port 8011, localhost, tcp, client<br>
Make sure the -s clock is the same as the Gnuradio<br>
nc -l 8011 | sudo /home/pi/rpitx/rpitx -i- -m IQFLOAT -s 48000 -f 145891 &<br>
The input for transmitter.<br>
## Sending IQ Stream from comand line
Usage:\nsendiq [-i File Input][-s Samplerate][-l] [-f Frequency] [-h Harmonic number] <br>
-i            path to File Input <br>
-s            SampleRate 10000-250000 <br>
-f float      central frequency Hz(50 kHz to 1500 MHz),<br>
-l            loop mode for file input<br>
-h            Use harmonic number <br>
-t            IQ type (i16 default) {i16,u8,float,double}<br>
-?            help (this help).<br>
\n",\
