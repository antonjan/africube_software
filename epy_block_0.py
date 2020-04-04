"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
#import tkinter as tk
import sys
from subprocess import Popen, PIPE
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, gain=1.0,threshold=0.0,example_param=1.0,exe_param="while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 88200 -f 145960 "):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Display Message',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param
        self.gain = gain
        self.threshold = threshold
        self.exe_param = exe_param

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = input_items[0] * self.example_param
        print "length of input_items = ", len(input_items[0])
        print "length of output_items = ", len(output_items[0])
        proc = Popen('while true; do (nc -l 8011; dd if=/dev/zero bs=4096 count=30); done | sudo rpitx -i- -m IQFLOAT -s 88200 -f 145960', stdout=PIPE, shell=True)
       
        return len(output_items[0])
