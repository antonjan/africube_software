#!/bin/sh
#Usage:	 -f frequency_to_tune_to [Hz]
#	[-s samplerate (default: 2048000 Hz)]
#	[-d device key/value query (ex: 0, 1, driver=rtlsdr, driver=hackrf)]
#	[-g tuner gain(s) (ex: 20, 40, LNA=40,VGA=20,AMP=0)]
#	[-c channel number (ex: 0)]
#	[-a antenna (ex: 'Tuner 1 50 ohm')]
#	[-p ppm_error (default: 0)]
#	[-b output_block_size (default: 16 * 16384)]
#	[-n number of samples to read (default: 0, infinite)]
#	[-I input format, CU8|CS8|CS12|CS16|CF32 (default: CS16)]
#	[-F output format, CU8|CS8|CS12|CS16|CF32 (default: CU8)]
#	[-S force sync output (default: async)]
#	[-D direct_sampling_mode, 0 (default/off), 1 (I), 2 (Q), 3 (no-mod)]
#	[-t SDR settings (ex: rfnotch_ctrl=false,dabnotch_ctrlb=true)]
#	filename (a '-' dumps samples to stdout)
#Usage:
#sendiq [-i File Input][-s Samplerate][-l] [-f Frequency] [-h Harmonic number] 
#-i            path to File Input 
#-s            SampleRate 10000-250000 
#-f float      central frequency Hz(50 kHz to 1500 MHz),
#-l            loop mode for file input
#-h            Use harmonic number n
#-t            IQ type (i16 default) {i16,u8,float,double}
#-?            help (this help).

#You need a rtl-sdr dongle in order to run this
echo "FREQ_IN=value-in_MHz GAIN=value-0_to_45 FREQ_OUT=value-in_MHz transponder"
GAIN=0
FREQ_IN=435100000
FREQ_OUT=145925000
rx_sdr -s 250000 -F CS16 -g "$GAIN" -f "$FREQ_IN" - | buffer \
  | sudo sendiq -s 250000  -f "$FREQ_OUT" -t i16 -i -
