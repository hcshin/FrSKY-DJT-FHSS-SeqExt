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
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import threading
import time
import datetime as dt

class Sequence_extractor(gr.top_block):

    def __init__(self, center_chann, chann_num_l, chann_num_r):
        gr.top_block.__init__(self, "Sequence Extractor")

        ##################################################
        # Variables
        ##################################################
        self.variable_function_probe_0_15 = variable_function_probe_0_15 = 0
        self.variable_function_probe_0_14 = variable_function_probe_0_14 = 0
        self.variable_function_probe_0_13 = variable_function_probe_0_13 = 0
        self.variable_function_probe_0_12 = variable_function_probe_0_12 = 0
        self.variable_function_probe_0_11 = variable_function_probe_0_11 = 0
        self.variable_function_probe_0_10 = variable_function_probe_0_10 = 0
        self.variable_function_probe_0_9 = variable_function_probe_0_9 = 0
        self.variable_function_probe_0_8 = variable_function_probe_0_8 = 0
        self.variable_function_probe_0_7 = variable_function_probe_0_7 = 0
        self.variable_function_probe_0_6 = variable_function_probe_0_6 = 0
        self.variable_function_probe_0_5 = variable_function_probe_0_5 = 0
        self.variable_function_probe_0_4 = variable_function_probe_0_4 = 0
        self.variable_function_probe_0_3 = variable_function_probe_0_3 = 0
        self.variable_function_probe_0_2 = variable_function_probe_0_2 = 0
        self.variable_function_probe_0_1 = variable_function_probe_0_1 = 0
        self.variable_function_probe_0_0 = variable_function_probe_0_0 = 0
        #self.variable_function_probe_0 = variable_function_probe_0 = 0
        NUM = 0
        STR = 'variable_function_probe'
        exec('self' + STR + '_%s' % NUM + '=' + STR + '_%s' % NUM + '= 0')
        #eval('self' + STR +'_%s' % NUM) = eval(STR + '_%s' % NUM)
        self.center_chann = center_chann
        self.samp_rate = samp_rate = 25000000
        self.if_freq_table = [0]
        self.chann_num_l = chann_num_l
        self.chann_num_r = chann_num_r
        self.lock = threading.Lock()

        ##################################################
        # Blocks
        ##################################################
        self.freq_xlating_fir_filter_xxx_0_15 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_14 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_13 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_12 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_11 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_10 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_9 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_8 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_7 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_6 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_5 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_4 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_3 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_2 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_1 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(10, ((-0.0010285986354574561, -0.0009848017944023013, -0.0009711346356198192, -0.0009126878576353192, -0.0007082896772772074, -0.00023802171926945448, 0.0006265888805501163, 0.002010512864217162, 0.004022321198135614, 0.006741601508110762, 0.01020786166191101, 0.014412014745175838, 0.019291354343295097, 0.024728646501898766, 0.030555615201592445, 0.036560770124197006, 0.042501047253608704, 0.048116534948349, 0.05314710736274719, 0.05734973028302193, 0.060515083372592926, 0.062482092529535294, 0.06314931064844131, 0.062482092529535294, 0.060515083372592926, 0.05734973028302193, 0.05314710736274719, 0.048116534948349, 0.042501047253608704, 0.036560770124197006, 0.030555615201592445, 0.024728646501898766, 0.019291354343295097, 0.014412014745175838, 0.01020786166191101, 0.006741601508110762, 0.004022321198135614, 0.002010512864217162, 0.0006265888805501163, -0.00023802171926945448, -0.0007082896772772074, -0.0009126878576353192, -0.0009711346356198192, -0.0009848017944023013, -0.0010285986354574561)), 0, samp_rate)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_null_sink_0_0_14 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_13 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_12 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_11 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_10 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_9 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_8 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_7 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_6 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_5 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_4 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_3 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_2 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/hocheol/GRC/Sample/ramdisk/centered#9.cfloat", False)
        self.analog_pwr_squelch_xx_0_15 = analog.pwr_squelch_cc(-20, 1, 25, False)
        self.analog_pwr_squelch_xx_0_14 = analog.pwr_squelch_cc(-19, 1, 25, False)
        self.analog_pwr_squelch_xx_0_13 = analog.pwr_squelch_cc(-18, 1, 25, False)
        self.analog_pwr_squelch_xx_0_12 = analog.pwr_squelch_cc(-17, 1, 25, False)
        self.analog_pwr_squelch_xx_0_11 = analog.pwr_squelch_cc(-16, 1, 25, False)
        self.analog_pwr_squelch_xx_0_10 = analog.pwr_squelch_cc(-15, 1, 25, False)
        self.analog_pwr_squelch_xx_0_9 = analog.pwr_squelch_cc(-15, 1, 25, False)
        self.analog_pwr_squelch_xx_0_8 = analog.pwr_squelch_cc(-15, 1, 25, False)
        self.analog_pwr_squelch_xx_0_7 = analog.pwr_squelch_cc(-15, 1, 25, False)
        self.analog_pwr_squelch_xx_0_6 = analog.pwr_squelch_cc(-15, 1, 25, False)
        self.analog_pwr_squelch_xx_0_5 = analog.pwr_squelch_cc(-15, 1, 25, False)
        self.analog_pwr_squelch_xx_0_4 = analog.pwr_squelch_cc(-15, 1, 25, False)
        self.analog_pwr_squelch_xx_0_3 = analog.pwr_squelch_cc(-16, 1, 25, False)
        self.analog_pwr_squelch_xx_0_2 = analog.pwr_squelch_cc(-17, 1, 25, False)
        self.analog_pwr_squelch_xx_0_1 = analog.pwr_squelch_cc(-18, 1, 25, False)
        self.analog_pwr_squelch_xx_0_0 = analog.pwr_squelch_cc(-19, 1, 25, False)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-20, 1, 25, False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_pwr_squelch_xx_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_2, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_3, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_4, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_5, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_6, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_7, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_8, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_9, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_10, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_11, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_12, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_13, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_14, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_15, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_pwr_squelch_xx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_1, 0), (self.analog_pwr_squelch_xx_0_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_2, 0), (self.analog_pwr_squelch_xx_0_2, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_3, 0), (self.analog_pwr_squelch_xx_0_3, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_4, 0), (self.analog_pwr_squelch_xx_0_4, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_5, 0), (self.analog_pwr_squelch_xx_0_5, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_6, 0), (self.analog_pwr_squelch_xx_0_6, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_7, 0), (self.analog_pwr_squelch_xx_0_7, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_8, 0), (self.analog_pwr_squelch_xx_0_8, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_9, 0), (self.analog_pwr_squelch_xx_0_9, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_10, 0), (self.analog_pwr_squelch_xx_0_10, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_11, 0), (self.analog_pwr_squelch_xx_0_11, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_12, 0), (self.analog_pwr_squelch_xx_0_12, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_13, 0), (self.analog_pwr_squelch_xx_0_13, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_14, 0), (self.analog_pwr_squelch_xx_0_14, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_15, 0), (self.analog_pwr_squelch_xx_0_15, 0))
        self.connect((self.analog_pwr_squelch_xx_0_0, 0), (self.blocks_null_sink_0_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_1, 0), (self.blocks_null_sink_0_0_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0_2, 0), (self.blocks_null_sink_0_0_1, 0))
        self.connect((self.analog_pwr_squelch_xx_0_3, 0), (self.blocks_null_sink_0_0_2, 0))
        self.connect((self.analog_pwr_squelch_xx_0_4, 0), (self.blocks_null_sink_0_0_3, 0))
        self.connect((self.analog_pwr_squelch_xx_0_5, 0), (self.blocks_null_sink_0_0_4, 0))
        self.connect((self.analog_pwr_squelch_xx_0_6, 0), (self.blocks_null_sink_0_0_5, 0))
        self.connect((self.analog_pwr_squelch_xx_0_7, 0), (self.blocks_null_sink_0_0_6, 0))
        self.connect((self.analog_pwr_squelch_xx_0_8, 0), (self.blocks_null_sink_0_0_7, 0))
        self.connect((self.analog_pwr_squelch_xx_0_9, 0), (self.blocks_null_sink_0_0_8, 0))
        self.connect((self.analog_pwr_squelch_xx_0_10, 0), (self.blocks_null_sink_0_0_9, 0))
        self.connect((self.analog_pwr_squelch_xx_0_11, 0), (self.blocks_null_sink_0_0_10, 0))
        self.connect((self.analog_pwr_squelch_xx_0_12, 0), (self.blocks_null_sink_0_0_11, 0))
        self.connect((self.analog_pwr_squelch_xx_0_13, 0), (self.blocks_null_sink_0_0_12, 0))
        self.connect((self.analog_pwr_squelch_xx_0_14, 0), (self.blocks_null_sink_0_0_13, 0))
        self.connect((self.analog_pwr_squelch_xx_0_15, 0), (self.blocks_null_sink_0_0_14, 0))


# QT sink close method reimplementation
    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def initialize(self):
        center_freq = frequency_table(self.center_chann)

        for idx in range(self.center_chann - 1, self.center_chann - self.chann_num_l - 1, -1):
            self.if_freq_table.insert(0, frequency_table(idx) - center_freq)
        
        for idx in range(self.center_chann + 1, self.center_chann + self.chann_num_r + 1, 1):
            self.if_freq_table.append(frequency_table(idx) - center_freq)

    def set_filter_freq(self):
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.if_freq_table[0])
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.if_freq_table[1])
        self.freq_xlating_fir_filter_xxx_0_1.set_center_freq(self.if_freq_table[2])
        self.freq_xlating_fir_filter_xxx_0_2.set_center_freq(self.if_freq_table[3])
        self.freq_xlating_fir_filter_xxx_0_3.set_center_freq(self.if_freq_table[4])
        self.freq_xlating_fir_filter_xxx_0_4.set_center_freq(self.if_freq_table[5])
        self.freq_xlating_fir_filter_xxx_0_5.set_center_freq(self.if_freq_table[6])
        self.freq_xlating_fir_filter_xxx_0_6.set_center_freq(self.if_freq_table[7])
        self.freq_xlating_fir_filter_xxx_0_7.set_center_freq(self.if_freq_table[8])
        self.freq_xlating_fir_filter_xxx_0_8.set_center_freq(self.if_freq_table[9])
        self.freq_xlating_fir_filter_xxx_0_9.set_center_freq(self.if_freq_table[10])
        self.freq_xlating_fir_filter_xxx_0_10.set_center_freq(self.if_freq_table[11])
        self.freq_xlating_fir_filter_xxx_0_11.set_center_freq(self.if_freq_table[12])
        self.freq_xlating_fir_filter_xxx_0_12.set_center_freq(self.if_freq_table[13])
        self.freq_xlating_fir_filter_xxx_0_13.set_center_freq(self.if_freq_table[14])
        self.freq_xlating_fir_filter_xxx_0_14.set_center_freq(self.if_freq_table[15])
        self.freq_xlating_fir_filter_xxx_0_15.set_center_freq(self.if_freq_table[16])

    def get_filter_freq(self):
        print tb.freq_xlating_fir_filter_xxx_0.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_0.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_1.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_2.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_3.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_4.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_5.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_6.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_7.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_8.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_9.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_10.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_11.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_12.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_13.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_14.center_freq()
        print tb.freq_xlating_fir_filter_xxx_0_15.center_freq()


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
    tb = Sequence_extractor(9, 8, 8)
    tb.initialize()
    tb.set_filter_freq()

    tb.start()

    iter_period_in_sec = 1.0/200
    Runtime_in_sec = 10
    N_iter = int(Runtime_in_sec / iter_period_in_sec) + 1

    for j in range(N_iter):
        for k in range(tb.chann_num_l + 1 + tb.chann_num_r):
            if tb.analog_pwr_squelch_xx_0.unmuted():
                print 1
            if tb.analog_pwr_squelch_xx_0_0.unmuted():
                print 2
            if tb.analog_pwr_squelch_xx_0_1.unmuted():
                print 3
            if tb.analog_pwr_squelch_xx_0_2.unmuted():
                print 4
            if tb.analog_pwr_squelch_xx_0_3.unmuted():
                print 5
            if tb.analog_pwr_squelch_xx_0_4.unmuted():
                print 6
            if tb.analog_pwr_squelch_xx_0_5.unmuted():
                print 7
            if tb.analog_pwr_squelch_xx_0_6.unmuted():
                print 8
            if tb.analog_pwr_squelch_xx_0_7.unmuted():
                print 9
            if tb.analog_pwr_squelch_xx_0_8.unmuted():
                print 10
            if tb.analog_pwr_squelch_xx_0_9.unmuted():
                print 11
            if tb.analog_pwr_squelch_xx_0_10.unmuted():
                print 12
            if tb.analog_pwr_squelch_xx_0_11.unmuted():
                print 13
            if tb.analog_pwr_squelch_xx_0_12.unmuted():
                print 14
            if tb.analog_pwr_squelch_xx_0_13.unmuted():
                print 15
            if tb.analog_pwr_squelch_xx_0_14.unmuted():
                print 16
            if tb.analog_pwr_squelch_xx_0_15.unmuted():
                print 17
        time.sleep(iter_period_in_sec)

    tb.stop()
    tb.wait()
