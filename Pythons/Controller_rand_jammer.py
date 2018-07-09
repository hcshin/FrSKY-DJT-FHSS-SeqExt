#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Rand Jammer
# Generated: Fri Nov  7 15:12:26 2014
##################################################

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time
import datetime as dt
import random

class rand_jammer(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Rand Jammer")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.curr_chann_idx = 0

        ##################################################
        # Blocks
        ##################################################
        self.analog_noise_source = analog.noise_source_c(analog.GR_GAUSSIAN, 1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.30.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_gain(31.5, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        #self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        #self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.analog_noise_source, 0), (self.uhd_usrp_sink_0, 0))



    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        
def frequency_table(chann_num):
    frequency_table = (2.40517,2.40668,2.40816,2.40965,2.41115,2.41268,2.41418,2.41567,2.41718,2.41866,2.42017,2.42167,2.42318,2.42469,2.42616,2.42768,2.42913,2.43064,2.43216,2.43365,2.43514,2.43665,2.43818,2.43967,2.44113,2.44263,2.44414,2.44563,2.44715,2.44866,2.45013,2.45163,2.45318,2.45463,2.45613,2.45767,2.45915,2.46062,2.46217,2.46365,2.46513,2.46663,2.46812,2.46965,2.47115,2.47266,2.47415)
    return frequency_table[chann_num -1] * 1e9

def log_elapsed(log, desc, start):
    end = dt.datetime.now()
    log.write(str(desc) + ' @ %f sec\n' % ((end - start).seconds + ((end - start).microseconds)/1e6))

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()

    inception = dt.datetime.now()
    log = open('../Sample/ramdisk/Log_rand_jammer.txt', 'w')

    tb = rand_jammer()
    tb.curr_chann_idx = random.randrange(0, 46, 1)
    log_elapsed(log, 'new channel: %d' % (tb.curr_chann_idx + 1), inception)
    tb.uhd_usrp_sink_0.set_center_freq(frequency_table(tb.curr_chann_idx))
    while not tb.uhd_usrp_sink_0.get_sensor('lo_locked').to_bool():
        pass
    log_elapsed(log, 'lo_locked!', inception)

    tb.start()

    time.sleep(5)
    log_elapsed(log, 'Waited 5sec', inception)

    while 1:
        tb.curr_chann_idx = random.randrange(0, 47, 1)
        log_elapsed(log, 'new channel: %d' % (tb.curr_chann_idx + 1), inception)
        tb.uhd_usrp_sink_0.set_center_freq(frequency_table(tb.curr_chann_idx))
        while not tb.uhd_usrp_sink_0.get_sensor('lo_locked').to_bool():
            pass
        log_elapsed(log, 'lo_locked!', inception)
        time.sleep(0.0058)

    raw_input('Press Enter to quit: ')
    log.close()
    tb.stop()
    tb.wait()
