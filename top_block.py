#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Africube
# Author: Anton Janovsky
# Generated: Wed Jun 24 19:39:05 2020
##################################################

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
import SimpleXMLRPCServer
import sdrplay
import threading


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Africube")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate_Baseband = samp_rate_Baseband = 88200
        self.samp_rate = samp_rate = 2205000
        self.beacon = beacon = 1

        ##################################################
        # Blocks
        ##################################################
        self.xmlrpc_server_0 = SimpleXMLRPCServer.SimpleXMLRPCServer(('localhost', 8080), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.sdrplay_rsp1_source_0 = sdrplay.rsp1_source(435.1e6, 1536, True, 40, False, False,
                False, 0, 1, samp_rate, True, '0')
            
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(25, (1, ))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vcc((beacon, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((0.26, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((20, ))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_tcp_sink_1 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr='127.0.0.1',
        	port=8011,
        	server=False,
        )
        self.audio_source_0 = audio.source(44100, 'plughw:0,1', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate_Baseband, analog.GR_COS_WAVE, -25100, 0.8, 0)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=44100,
        	quad_rate=samp_rate_Baseband,
        	tau=75e-6,
        	max_dev=2.6e3,
        	fh=-1.0,
                )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blks2_tcp_sink_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_3, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.sdrplay_rsp1_source_0, 0), (self.fir_filter_xxx_0, 0))    

    def get_samp_rate_Baseband(self):
        return self.samp_rate_Baseband

    def set_samp_rate_Baseband(self, samp_rate_Baseband):
        self.samp_rate_Baseband = samp_rate_Baseband
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate_Baseband)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_beacon(self):
        return self.beacon

    def set_beacon(self, beacon):
        self.beacon = beacon
        self.blocks_multiply_const_vxx_3.set_k((self.beacon, ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
