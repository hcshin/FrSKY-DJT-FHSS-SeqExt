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
from sys import exit

class Follow_with_single_usrp(gr.top_block):

    def __init__(self, FH_seq):
        gr.top_block.__init__(self, "Test2")

        ##################################################
        # Variables
        ##################################################
        self.sql_on = sql_on = 0
        self.samp_rate = samp_rate = 2e6
        self.curr_chann_idx = 0
        self.FH_seq = FH_seq

        ##################################################
        # Blocks
        ##################################################
        #self.analog_noise_source = analog.noise_source_c(analog.GR_GAUSSIAN, 0)
        self.cosine_source = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)
        self.analog_pwr_squelch_xx_1 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	device_addr="addr=192.168.30.2",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec("A:0", 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(2.43665e9, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_sink = uhd.usrp_sink(
                device_addr = "addr=192.168.30.2",
                stream_args = uhd.stream_args(
                    cpu_format="fc32",
                    channels=range(1),
                ),
        )
        self.uhd_usrp_sink.set_subdev_spec("A:0", 0)
        self.uhd_usrp_sink.set_samp_rate(samp_rate)
        self.uhd_usrp_sink.set_center_freq(2.43665e9, 0)
        self.uhd_usrp_sink.set_gain(31.5, 0)
        self.uhd_usrp_sink.set_antenna("TX/RX", 0)
        def _sql_on_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_1.unmuted()
        		try: self.set_sql_on(val)
        		except AttributeError, e: pass
        		time.sleep((0.001))
        _sql_on_thread = threading.Thread(target=_sql_on_probe)
        _sql_on_thread.daemon = True
        _sql_on_thread.start()
        #self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, (2.337093355240479e-18, 0.001956143882125616, -0.004504681099206209, 0.005366003606468439, -9.056237216845951e-18, -0.01352460216730833, 0.028625724837183952, -0.029645023867487907, 2.2494524940056896e-17, 0.06486776471138, -0.1492309421300888, 0.22137974202632904, 0.7494196891784668, 0.22137974202632904, -0.1492309421300888, 0.06486776471138, 2.2494524940056896e-17, -0.029645023867487907, 0.028625724837183952, -0.01352460216730833, -9.056237216845951e-18, 0.005366003606468439, -0.004504681099206209, 0.001956143882125616, 2.337093355240479e-18))
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, firdes.low_pass(1, samp_rate, 750000, 1000000, firdes.WIN_HAMMING, 6.76))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.analog_pwr_squelch_xx_1, 0))
        self.connect((self.analog_pwr_squelch_xx_1, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.cosine_source, 0), (self.uhd_usrp_sink, 0))
        #self.connect((self.analog_noise_source, 0), (self.uhd_usrp_sink, 0))


# Class Members
    def get_sql_on(self):
        return self.sql_on

    def set_sql_on(self, sql_on):
        self.sql_on = sql_on

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def set_usrp_freq(self, rxtx):
        if rxtx == 'rx' or rxtx == 'RX':
            self.uhd_usrp_source_0.set_center_freq(frequency_table(self.FH_seq[self.curr_chann_idx]))
            while not self.uhd_usrp_source_0.get_sensor('lo_locked').to_bool():
                pass
            log_elapsed(self.log, 'lo_locked!', inception)
        elif rxtx == 'tx' or rxtx == 'TX':
            self.uhd_usrp_sink.set_center_freq(frequency_table(self.FH_seq[self.curr_chann_idx]))
            while not self.uhd_usrp_sink.get_sensor('lo_locked').to_bool():
                pass
            log_elapsed(self.log, 'lo_locked!', inception)
        else:
            print 'txrx value should be either ''tx'', ''TX'', ''rx'', ''RX'''
            raise ValueError
            exit(1)

    def rx_hop(self):
        log_elapsed(self.log, 'Entered self.rx_hop()', inception)
        if self.curr_chann_idx == len(self.FH_seq) - 1:
            self.curr_chann_idx = 0
            self.set_usrp_freq('rx')
            log_elapsed(self.log, 'curr chann %d' % self.FH_seq[self.curr_chann_idx], inception)
            log_elapsed(self.log, 'usrp: center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
            log_elapsed(self.log, 'usrp_TX: center freq is changed to %.4e' % tb.uhd_usrp_sink.get_center_freq(), inception)
        else:
            self.curr_chann_idx += 1
            self.set_usrp_freq('rx')
            log_elapsed(self.log, 'curr chann %d' % self.FH_seq[self.curr_chann_idx], inception)
            log_elapsed(self.log, 'usrp: center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
            log_elapsed(self.log, 'usrp_TX: center freq is changed to %.4e' % tb.uhd_usrp_sink.get_center_freq(), inception)

    def tx_hop(self):
        log_elapsed(self.log, 'Entered self.tx_hop()', inception)
        self.set_usrp_freq('tx')
        log_elapsed(self.log, 'curr chann %d' % self.FH_seq[self.curr_chann_idx], inception)
        log_elapsed(self.log, 'usrp: center freq is changed to %.4e' % tb.uhd_usrp_sink.get_center_freq(), inception)
        log_elapsed(self.log, 'usrp_TX: center freq is changed to %.4e' % tb.uhd_usrp_sink.get_center_freq(), inception)
        #while not self.get_sql_on():
        #    time.sleep(0.0005)
        #log_elapsed(self.log, 'Squelch is back on, restarting', inception)

    def initialize(self, log):
        self.log = log
        self.uhd_usrp_source_0.set_center_freq(frequency_table(self.FH_seq[self.curr_chann_idx]))
        log_elapsed(self.log, 'Initial center freq: %.4e' % self.uhd_usrp_source_0.get_center_freq(), inception)
        print self.uhd_usrp_source_0.get_sensor_names()
    
    def jam(self, onoff):
        if onoff:
            #self.analog_noise_source.set_amplitude(1)
            self.cosine_source.set_amplitude(1)
        else:
            #self.analog_noise_source.set_amplitude(0)
            self.cosine_source.set_amplitude(0)


#Global functions
def log_elapsed(log, desc, start):
    end = dt.datetime.now()
    log.write(str(desc) + ' @ %f sec\n' % ((end - start).seconds + ((end - start).microseconds)/1e6))

def print_elapsed(desc, start):
    end = dt.datetime.now()
    print str(desc) + ': %f sec\n' % ((end - start).seconds + ((end - start).microseconds)/1e6)

def frequency_table(chann_num):
    frequency_table = (2.40517,2.40668,2.40816,2.40965,2.41115,2.41268,2.41418,2.41567,2.41718,2.41866,2.42017,2.42167,2.42318,2.42469,2.42616,2.42768,2.42913,2.43064,2.43216,2.43365,2.43514,2.43665,2.43818,2.43967,2.44113,2.44263,2.44414,2.44563,2.44715,2.44866,2.45013,2.45163,2.45318,2.45463,2.45613,2.45767,2.45915,2.46062,2.46217,2.46365,2.46513,2.46663,2.46812,2.46965,2.47115,2.47266,2.47415)
    return frequency_table[chann_num -1] * 1e9

def catch_seq(tb):
    break_flag = False
    while 1:
        while not tb.get_sql_on():
            time.sleep(0.0005)
        log_elapsed(tb.log, 'Activeness captured', inception)
        log_elapsed(tb.log, 'curr chann %d' % tb.FH_seq[tb.curr_chann_idx], inception)
        log_elapsed(tb.log, 'Initial center freq %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
        tb.log.write('\n')

        #while tb.get_sql_on():
        #    time.sleep(0.0005)

        #log_elapsed(tb.log, 'First channel deactivated', inception)
        tb.curr_chann_idx += 1
        tb.set_usrp_freq('rx')
        log_elapsed(tb.log, 'curr chann %d' % tb.FH_seq[tb.curr_chann_idx], inception)
        log_elapsed(tb.log, 'center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
        tb.log.write('\n')
        
        cnt = 0
        while  cnt < 20:
            time.sleep(0.0005)
            cnt += 1
            if tb.get_sql_on():
                break_flag = True
                break
        if break_flag is not True:
            log_elapsed(tb.log, 'Waited the second sequence for 10msec. No activity. Resetting.', inception)
            tb.curr_chann_idx -= 1
            tb.set_usrp_freq('rx')
            log_elapsed(tb.log, 'center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
            tb.log.write('\n')
            continue
        
        break_flag = False
        log_elapsed(tb.log, 'Second Sequence caught', inception)
        log_elapsed(tb.log, 'curr chann %d' % tb.FH_seq[tb.curr_chann_idx], inception)
        log_elapsed(tb.log, 'center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
        print''
        tb.log.write('\n')

        #while tb.get_sql_on():
        #    time.sleep(0.0005)
        #log_elapsed(tb.log, 'Second channel deactivated', inception)
        tb.curr_chann_idx += 1
        tb.set_usrp_freq('rx')
        log_elapsed(tb.log, 'curr chann %d' % tb.FH_seq[tb.curr_chann_idx], inception)
        log_elapsed(tb.log, 'center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
        tb.log.write('\n')
        
        cnt = 0
        while  cnt < 20:
            time.sleep(0.0005)
            cnt += 1
            if tb.get_sql_on():
                break_flag = True
                break
        if break_flag is not True:
            log_elapsed(tb.log, 'Waited the last sequence for 10msec. No activity. Resetting.', inception)
            tb.curr_chann_idx -= 2
            tb.set_usrp_freq('rx')
            log_elapsed(tb.log, 'center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
            tb.log.write('\n')
        else:
            log_elapsed(tb.log, 'Last channel caught. Getting on the sequence', inception)
            log_elapsed(tb.log, 'curr chann %d' % tb.FH_seq[tb.curr_chann_idx], inception)
            log_elapsed(tb.log, 'center freq is changed to %.4e' % tb.uhd_usrp_source_0.get_center_freq(), inception)
            tb.log.write('\n')
            break


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()

    
    inception = dt.datetime.now()
    sequence = (29,23,17,5,46,40,28,22,16,4,45,39,27,21,15,3,44,38,26,20,14,2,43,37,25,19,13,1,42,36,24,18,12,47,41,35,23,17,11,46,40,34,22,16,10,45,39,33,21,15,9,44,38,32,20,14,8,43,37,31,19,13,7,42,36,30,18,12,6,41,35,29,17,11,5,40,34,28,16,10,4,39,33,27,15,9,3,38,32,26,14,8,2,37,31,25,13,7,1,36,30,24,12,6,47,35,29,23,11,5,46,34,28,22,10,4,45,33,27,21,9,3,44,32,26,20,8,2,43,31,25,19,7,1,42,30,24,18,6,47,41)
    log = open('../Sample/ramdisk/Log_controller_jammer.txt', 'w')
    
    tb = Follow_with_single_usrp(sequence)
    tb.initialize(log)
    
    tb.start()

    time.sleep(5)
    log_elapsed(log, 'Waited 5sec', inception)
    
    
    catch_seq(tb)
    log_elapsed(log, 'Start Following...', inception)
    
    global_cnt = 0
    tb.tx_hop()
    tb.jam(True)
    tb.rx_hop()
    while 1:
        #if global_cnt > 1000:
        #    break
        if not tb.get_sql_on():
            log_elapsed(log, 'RX: Waiting for the activity', inception)
            time.sleep(0.001)
        else:
            tb.tx_hop()
            tb.rx_hop()
            log_elapsed(log, 'Hop ordered', inception)
            global_cnt += 1

    log.close()
    tb.stop()
    tb.wait()
