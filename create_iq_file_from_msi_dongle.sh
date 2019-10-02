#rx_sdr
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
rx_sdr -f 435100000 -s 250000 -d 0  -g 0  -F CS16 rx_sdr_recording_CS16.iq



