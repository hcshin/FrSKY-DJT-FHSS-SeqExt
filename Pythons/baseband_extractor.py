#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Baseband Extractor
# Generated: Sun Dec 14 13:46:35 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class baseband_extractor(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Baseband Extractor")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/2,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.30.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(2.44263e9, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 1.5e6, 0.2e6, firdes.WIN_BLACKMAN, 6.76))
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/hocheol/GRC/Sample/ramdisk1/Baseband.cfloat", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_pll_carriertracking_cc_0 = analog.pll_carriertracking_cc(200.0/3.14, 0.5, -0.5)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_pll_carriertracking_cc_0, 0))
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.blocks_file_sink_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate/2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 1.5e6, 0.2e6, firdes.WIN_BLACKMAN, 6.76))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = baseband_extractor()
    tb.Start(True)
    tb.Wait()
