#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Sequence Follower
# Generated: Fri Jan 10 21:46:10 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import threading
import time
import datetime as dt

class Sequence_Follower(gr.top_block):

    def __init__(self, FH_seq, start_chann_idx):
        gr.top_block.__init__(self, "Sequence Follower")

        ##################################################
        # Variables
        ##################################################
        self.sql_on = sql_on = 0
        self.samp_rate = samp_rate = 32000
        self.curr_chann_idx = start_chann_idx
        self.FH_seq = FH_seq 
        ##################################################
        # Blocks
        ##################################################
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-10, 1, 25, False)
        def _sql_on_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0.unmuted()
        		try: self.set_sql_on(val)
        		except AttributeError, e: pass
        		time.sleep(1.0/(100))
        _sql_on_thread = threading.Thread(target=_sql_on_probe)
        _sql_on_thread.daemon = True
        _sql_on_thread.start()
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccf(64, ( [0.0027054441161453724, 0.002875175094231963, 0.0033175654243677855, 0.004034834913909435, 0.005023509729653597, 0.006274390500038862, 0.007772639859467745, 0.009498009458184242, 0.011425167322158813, 0.013524158857762814, 0.015760963782668114, 0.01809815689921379, 0.020495640113949776, 0.02291143871843815, 0.025302572175860405, 0.027625905349850655, 0.02983906865119934, 0.03190131485462189, 0.03377437964081764, 0.035423289984464645, 0.03681709244847298, 0.03792952373623848, 0.038739532232284546, 0.03923177719116211, 0.039396900683641434, 0.03923177719116211, 0.038739532232284546, 0.03792952373623848, 0.03681709244847298, 0.035423289984464645, 0.03377437964081764, 0.03190131485462189, 0.02983906865119934, 0.027625905349850655, 0.025302572175860405, 0.02291143871843815, 0.020495640113949776, 0.01809815689921379, 0.015760963782668114, 0.013524158857762814, 0.011425167322158813, 0.009498009458184242, 0.007772639859467745, 0.006274390500038862, 0.005023509729653597, 0.004034834913909435, 0.0033175654243677855, 0.002875175094231963, 0.0027054441161453724]), 1000, samp_rate)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/hocheol/GRC/Sample/FHSS_Sig", True)

        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/hocheol/GRC/Sample/FHSS_Demodulated.cfloat", False)
        self.blocks_file_sink_0.set_unbuffered(True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_pwr_squelch_xx_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.blocks_file_sink_0, 0))

# QT sink close method reimplementation

    def get_sql_on(self):
        return self.sql_on

    def set_sql_on(self, sql_on):
        self.sql_on = sql_on

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
    
    def follow(self):
        print_elapsed('Entered self.follow()', inception)
        if not self.get_sql_on():
            if self.curr_chann_idx == len(self.FH_seq) - 1:
                self.curr_chann_idx = 0
                print_elapsed(['center freq was set as', self.freq_xlating_fir_filter_xxx_0.center_freq()], inception)
                self.freq_xlating_fir_filter_xxx_0.set_center_freq(1000*self.FH_seq[0])
                print_elapsed(['center freq is changed to', self.freq_xlating_fir_filter_xxx_0.center_freq()], inception)
                while not self.get_sql_on():
                    time.sleep(0.01)
                print_elapsed('Squelch is back on, restarting', inception)
            else:
                self.curr_chann_idx += 1
                print_elapsed(['center freq was set as', self.freq_xlating_fir_filter_xxx_0.center_freq()], inception)
                self.freq_xlating_fir_filter_xxx_0.set_center_freq(1000*self.FH_seq[self.curr_chann_idx])
                print_elapsed(['center freq is set as', self.freq_xlating_fir_filter_xxx_0.center_freq()], inception)
                while not self.get_sql_on():
                    time.sleep(0.01)
                print_elapsed('Squelch is back on, restarting', inception)


def print_elapsed(desc, start):
    end = dt.datetime.now()
    print desc, (end - start).seconds + ((end - start).microseconds)/1e6

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()

    inception = dt.datetime.now()
    tb = Sequence_Follower((1, 3, 2), 0)
    tb.start()
    print_elapsed('Flowgraph started', inception)
    
    while not tb.get_sql_on():
        pass

    print_elapsed('Activeness captured', inception)
    while 1:
        print_elapsed(['Squelch State', tb.get_sql_on()], inception)
        if tb.get_sql_on():
            print_elapsed('Stayed on the Channel', inception)
            time.sleep(0.01)
        else:
            tb.follow()
            print_elapsed('Hop ordered', inception)
            time.sleep(0.01)
