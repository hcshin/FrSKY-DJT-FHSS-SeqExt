#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Test2
# Generated: Wed Feb 12 16:57:35 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from grc_gnuradio import blks2 as grc_blks2
import threading
import time
import datetime as dt
import math
import wx
from gnuradio import wxgui
from grc_gnuradio import wxgui as grc_wxgui
from gnuradio.wxgui import scopesink2

class Follow_with_single_usrp(grc_wxgui.top_block_gui):

    def __init__(self, FH_seq):
        #gr.top_block.__init__(self, "Test2")
        grc_wxgui.top_block_gui.__init__(self, title="Follow_with_single_usrp")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sql_on = sql_on = 0
        self.samp_rate = samp_rate = 2e6
        self.curr_chann_idx = 0
        self.FH_seq = FH_seq
        self.inception = 0

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
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
        self.analog_pwr_squelch_xx_1 = analog.pwr_squelch_cc(-40, 1, 25, False)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="addr=192.168.30.2",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(2.43064e9, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        def _sql_on_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_1.unmuted()
        		try: self.set_sql_on(val)
        		except AttributeError, e: pass
        		time.sleep((0.001))
        _sql_on_thread = threading.Thread(target=_sql_on_probe)
        _sql_on_thread.daemon = True
        _sql_on_thread.start()
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, (2.337093355240479e-18, 0.001956143882125616, -0.004504681099206209, 0.005366003606468439, -9.056237216845951e-18, -0.01352460216730833, 0.028625724837183952, -0.029645023867487907, 2.2494524940056896e-17, 0.06486776471138, -0.1492309421300888, 0.22137974202632904, 0.7494196891784668, 0.22137974202632904, -0.1492309421300888, 0.06486776471138, 2.2494524940056896e-17, -0.029645023867487907, 0.028625724837183952, -0.01352460216730833, -9.056237216845951e-18, 0.005366003606468439, -0.004504681099206209, 0.001956143882125616, 2.337093355240479e-18))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        #self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/hocheol/GRC/Sample/ramdisk/rcvd.cfloat", False)
        #self.blocks_file_sink_0.set_unbuffered(True)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=0,
        )
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.analog_pwr_squelch_xx_1, 0))
        self.connect((self.analog_pwr_squelch_xx_1, 0), (self.blks2_selector_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blks2_selector_0, 1), (self.wxgui_scopesink2_0, 0))

# QT sink close method reimplementation

    def get_sql_on(self):
        return self.sql_on

    def set_sql_on(self, sql_on):
        self.sql_on = sql_on

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def set_usrp_freq(self):
        self.uhd_usrp_source_0.set_center_freq(frequency_table(self.FH_seq[self.curr_chann_idx]))
        while not self.uhd_usrp_source_0.get_sensor('lo_locked').to_bool():
            pass
        print_elapsed('lo_locked!', inception)

    def follow(self):
        print_elapsed('Entered self.follow()', inception)
        if self.curr_chann_idx == len(self.FH_seq) - 1:
            self.curr_chann_idx = 0
            self.set_usrp_freq()
            print_elapsed(['curr chann', self.FH_seq[self.curr_chann_idx]], inception)
            print_elapsed(['usrp: center freq is changed to', tb.uhd_usrp_source_0.get_center_freq()], inception)
        else:
            self.curr_chann_idx += 1
            self.set_usrp_freq()
            print_elapsed(['curr chann', self.FH_seq[self.curr_chann_idx]], inception)
            print_elapsed(['usrp: center freq is changed to', tb.uhd_usrp_source_0.get_center_freq()], inception)
        while not self.get_sql_on():
            time.sleep(0.0005)
        print_elapsed('Squelch is back on, restarting', inception)
    
    def initialize(self):
        self.uhd_usrp_source_0.set_center_freq(frequency_table(self.FH_seq[self.curr_chann_idx]))
        print_elapsed(['Initial center freq: chann', self.uhd_usrp_source_0.get_center_freq()], inception)
        print self.uhd_usrp_source_0.get_sensor_names()

    def Control(self):
        self.inception = dt.datetime.now()
        
        print_elapsed('Flowgraph started', self.inception)
        time.sleep(5)
        print_elapsed('Waited 5sec', self.inception)

        self.catch_seq()
        self.blks2_selector_0.set_output_index(1)
        print_elapsed('Start Transmitting to wxgui scope...', inception)

        while 1:
            print_elapsed('Squelch State: %s' % tb.get_sql_on(), inception)
            if tb.get_sql_on():
                print_elapsed('Stayed on the Channel', inception)
                time.sleep(0.0005)
            else:
                print ''
                tb.follow()
                print_elapsed('Hop ordered', inception)

    def catch_seq(self):
        break_flag = False
        while 1:
            while not self.get_sql_on():
                time.sleep(0.0005)
            print_elapsed('Activeness captured', inception)
            print_elapsed('curr chann: %d' % self.FH_seq[self.curr_chann_idx], inception)
            print_elapsed('Initial center freq: %f' % self.uhd_usrp_source_0.get_center_freq(), inception)
            print ''

            while self.get_sql_on():
                time.sleep(0.0005)

            print_elapsed('First channel deactivated', inception)
            self.curr_chann_idx += 1
            self.set_usrp_freq()
            print_elapsed('curr chann: %d' % self.FH_seq[self.curr_chann_idx], inception)
            print_elapsed('center freq is changed to: %f' % self.uhd_usrp_source_0.get_center_freq(), inception)
            print ''
            
            cnt = 0
            while  cnt < 8:
                time.sleep(0.0005)
                cnt += 1
                if self.get_sql_on():
                    break_flag = True
                    break
            if break_flag is not True:
                print_elapsed('Waited the second sequence for 4msec. No activity. Resetting.', inception)
                self.curr_chann_idx -= 1
                self.set_usrp_freq()
                print_elapsed('center freq is changed to: %f' % self.uhd_usrp_source_0.get_center_freq(), inception)
                print''
                continue
            
            break_flag = False
            print_elapsed('Second Sequence caught', inception)
            print_elapsed('curr chann: %d' % self.FH_seq[self.curr_chann_idx], inception)
            print_elapsed('center freq is changed to: %f' % self.uhd_usrp_source_0.get_center_freq(), inception)
            print''

            while self.get_sql_on():
                time.sleep(0.0005)
            print_elapsed('Second channel deactivated', inception)
            self.curr_chann_idx += 1
            self.set_usrp_freq()
            print_elapsed('curr chann: %d' % self.FH_seq[self.curr_chann_idx], inception)
            print_elapsed('center freq is changed to: %f' % self.uhd_usrp_source_0.get_center_freq(), inception)
            print ''
            
            cnt = 0
            while  cnt < 8:
                time.sleep(0.0005)
                cnt += 1
                if self.get_sql_on():
                    break_flag = True
                    break
            if break_flag is not True:
                print_elapsed('Waited the last sequence for 4msec. No activity. Resetting.', inception)
                self.curr_chann_idx -= 2
                self.set_usrp_freq()
                print_elapsed('center freq is changed to: %f' % self.uhd_usrp_source_0.get_center_freq(), inception)
                print ''
            else:
                print_elapsed('Last channel caught. Getting on the sequence', inception)
                print_elapsed('curr chann: %d' % self.FH_seq[self.curr_chann_idx], inception)
                print_elapsed('center freq is changed to: %f' % self.uhd_usrp_source_0.get_center_freq(), inception)
                print ''
                break

        

#Global functions
def print_elapsed(desc, start):
    end = dt.datetime.now()
    print str(desc) + ': %f sec\n' % ((end - start).seconds + ((end - start).microseconds)/1e6)

def frequency_table(chann_num):
    frequency_table = (2.40517,2.40668,2.40816,2.40965,2.41115,2.41268,2.41418,2.41567,2.41718,2.41866,2.42017,2.42167,2.42318,2.42469,2.42616,2.42768,2.42913,2.43064,2.43216,2.43365,2.43514,2.43665,2.43818,2.43967,2.44113,2.44263,2.44414,2.44563,2.44715,2.44866,2.45013,2.45163,2.45318,2.45463,2.45613,2.45767,2.45915,2.46062,2.46217,2.46365,2.46513,2.46663,2.46812,2.46965,2.47115,2.47266,2.47415)
    return frequency_table[chann_num - 1] * 1e9



if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    
    inception = dt.datetime.now()
    sequence = (29,23,17,5,46,40,28,22,16,4,45,39,27,21,15,3,44,38,26,20,14,2,43,37,25,19,13,1,42,36,24,18,12,47,41,35,23,17,11,46,40,34,22,16,10,45,39,33,21,15,9,44,38,32,20,14,8,43,37,31,19,13,7,42,36,30,18,12,6,41,35,29,17,11,5,40,34,28,16,10,4,39,33,27,15,9,3,38,32,26,14,8,2,37,31,25,13,7,1,36,30,24,12,6,47,35,29,23,11,5,46,34,28,22,10,4,45,33,27,21,9,3,44,32,26,20,8,2,43,31,25,19,7,1,42,30,24,18,6,47,41)
    tb = Follow_with_single_usrp(sequence)
    tb.initialize()
    tb.Start()
    thread_Control = threading.Thread(target = tb.Control)
    thread_Control.daemon = True
    thread_Control.start()
    tb.Wait()
