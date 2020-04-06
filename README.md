# Africube_software
This repository will have the Transponder and Telemetry software applications.
Diagram
![Block Diagram](Digital_Transponder_v4.jpg?raw=true "Block Diagram")<br>
# MSI input SDR chipset configueration for Sateliite
## IF bandwidth<br>
<br>
This selects the IF filter. Following bandwidths are available according to MSi001 specs:<br>

1) 200 kHz <<<<<<<<<<<<<br>
2) 300 kHz<br>
3) 600 kHz<br>
4) 1536 kHz<br>
5) 5000 kHz<br>
6) 6000 kHz<br>
7) 7000 kHz<br>
8) 8000 kHz<br>

## IF Type
<br>
This selects the IF frequency between these values:<br>
<br>
1) 0 for zero IF<br>
2) 450 kHz: you have to set sample rate to 1792 kHz (7) and use decimation (8) with an infradyne position (9)<br>
3) 1620 kHz: you have to set sample rate to 6400 kHz (7) and use decimation (8) with an infradyne position (9)<br>
4) 2048 kHz: you have to set sample rate to 8192 kHz (7) and use decimation (8) with an infradyne position (9)<br>

## Sample rate
<br>
You have the choice between various sample rates from 1536 to 8192 kHz. Some values have a special destination:
<br>
1) 1792 kHz: for use with an IF of 450 kHz.<br>
2) 6400 kHz: for use with an IF of 1620 kHz.<br>
3) 8192 kHz: for use with an IF of 2048 kHz.<br>

## Decimation
<br>
Decimation in powers of two from 1 (no decimation) to 64.<br>
## Decimated bandpass center frequency position relative the SDRplay center frequency

Cen: the decimation operation takes place around the SDRplay center frequency Fs<br>
Inf: the decimation operation takes place around Fs - Fc.<br>
Sup: the decimation operation takes place around Fs + Fc.<br>

## With SR as the sample rate before decimation Fc is calculated as:

if decimation n is 4 or lower: Fc = SR/2^(log2(n)-1). The device center frequency is on the side of the baseband. You need a RF filter bandwidth at least twice the baseband.<br>
if decimation n is 8 or higher: Fc = SR/n. The device center frequency is half the baseband away from the side of the baseband. You need a RF filter bandwidth at least 3 times the baseband.<br>
# IF Attenuator


# Exsample for rpitx V2 not (usable on PI 4)
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
Usage: sendiq [-i File Input][-s Samplerate][-l] [-f Frequency] [-h Harmonic number] <br>
-i            path to File Input <br>
-s            SampleRate 10000-250000 <br>
-f float      central frequency Hz(50 kHz to 1500 MHz),<br>
-l            loop mode for file input<br>
-h            Use harmonic number <br>
-t            IQ type (i16 default) {i16,u8,float,double}<br>
-?            help (this help).<br>

# Aditional gnuradio addons requerd
libboostall-dev<br>
swig<br>
gnuradio 3.7<br>
gr-bruninga Requierd for FSK generation for FM telemetry<br>
gr-sdrplay  Requierd for MSI miri sdr froned chipset driver<br>
gr-ax25 Requierd for AFSK decoding for command controle<br>
gr-osmosdr (not reqierd any more as it is using to much CPU)<br>

# Ground Station Configuration.
![Link to the Wiki on how to enable a windows telemetry configuration](https://github.com/antonjan/africube_software/wiki/Telemetry-Decoding?raw=true "Ground Station")<br>

# Decoding the telemetry cw and afsk/aprs
## multimon-ng

Multimon-ng is a general purpose decoder. It can take wav or raw files and decode a variety of modes among which: CW, AFSK, FSK...
## How to CW

The gain is in dB and has a considerable impact on the decoding in the special case of CW. You have to adjust gain to get proper decoding.

Then you must apply on the raw file the proper decoder:
multimon-ng -a MORSE_CW -t raw file.raw
## How to AFSK

Use multimon-ng with AFSK1200 decoder
multimon-ng -t raw -a AFSK1200 $file.raw

You can add more decoders if needed with additionnal "-a" options
## Direwolf

Direwolf is a software encoder/decoder for APRS (AX.25). It can take raw files and decode APRS.
How to

direwolf -B 1200 -b 16 -n 1 -r 48000 -q hd -t 0 -q h -q d -d p -d t -a 0 - < file.raw

## QSSTV

QSSTV is a modem software to send and receive SSTV (Slow Scan Television).
Usage

   
Open QSSTV and specify "Sound>Sound Input: from file"
Press the play button and you will be asked to select the previously generated wav file. The decoding should start now.
##WXtoImg

WXtoImg is a program used to produce neat weather pictures from APT format receptions of NOAA satellites.

It uses a .wav file and produces weather picture with possible nice overlays (frontiers, colors...).
Usage
wxtoimg -t n -e HVC -N 1193773_2019-11-12T07-13-50.wav > 1193773_2019-11-12T07-13-50.png 
