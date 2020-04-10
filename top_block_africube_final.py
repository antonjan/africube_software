#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author: Anton Janovsky
# Generated: Mon Apr  6 16:31:00 2020

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sdrplay


class top_block_africube_final(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "final_africube.py")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2205000

        ##################################################
        # Blocks
        ##################################################
        self.sdrplay_rsp1_source_0 = sdrplay.rsp1_source(435.100e6, 200, True, 0, False, False,
                False, 0, 1, samp_rate, True, '0')
            
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=25,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((.9, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((2, ))
        self.blks2_tcp_sink_1 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr='127.0.0.1',
        	port=8011,
        	server=False,
        )
        self.audio_source_0 = audio.source(44100, 'plughw:0,1', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(88200, analog.GR_COS_WAVE, 38000, 1, 0)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=44100,
        	quad_rate=88200,
        	tau=75e-6,
        	max_dev=1800,
        	fh=-1.0,
                )
        self.analog_agc_xx_0 = analog.agc_cc(1e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(4)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_tcp_sink_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_null_sink_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_agc_xx_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=top_block_africube_final, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
