arecord -c1 -r 48000 -D hw:Loopback,1,0 -f S16_LE - | csdr convert_s16_f |
csdr dsb_fc | csdr bandpass_fir_fft_cc 0 0.1 0.01 | csdr gain_ff 2.0 | csdr
shift_addition_cc 0.2 | sudo rpitx -i - -m IQ -f $FREQUENCY
