#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Africube
# Author: Anton Janovsky
# Generated: Thu May 21 20:27:07 2020
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sdrplay
import sip
import sys
import threading
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Africube")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Africube")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.fun_probe = fun_probe = 0
        self.variable_qtgui_range_1 = variable_qtgui_range_1 = -10
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = fun_probe
        self.samp_rate_Baseband = samp_rate_Baseband = 88200
        self.samp_rate = samp_rate = 2205000

        ##################################################
        # Blocks
        ##################################################
        self.probe = blocks.probe_signal_f()
        self._variable_qtgui_range_1_range = Range(-110, 30, 1, -10, 200)
        self._variable_qtgui_range_1_win = RangeWidget(self._variable_qtgui_range_1_range, self.set_variable_qtgui_range_1, 'Power level sq', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_1_win)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: x
        
        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Power level'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
          
        self.sdrplay_rsp1_source_0 = sdrplay.rsp1_source(435.1e6, 1536, True, 40, False, False,
                False, 0, 1, samp_rate, True, '0')
            
        self.qtgui_sink_x_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	88200, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_1.set_update_time(1.0/10)
        self._qtgui_sink_x_1_win = sip.wrapinstance(self.qtgui_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_1_win)
        
        self.qtgui_sink_x_1.enable_rf_freq(False)
        
        
          
        
        def _fun_probe_probe():
            while True:
                val = self.probe.level()
                try:
                    self.set_fun_probe(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _fun_probe_thread = threading.Thread(target=_fun_probe_probe)
        _fun_probe_thread.daemon = True
        _fun_probe_thread.start()
            
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(25, (1, ))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((0.2, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((20, ))
        self.blocks_copy_0 = blocks.copy(gr.sizeof_gr_complex*1)
        self.blocks_copy_0.set_enabled(True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_tcp_sink_1 = grc_blks2.tcp_sink(
        	itemsize=gr.sizeof_gr_complex*1,
        	addr='127.0.0.1',
        	port=8011,
        	server=False,
        )
        self.audio_source_0 = audio.source(44100, 'plughw:0,1', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate_Baseband, analog.GR_COS_WAVE, -22100, 1, 0)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=44100,
        	quad_rate=samp_rate_Baseband,
        	tau=75e-6,
        	max_dev=2.5e3,
        	fh=-1.0,
                )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_2, 0))    
        self.connect((self.audio_source_0, 0), (self.probe, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blks2_tcp_sink_1, 0))    
        self.connect((self.blocks_copy_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_copy_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_sink_x_1, 0))    
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.sdrplay_rsp1_source_0, 0), (self.fir_filter_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_fun_probe(self):
        return self.fun_probe

    def set_fun_probe(self, fun_probe):
        self.fun_probe = fun_probe
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.fun_probe))

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.variable_qtgui_label_0)))

    def get_samp_rate_Baseband(self):
        return self.samp_rate_Baseband

    def set_samp_rate_Baseband(self, samp_rate_Baseband):
        self.samp_rate_Baseband = samp_rate_Baseband
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate_Baseband)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
