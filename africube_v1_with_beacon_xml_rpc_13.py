#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Test Rpitx
# Author: root
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import rpitx
import soapy
import distutils
from distutils import util
try:
    from xmlrpc.server import SimpleXMLRPCServer
except ImportError:
    from SimpleXMLRPCServer import SimpleXMLRPCServer
import threading

from gnuradio import qtgui

class africube_v1_with_beacon_xml_rpc_13(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Test Rpitx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test Rpitx")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "africube_v1_with_beacon_xml_rpc_13")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000*2
        self.command_trans_witdth_freq = command_trans_witdth_freq = 2000
        self.command_taps_cutoff_freq = command_taps_cutoff_freq = 12000
        self.variable_qtgui_range_1 = variable_qtgui_range_1 = 5000
        self.variable_low_pass_filter_taps = variable_low_pass_filter_taps = firdes.low_pass(1.0, samp_rate, command_taps_cutoff_freq,command_trans_witdth_freq, firdes.WIN_HAMMING, 6.76)
        self.tran_tx_freq = tran_tx_freq = 145970000
        self.sdrplay_rx_gain = sdrplay_rx_gain = 10
        self.samp_rate_0 = samp_rate_0 = 1248000
        self.rx_freq = rx_freq = 435100000
        self.lpf_cutoff_freq = lpf_cutoff_freq = 20000
        self.low_pass_filter_gain = low_pass_filter_gain = 1
        self.command_freq_ofset = command_freq_ofset = -35e3
        self.command_costas_loop_order = command_costas_loop_order = 2
        self.command_costas_loop_bw = command_costas_loop_bw = 10000
        self.command_agc_ref = command_agc_ref = 1
        self.command_agc_rate = command_agc_rate = 1e-4
        self.command_agc_max_gain = command_agc_max_gain = 5
        self.command_agc_gain = command_agc_gain = 1
        self.beacon_tau = beacon_tau = 75e-6
        self.beacon_offset_freq = beacon_offset_freq = -24800
        self.beacon_offset = beacon_offset = 0
        self.beacon_int_phase = beacon_int_phase = 0
        self.beacon_deviation = beacon_deviation = 2.5e3
        self.beacon_bpf_low_cutoff = beacon_bpf_low_cutoff = 21000
        self.beacon_bpf_high_cutoff = beacon_bpf_high_cutoff = 31000
        self.beacon_Preemphasis = beacon_Preemphasis = -1
        self.SDR_rf_gain = SDR_rf_gain = 1
        self.LPF_rf_gain_0 = LPF_rf_gain_0 = 9
        self.Beacon_mod_gain = Beacon_mod_gain = 0.8
        self.Beacom_overall_gain = Beacom_overall_gain = 0.8
        self.Beacom_mixer_gain = Beacom_mixer_gain = 0.8

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_1_range = Range(1000, 25000, 1, 5000, 200)
        self._variable_qtgui_range_1_win = RangeWidget(self._variable_qtgui_range_1_range, self.set_variable_qtgui_range_1, 'deviastion', "counter_slider", float)
        self.top_grid_layout.addWidget(self._variable_qtgui_range_1_win)
        self.xmlrpc_server_0 = SimpleXMLRPCServer(('127.0.0.1', 8008), allow_none=True)
        self.xmlrpc_server_0.register_instance(self)
        self.xmlrpc_server_0_thread = threading.Thread(target=self.xmlrpc_server_0.serve_forever)
        self.xmlrpc_server_0_thread.daemon = True
        self.xmlrpc_server_0_thread.start()
        self.soapy_source_0 = None
        # Make sure that the gain mode is valid
        if('Overall' not in ['Overall', 'Specific', 'Settings Field']):
            raise ValueError("Wrong gain mode on channel 0. Allowed gain modes: "
                  "['Overall', 'Specific', 'Settings Field']")

        dev = 'driver=sdrplay'

        # Stream arguments for every activated stream
        tune_args = ['']
        settings = ['']

        # Setup the device arguments
        dev_args = 'driver=sdrplay'

        self.soapy_source_0 = soapy.source(1, dev, dev_args, '',
                                  tune_args, settings, samp_rate, "fc32")



        self.soapy_source_0.set_dc_removal(0,bool(distutils.util.strtobool('False')))

        # Set up DC offset. If set to (0, 0) internally the source block
        # will handle the case if no DC offset correction is supported
        self.soapy_source_0.set_dc_offset(0,0)

        # Setup IQ Balance. If set to (0, 0) internally the source block
        # will handle the case if no IQ balance correction is supported
        self.soapy_source_0.set_iq_balance(0,0)

        self.soapy_source_0.set_agc(0,False)

        # generic frequency setting should be specified first
        self.soapy_source_0.set_frequency(0, rx_freq)

        self.soapy_source_0.set_frequency(0,"BB",0)

        # Setup Frequency correction. If set to 0 internally the source block
        # will handle the case if no frequency correction is supported
        self.soapy_source_0.set_frequency_correction(0,0)

        self.soapy_source_0.set_antenna(0,'RX')

        self.soapy_source_0.set_bandwidth(0,0)

        if('Overall' != 'Settings Field'):
            # pass is needed, in case the template does not evaluare anything
            pass
            self.soapy_source_0.set_gain(0,SDR_rf_gain)
        self.rpitx_rpitx_source_0 = rpitx.rpitx_source(samp_rate, tran_tx_freq)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            48000, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                LPF_rf_gain_0,
                samp_rate,
                lpf_cutoff_freq,
                samp_rate/32,
                firdes.WIN_HAMMING,
                6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, variable_low_pass_filter_taps, command_freq_ofset, samp_rate)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(command_costas_loop_bw, command_costas_loop_order, False)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(Beacom_overall_gain)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(Beacon_mod_gain)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.band_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                beacon_bpf_low_cutoff,
                beacon_bpf_high_cutoff,
                samp_rate/32,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_source_0 = audio.source(48000, 'hw:2,1,0', True)
        self.audio_sink_0 = audio.sink(48000, 'hw:2,0,1', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, beacon_offset_freq, Beacom_mixer_gain, beacon_offset, beacon_int_phase)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=48000,
        	quad_rate=samp_rate,
        	tau=beacon_tau,
        	max_dev=beacon_deviation,
        	fh=beacon_Preemphasis,
                )
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=48000,
        	quad_rate=96000,
        	tau=75e-6,
        	max_dev=variable_qtgui_range_1,
          )
        self.analog_agc_xx_0 = analog.agc_cc(command_agc_rate, command_agc_ref, command_agc_gain)
        self.analog_agc_xx_0.set_max_gain(command_agc_max_gain)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.analog_agc_xx_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.analog_nbfm_rx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.audio_source_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.rpitx_rpitx_source_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.soapy_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.soapy_source_0, 0), (self.low_pass_filter_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "africube_v1_with_beacon_xml_rpc_13")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.beacon_bpf_low_cutoff, self.beacon_bpf_high_cutoff, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.LPF_rf_gain_0, self.samp_rate, self.lpf_cutoff_freq, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_command_trans_witdth_freq(self):
        return self.command_trans_witdth_freq

    def set_command_trans_witdth_freq(self, command_trans_witdth_freq):
        self.command_trans_witdth_freq = command_trans_witdth_freq

    def get_command_taps_cutoff_freq(self):
        return self.command_taps_cutoff_freq

    def set_command_taps_cutoff_freq(self, command_taps_cutoff_freq):
        self.command_taps_cutoff_freq = command_taps_cutoff_freq

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1
        self.analog_nbfm_rx_0.set_max_deviation(self.variable_qtgui_range_1)

    def get_variable_low_pass_filter_taps(self):
        return self.variable_low_pass_filter_taps

    def set_variable_low_pass_filter_taps(self, variable_low_pass_filter_taps):
        self.variable_low_pass_filter_taps = variable_low_pass_filter_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps(self.variable_low_pass_filter_taps)

    def get_tran_tx_freq(self):
        return self.tran_tx_freq

    def set_tran_tx_freq(self, tran_tx_freq):
        self.tran_tx_freq = tran_tx_freq
        self.rpitx_rpitx_source_0.set_freq(self.tran_tx_freq)

    def get_sdrplay_rx_gain(self):
        return self.sdrplay_rx_gain

    def set_sdrplay_rx_gain(self, sdrplay_rx_gain):
        self.sdrplay_rx_gain = sdrplay_rx_gain

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.soapy_source_0.set_frequency(0, self.rx_freq)

    def get_lpf_cutoff_freq(self):
        return self.lpf_cutoff_freq

    def set_lpf_cutoff_freq(self, lpf_cutoff_freq):
        self.lpf_cutoff_freq = lpf_cutoff_freq
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.LPF_rf_gain_0, self.samp_rate, self.lpf_cutoff_freq, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))

    def get_low_pass_filter_gain(self):
        return self.low_pass_filter_gain

    def set_low_pass_filter_gain(self, low_pass_filter_gain):
        self.low_pass_filter_gain = low_pass_filter_gain

    def get_command_freq_ofset(self):
        return self.command_freq_ofset

    def set_command_freq_ofset(self, command_freq_ofset):
        self.command_freq_ofset = command_freq_ofset
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.command_freq_ofset)

    def get_command_costas_loop_order(self):
        return self.command_costas_loop_order

    def set_command_costas_loop_order(self, command_costas_loop_order):
        self.command_costas_loop_order = command_costas_loop_order

    def get_command_costas_loop_bw(self):
        return self.command_costas_loop_bw

    def set_command_costas_loop_bw(self, command_costas_loop_bw):
        self.command_costas_loop_bw = command_costas_loop_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.command_costas_loop_bw)

    def get_command_agc_ref(self):
        return self.command_agc_ref

    def set_command_agc_ref(self, command_agc_ref):
        self.command_agc_ref = command_agc_ref
        self.analog_agc_xx_0.set_reference(self.command_agc_ref)

    def get_command_agc_rate(self):
        return self.command_agc_rate

    def set_command_agc_rate(self, command_agc_rate):
        self.command_agc_rate = command_agc_rate
        self.analog_agc_xx_0.set_rate(self.command_agc_rate)

    def get_command_agc_max_gain(self):
        return self.command_agc_max_gain

    def set_command_agc_max_gain(self, command_agc_max_gain):
        self.command_agc_max_gain = command_agc_max_gain
        self.analog_agc_xx_0.set_max_gain(self.command_agc_max_gain)

    def get_command_agc_gain(self):
        return self.command_agc_gain

    def set_command_agc_gain(self, command_agc_gain):
        self.command_agc_gain = command_agc_gain
        self.analog_agc_xx_0.set_gain(self.command_agc_gain)

    def get_beacon_tau(self):
        return self.beacon_tau

    def set_beacon_tau(self, beacon_tau):
        self.beacon_tau = beacon_tau

    def get_beacon_offset_freq(self):
        return self.beacon_offset_freq

    def set_beacon_offset_freq(self, beacon_offset_freq):
        self.beacon_offset_freq = beacon_offset_freq
        self.analog_sig_source_x_0.set_frequency(self.beacon_offset_freq)

    def get_beacon_offset(self):
        return self.beacon_offset

    def set_beacon_offset(self, beacon_offset):
        self.beacon_offset = beacon_offset
        self.analog_sig_source_x_0.set_offset(self.beacon_offset)

    def get_beacon_int_phase(self):
        return self.beacon_int_phase

    def set_beacon_int_phase(self, beacon_int_phase):
        self.beacon_int_phase = beacon_int_phase
        self.analog_sig_source_x_0.set_phase(self.beacon_int_phase)

    def get_beacon_deviation(self):
        return self.beacon_deviation

    def set_beacon_deviation(self, beacon_deviation):
        self.beacon_deviation = beacon_deviation
        self.analog_nbfm_tx_0.set_max_deviation(self.beacon_deviation)

    def get_beacon_bpf_low_cutoff(self):
        return self.beacon_bpf_low_cutoff

    def set_beacon_bpf_low_cutoff(self, beacon_bpf_low_cutoff):
        self.beacon_bpf_low_cutoff = beacon_bpf_low_cutoff
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.beacon_bpf_low_cutoff, self.beacon_bpf_high_cutoff, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))

    def get_beacon_bpf_high_cutoff(self):
        return self.beacon_bpf_high_cutoff

    def set_beacon_bpf_high_cutoff(self, beacon_bpf_high_cutoff):
        self.beacon_bpf_high_cutoff = beacon_bpf_high_cutoff
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.beacon_bpf_low_cutoff, self.beacon_bpf_high_cutoff, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))

    def get_beacon_Preemphasis(self):
        return self.beacon_Preemphasis

    def set_beacon_Preemphasis(self, beacon_Preemphasis):
        self.beacon_Preemphasis = beacon_Preemphasis

    def get_SDR_rf_gain(self):
        return self.SDR_rf_gain

    def set_SDR_rf_gain(self, SDR_rf_gain):
        self.SDR_rf_gain = SDR_rf_gain
        self.soapy_source_0.set_gain(0, self.SDR_rf_gain)

    def get_LPF_rf_gain_0(self):
        return self.LPF_rf_gain_0

    def set_LPF_rf_gain_0(self, LPF_rf_gain_0):
        self.LPF_rf_gain_0 = LPF_rf_gain_0
        self.low_pass_filter_0.set_taps(firdes.low_pass(self.LPF_rf_gain_0, self.samp_rate, self.lpf_cutoff_freq, self.samp_rate/32, firdes.WIN_HAMMING, 6.76))

    def get_Beacon_mod_gain(self):
        return self.Beacon_mod_gain

    def set_Beacon_mod_gain(self, Beacon_mod_gain):
        self.Beacon_mod_gain = Beacon_mod_gain
        self.blocks_multiply_const_vxx_0.set_k(self.Beacon_mod_gain)

    def get_Beacom_overall_gain(self):
        return self.Beacom_overall_gain

    def set_Beacom_overall_gain(self, Beacom_overall_gain):
        self.Beacom_overall_gain = Beacom_overall_gain
        self.blocks_multiply_const_vxx_0_0.set_k(self.Beacom_overall_gain)

    def get_Beacom_mixer_gain(self):
        return self.Beacom_mixer_gain

    def set_Beacom_mixer_gain(self, Beacom_mixer_gain):
        self.Beacom_mixer_gain = Beacom_mixer_gain
        self.analog_sig_source_x_0.set_amplitude(self.Beacom_mixer_gain)





def main(top_block_cls=africube_v1_with_beacon_xml_rpc_13, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
