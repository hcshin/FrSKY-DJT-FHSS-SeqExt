#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Sequence Extractor
# Generated: Fri Mar 14 21:36:14 2014
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
import threading
import time
import datetime as dt
import sys
import numpy

class Sequence_extractor(gr.top_block):

    def __init__(self, center_chann, chann_num_l, chann_num_r):
        gr.top_block.__init__(self, "Sequence Extractor")

        ##################################################
        # Variables
        ##################################################
        self.number_of_channels = chann_num_r + 1 +  chann_num_l
        self.center_chann = center_chann
        self.samp_rate = samp_rate = 25000000
        self.if_freq_table = [0]
        self.chann_num_l = chann_num_l
        self.chann_num_r = chann_num_r
        self.lock = threading.Lock()
        self.filter_tab = (-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)
        self.filter_decimation = 10
        self.squelch_thresholds = (-20, -19, -18, -17, -16, -15, -15, -15, -15, -15, -15, -15, -16, -17, -18, -19, -20)

        ##################################################
        # Blocks
        ##################################################
        
        #usrp source
        self.usrp_source = uhd.usrp_source(
                device_addr = "addr=192.168.10.2",
                stream_args = uhd.stream_args(
                    cpu_format="fc32",
                    channels=range(1),
                    ),
                )
        self.usrp_source.set_samp_rate(samp_rate)
        self.usrp_source.set_center_freq(2.42e9, 0)
        self.usrp_source.set_gain(0, 0)
        self.usrp_source.set_antenna("RX2", 0)

        #parallel blocks
        for n in range(self.number_of_channels):
            #filter banks
            exec('self.channel_filter_%s = filter.freq_xlating_fir_filter_ccc(self.filter_decimation, self.filter_tab, 0, samp_rate)' % n)

            #null sinks
            exec('self.null_sink_%s = blocks.null_sink(gr.sizeof_gr_complex*1)' % n)

            #squelch blocks
            exec('self.squelch_%s = analog.pwr_squelch_cc(self.squelch_thresholds[%s], 1, 25, False)' % (n, n))

        ##################################################
        # Connections
        ##################################################

        #sigular connections

        #parallel connections
        for n in range(self.number_of_channels):
            #usrp source -> channel_filter -> squelch -> null_sink
            exec('self.connect((self.usrp_source, 0), (self.channel_filter_%s, 0), (self.squelch_%s, 0), (self.null_sink_%s, 0))' % (n, n, n))

#class methods

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.throttle.set_sample_rate(self.samp_rate)

    def initialize(self):
        center_freq = frequency_table(self.center_chann)
        self.usrp_source.set_center_freq(frequency_table(self.center_chann))
        while not self.usrp_source.get_sensor("lo_locked"):
            pass

        for idx in range(self.center_chann - 1, self.center_chann - self.chann_num_l - 1, -1):
            self.if_freq_table.insert(0, frequency_table(idx) - center_freq)
        
        for idx in range(self.center_chann + 1, self.center_chann + self.chann_num_r + 1, 1):
            self.if_freq_table.append(frequency_table(idx) - center_freq)

    def set_filter_freq(self):
        for n in range(self.number_of_channels):
            exec('self.channel_filter_%s.set_center_freq(self.if_freq_table[%s])' % (n, n))

    def get_filter_freq(self, fp):
        for n in range(self.number_of_channels):
            fp.write(eval('self.channel_filter_%s.center_freq()' % n))

#Global functions
def print_elapsed(desc, start):
    end = dt.datetime.now()
    print desc, (end - start).seconds + ((end - start).microseconds)/1e6

def frequency_table(chann_num):
    frequency_table = (2.405148,2.406648,2.408148,2.409647,2.411149,2.412647,2.414149,2.415647,2.417147,2.418648,2.420147,2.421646,2.423146,2.424645,2.426146,2.427645,2.429145,2.430647,2.432147,2.433644,2.435145,2.436645,2.438148,2.439643,2.441144,2.442648,2.444147,2.445645,2.447148,2.448645,2.450142,2.451646,2.453146,2.454643,2.456143,2.457641,2.459138,2.460639,2.462137,2.463639,2.465138,2.466638,2.468134,2.469635,2.471134,2.472634,2.474134)
    return frequency_table[chann_num - 1] * 1e9

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()

    
    inception = dt.datetime.now()
    extractor = Sequence_extractor(9, 8, 8)
    extractor.initialize()
    extractor.set_filter_freq()

    #flowgraph start
    extractor.start()

    #set runtime
    iter_period_in_sec = 1.0/500
    Runtime_in_sec = 20 
    N_iter = int(Runtime_in_sec / iter_period_in_sec) + 1

    #output files
    channel_activity = open('out.txt', 'w')
    log = open('log_seq_full_ext_ver5.txt', 'w')

    #monitor channel activity
    for j in range(N_iter):
        for n in range(extractor.number_of_channels):
            if eval('extractor.squelch_%s.unmuted()' % n):
                channel_activity.write('%s\n' % (n + 1))
        time.sleep(iter_period_in_sec)

    #stop flowgraph
    extractor.stop()
    extractor.wait()

    #close output files
    channel_activity.close()
    log.close()


# peak identification starts
# file name configure, infile = input file, step# = output file of each step
infile = 'out.txt'
out1 = infile.replace('.', '-1.')
out2 = infile.replace('.', '-2.')
out3 = infile.replace('.', '-3.')

print '=============== step1 ===============\n'
with open(infile, 'r') as fin:
    signal = fin.read().split('\n')                # read input sequence
    signal = map(int, signal[0:-1])              # str --> int mapping
    fout1 = open(out1, 'w')                    # [ch] [count] format

    # count the number of repetition
    prev = signal[0]                        
    counter = 1
    a = 0                                                  # avg = a/b
    b = 0
    for ch in signal:
        if ch == prev:
            counter += 1
        else:
            fout1.write('%s %s\n' % (prev, counter))
            if prev != 0:
                a += counter #cumulatively calculate total # of iteration
                b += 1 #cumulatively calculate total # of peaks
            counter = 1
        prev = ch

    fout1.close()
    
avg = a / b                           # avg = int(# of iteration of 1 peak)
print 'avg = %d\n' % avg 

'''
add assumption : no channel repetition
'''
prev = 0

print '=============== step2 ===============\n'
with open(out1, 'r') as fout1: #load output of step1
    lines = fout1.readlines() #step1 line format: [ch] [count]
    fout2 = open(out2, 'w')     # [ch] [count] [rate] [len] w/o zeros

    for line in lines:
        temp = list(map(int, line.split()))    # temp = [ch] [count]
        num = int(round(float(temp[1]) / avg)) # temp[1] = count, # iter in peak

        if temp[0] == 0: # in case of inactive 
            #format: [ch] [# iter in int] [# iter in float] [# iter in peak]
            print '%3d %3d %10f %3d' % (temp[0], temp[1], float(temp[1]) / avg, num)
        for i in range(num):
            if prev != 0 and prev == temp[0]: #if the same channel occurs consecutively
                continue
            fout2.write('%s\n' % (temp[0])) #record repetition removed peak
            prev = temp[0]
    fout2.close()
            
print '=============== step3 ===============\n'
#from this step period derivation starts
with open(out2, 'r') as fout2: #load output of step2
    seq = fout2.read().split('\n') #print list of channels in the file
    seq = map(int, seq[: -1])  # convert str --> int raw sequence data

winsize = 100                   # window size (sliding window)
cutoff = 10                    # start offset (erase first # elements)
freqList = []                  # save freq list for

for offset in range(cutoff, len(seq) - cutoff):
    window = seq[offset : offset + winsize] # sliding window for search

    freq = 0
    for i in range(offset + 1, len(seq) - winsize):
        temp = seq[i : i + winsize] #sliding window for comparison
        freq = freq + 1 #freq = #(window shift)
        checker = winsize

        for i, j in zip(window, temp):
            if i == j:                    
                checker = checker - 1

        if checker == 0:             # window == temp, i.e. perfect match
            if len(freqList) > 3: #if more than 3 matches
                #tempavg = avg # of peaks in the first three period
                tempavg = float(sum(i for i, j in freqList)) /  len(freqList)
                if abs(tempavg - freq) > 5:  # if freq is weird (different in more than 5 peaks), drop!
                    continue
            # print freq, window
            freqList.append((freq, offset)) #freq becomes candidate period
            break

avgFreq = float(sum(i for i, j in freqList)) /  len(freqList) #should be homogenious since heterogeneity is removed 
print 'freq list = \n%s\n' % freqList
print 'average freq = %f\n' % avgFreq #avg # of peaks in a period
avgFreq = int(round(avgFreq)) #round the avg period
 
print '=============== step4 ===============\n'
first = freqList[0][1]  #freqlist = [(freq, offset)], i.e. offset to the second period
end = first + avgFreq #end of the first period
print 'first = %s, end = %s' % (first, end)
with open(out3, 'w') as fout:
    for j, k in freqList: #freqlist = [(freq, offset)]
        if j == avgFreq: #print periods which matches the avg only 
            sequence = numpy.roll(seq[k : k+avgFreq], k - first) # rotate list
            sequence = sequence.ravel().tolist()               # array to list
            # print k, sequence                                  
            fout.write('%s\n' % sequence)
