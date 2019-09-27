#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Linear Transponder
# Author: Anton JAnovsky
# Description: Satellite Linear Transponder
# Generated: Fri Sep 27 07:15:34 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Linear Transponder")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_slider_5 = variable_slider_5 = 50
        self.variable_slider_4 = variable_slider_4 = 50
        self.variable_slider_3 = variable_slider_3 = 50
        self.variable_slider_2 = variable_slider_2 = 50
        self.variable_slider_1 = variable_slider_1 = 50
        self.variable_slider_0 = variable_slider_0 = 50
        self.tx_freq = tx_freq = 438.1e6
        self.samp_rate = samp_rate = 2e6
        self.rx_freq = rx_freq = 145.3e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=80000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        _variable_slider_5_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_5_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_5_sizer,
        	value=self.variable_slider_5,
        	callback=self.set_variable_slider_5,
        	label='variable_slider_5',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_5_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_5_sizer,
        	value=self.variable_slider_5,
        	callback=self.set_variable_slider_5,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_5_sizer)
        _variable_slider_4_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_4_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_4_sizer,
        	value=self.variable_slider_4,
        	callback=self.set_variable_slider_4,
        	label='variable_slider_4',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_4_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_4_sizer,
        	value=self.variable_slider_4,
        	callback=self.set_variable_slider_4,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_4_sizer)
        _variable_slider_3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_3_sizer,
        	value=self.variable_slider_3,
        	callback=self.set_variable_slider_3,
        	label='variable_slider_3',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_3_sizer,
        	value=self.variable_slider_3,
        	callback=self.set_variable_slider_3,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_3_sizer)
        _variable_slider_2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_2_sizer,
        	value=self.variable_slider_2,
        	callback=self.set_variable_slider_2,
        	label='variable_slider_2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_2_sizer,
        	value=self.variable_slider_2,
        	callback=self.set_variable_slider_2,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_2_sizer)
        _variable_slider_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	label='variable_slider_1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_1_sizer,
        	value=self.variable_slider_1,
        	callback=self.set_variable_slider_1,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_1_sizer)
        _variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	label='variable_slider_0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_sizer)
        _tx_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tx_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tx_freq_sizer,
        	value=self.tx_freq,
        	callback=self.set_tx_freq,
        	label='TX Freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tx_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tx_freq_sizer,
        	value=self.tx_freq,
        	callback=self.set_tx_freq,
        	minimum=430e6,
        	maximum=440e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tx_freq_sizer)
        _rx_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rx_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rx_freq_sizer,
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	label='RX Freq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rx_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rx_freq_sizer,
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	minimum=144e6,
        	maximum=146e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_rx_freq_sizer)
        self.osmosdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + 'miri=0' )
        self.osmosdr_source_1.set_sample_rate(samp_rate)
        self.osmosdr_source_1.set_center_freq(438.100e6, 0)
        self.osmosdr_source_1.set_freq_corr(0, 0)
        self.osmosdr_source_1.set_dc_offset_mode(0, 0)
        self.osmosdr_source_1.set_iq_balance_mode(0, 0)
        self.osmosdr_source_1.set_gain_mode(False, 0)
        self.osmosdr_source_1.set_gain(1, 0)
        self.osmosdr_source_1.set_if_gain(1, 0)
        self.osmosdr_source_1.set_bb_gain(1, 0)
        self.osmosdr_source_1.set_antenna('', 0)
        self.osmosdr_source_1.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(25, firdes.low_pass(
        	1, samp_rate, 80000, 10000, firdes.WIN_HAMMING, 6.76))
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.osmosdr_source_1, 0), (self.low_pass_filter_0, 0))    

    def get_variable_slider_5(self):
        return self.variable_slider_5

    def set_variable_slider_5(self, variable_slider_5):
        self.variable_slider_5 = variable_slider_5
        self._variable_slider_5_slider.set_value(self.variable_slider_5)
        self._variable_slider_5_text_box.set_value(self.variable_slider_5)

    def get_variable_slider_4(self):
        return self.variable_slider_4

    def set_variable_slider_4(self, variable_slider_4):
        self.variable_slider_4 = variable_slider_4
        self._variable_slider_4_slider.set_value(self.variable_slider_4)
        self._variable_slider_4_text_box.set_value(self.variable_slider_4)

    def get_variable_slider_3(self):
        return self.variable_slider_3

    def set_variable_slider_3(self, variable_slider_3):
        self.variable_slider_3 = variable_slider_3
        self._variable_slider_3_slider.set_value(self.variable_slider_3)
        self._variable_slider_3_text_box.set_value(self.variable_slider_3)

    def get_variable_slider_2(self):
        return self.variable_slider_2

    def set_variable_slider_2(self, variable_slider_2):
        self.variable_slider_2 = variable_slider_2
        self._variable_slider_2_slider.set_value(self.variable_slider_2)
        self._variable_slider_2_text_box.set_value(self.variable_slider_2)

    def get_variable_slider_1(self):
        return self.variable_slider_1

    def set_variable_slider_1(self, variable_slider_1):
        self.variable_slider_1 = variable_slider_1
        self._variable_slider_1_slider.set_value(self.variable_slider_1)
        self._variable_slider_1_text_box.set_value(self.variable_slider_1)

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self._variable_slider_0_slider.set_value(self.variable_slider_0)
        self._variable_slider_0_text_box.set_value(self.variable_slider_0)

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        self._tx_freq_slider.set_value(self.tx_freq)
        self._tx_freq_text_box.set_value(self.tx_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_source_1.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 80000, 10000, firdes.WIN_HAMMING, 6.76))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self._rx_freq_slider.set_value(self.rx_freq)
        self._rx_freq_text_box.set_value(self.rx_freq)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
