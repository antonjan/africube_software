rtl_fm -f 402500000 -M raw -s 96k -g 49.6 | csdr convert_s16_f | csdr fir_decimate_cc 8 0.005 HAMMING 2>/dev/null | csdr fmdemod_quadri_cf | csdr limit_ff | csdr rational_resampler_ff 4 1 0.005 HAMMING | csdr convert_f_s16 | sox -t raw -r 48k -e signed-integer -b 16 -c 1 - -r 48000 -b 8 -t wav - 2>/dev/null| ./rs41ecc
