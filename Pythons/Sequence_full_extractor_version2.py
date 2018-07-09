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
        self.variable_function_probe_0 = variable_function_probe_0 = 0
        self.center_chann = center_chann
        self.samp_rate = samp_rate = 25000000
        self.if_freq_table = [0]
        self.chann_num_l = chann_num_l
        self.chann_num_r = chann_num_r

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
        self.analog_pwr_squelch_xx_0_15 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_14 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_13 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_12 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_11 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_10 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_9 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_8 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_7 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_6 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_5 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_4 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_3 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_2 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_1 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0_0 = analog.pwr_squelch_cc(-30, 1, 25, False)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-30, 1, 25, False)

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

        def _variable_function_probe_0_15_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_15.unmuted()
        		try: self.set_variable_function_probe_0_15(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_15():
                            print "17"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_15_thread = threading.Thread(target=_variable_function_probe_0_15_probe)
        _variable_function_probe_0_15_thread.daemon = True
        _variable_function_probe_0_15_thread.start()
        def _variable_function_probe_0_14_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_14.unmuted()
        		try: self.set_variable_function_probe_0_14(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_14():
                            print "16"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_14_thread = threading.Thread(target=_variable_function_probe_0_14_probe)
        _variable_function_probe_0_14_thread.daemon = True
        _variable_function_probe_0_14_thread.start()
        def _variable_function_probe_0_13_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_13.unmuted()
        		try: self.set_variable_function_probe_0_13(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_13():
                            print "15"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_13_thread = threading.Thread(target=_variable_function_probe_0_13_probe)
        _variable_function_probe_0_13_thread.daemon = True
        _variable_function_probe_0_13_thread.start()
        def _variable_function_probe_0_12_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_12.unmuted()
        		try: self.set_variable_function_probe_0_12(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_12():
                            print "14"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_12_thread = threading.Thread(target=_variable_function_probe_0_12_probe)
        _variable_function_probe_0_12_thread.daemon = True
        _variable_function_probe_0_12_thread.start()
        def _variable_function_probe_0_11_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_11.unmuted()
        		try: self.set_variable_function_probe_0_11(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_11():
                            print "13"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_11_thread = threading.Thread(target=_variable_function_probe_0_11_probe)
        _variable_function_probe_0_11_thread.daemon = True
        _variable_function_probe_0_11_thread.start()
        def _variable_function_probe_0_10_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_10.unmuted()
        		try: self.set_variable_function_probe_0_10(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_10():
                            print "12"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_10_thread = threading.Thread(target=_variable_function_probe_0_10_probe)
        _variable_function_probe_0_10_thread.daemon = True
        _variable_function_probe_0_10_thread.start()
        def _variable_function_probe_0_9_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_9.unmuted()
        		try: self.set_variable_function_probe_0_9(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_9():
                            print "11"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_9_thread = threading.Thread(target=_variable_function_probe_0_9_probe)
        _variable_function_probe_0_9_thread.daemon = True
        _variable_function_probe_0_9_thread.start()
        def _variable_function_probe_0_8_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_8.unmuted()
        		try: self.set_variable_function_probe_0_8(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_8():
                            print "10"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_8_thread = threading.Thread(target=_variable_function_probe_0_8_probe)
        _variable_function_probe_0_8_thread.daemon = True
        _variable_function_probe_0_8_thread.start()
        def _variable_function_probe_0_7_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_7.unmuted()
        		try: self.set_variable_function_probe_0_7(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_7():
                            print "9"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_7_thread = threading.Thread(target=_variable_function_probe_0_7_probe)
        _variable_function_probe_0_7_thread.daemon = True
        _variable_function_probe_0_7_thread.start()
        def _variable_function_probe_0_6_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_6.unmuted()
        		try: self.set_variable_function_probe_0_6(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_6():
                            print "8"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_6_thread = threading.Thread(target=_variable_function_probe_0_6_probe)
        _variable_function_probe_0_6_thread.daemon = True
        _variable_function_probe_0_6_thread.start()
        def _variable_function_probe_0_5_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_5.unmuted()
        		try: self.set_variable_function_probe_0_5(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_5():
                            print "7"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_5_thread = threading.Thread(target=_variable_function_probe_0_5_probe)
        _variable_function_probe_0_5_thread.daemon = True
        _variable_function_probe_0_5_thread.start()
        def _variable_function_probe_0_4_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_4.unmuted()
        		try: self.set_variable_function_probe_0_4(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_4():
                            print "6"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_4_thread = threading.Thread(target=_variable_function_probe_0_4_probe)
        _variable_function_probe_0_4_thread.daemon = True
        _variable_function_probe_0_4_thread.start()
        def _variable_function_probe_0_3_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_3.unmuted()
        		try: self.set_variable_function_probe_0_3(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_3():
                            print "5"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_3_thread = threading.Thread(target=_variable_function_probe_0_3_probe)
        _variable_function_probe_0_3_thread.daemon = True
        _variable_function_probe_0_3_thread.start()
        def _variable_function_probe_0_2_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_2.unmuted()
        		try: self.set_variable_function_probe_0_2(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_2():
                            print "4"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_2_thread = threading.Thread(target=_variable_function_probe_0_2_probe)
        _variable_function_probe_0_2_thread.daemon = True
        _variable_function_probe_0_2_thread.start()
        def _variable_function_probe_0_1_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_1.unmuted()
        		try: self.set_variable_function_probe_0_1(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_1():
                            print "3"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_1_thread = threading.Thread(target=_variable_function_probe_0_1_probe)
        _variable_function_probe_0_1_thread.daemon = True
        _variable_function_probe_0_1_thread.start()
        def _variable_function_probe_0_0_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0_0.unmuted()
        		try: self.set_variable_function_probe_0_0(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0_0():
                            print "2"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_0_thread = threading.Thread(target=_variable_function_probe_0_0_probe)
        _variable_function_probe_0_0_thread.daemon = True
        _variable_function_probe_0_0_thread.start()
        def _variable_function_probe_0_probe():
        	while True:
        		val = self.analog_pwr_squelch_xx_0.unmuted()
        		try: self.set_variable_function_probe_0(val)
        		except AttributeError, e: pass
                        if self.get_variable_function_probe_0():
                            print "1"
        		time.sleep(1.0/(200))
        _variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
        _variable_function_probe_0_thread.daemon = True
        _variable_function_probe_0_thread.start()

# QT sink close method reimplementation

    def get_variable_function_probe_0_15(self):
        return self.variable_function_probe_0_15
    def get_variable_function_probe_0_14(self):
        return self.variable_function_probe_0_14
    def get_variable_function_probe_0_13(self):
        return self.variable_function_probe_0_13
    def get_variable_function_probe_0_12(self):
        return self.variable_function_probe_0_12
    def get_variable_function_probe_0_11(self):
        return self.variable_function_probe_0_11
    def get_variable_function_probe_0_10(self):
        return self.variable_function_probe_0_10
    def get_variable_function_probe_0_9(self):
        return self.variable_function_probe_0_9
    def get_variable_function_probe_0_8(self):
        return self.variable_function_probe_0_8
    def get_variable_function_probe_0_7(self):
        return self.variable_function_probe_0_7
    def get_variable_function_probe_0_6(self):
        return self.variable_function_probe_0_6
    def get_variable_function_probe_0_5(self):
        return self.variable_function_probe_0_5
    def get_variable_function_probe_0_4(self):
        return self.variable_function_probe_0_4
    def get_variable_function_probe_0_3(self):
        return self.variable_function_probe_0_3

    def set_variable_function_probe_0_15(self, variable_function_probe_0_15):
        self.variable_function_probe_0_15 = variable_function_probe_0_15
    def set_variable_function_probe_0_14(self, variable_function_probe_0_14):
        self.variable_function_probe_0_14 = variable_function_probe_0_14
    def set_variable_function_probe_0_13(self, variable_function_probe_0_13):
        self.variable_function_probe_0_13 = variable_function_probe_0_13
    def set_variable_function_probe_0_12(self, variable_function_probe_0_12):
        self.variable_function_probe_0_12 = variable_function_probe_0_12
    def set_variable_function_probe_0_11(self, variable_function_probe_0_11):
        self.variable_function_probe_0_11 = variable_function_probe_0_11
    def set_variable_function_probe_0_10(self, variable_function_probe_0_10):
        self.variable_function_probe_0_10 = variable_function_probe_0_10
    def set_variable_function_probe_0_9(self, variable_function_probe_0_9):
        self.variable_function_probe_0_9 = variable_function_probe_0_9
    def set_variable_function_probe_0_8(self, variable_function_probe_0_8):
        self.variable_function_probe_0_8 = variable_function_probe_0_8
    def set_variable_function_probe_0_7(self, variable_function_probe_0_7):
        self.variable_function_probe_0_7 = variable_function_probe_0_7
    def set_variable_function_probe_0_6(self, variable_function_probe_0_6):
        self.variable_function_probe_0_6 = variable_function_probe_0_6
    def set_variable_function_probe_0_5(self, variable_function_probe_0_5):
        self.variable_function_probe_0_5 = variable_function_probe_0_5
    def set_variable_function_probe_0_4(self, variable_function_probe_0_4):
        self.variable_function_probe_0_4 = variable_function_probe_0_4
    def set_variable_function_probe_0_3(self, variable_function_probe_0_3):
        self.variable_function_probe_0_3 = variable_function_probe_0_3

    def get_variable_function_probe_0_2(self):
        return self.variable_function_probe_0_2

    def set_variable_function_probe_0_2(self, variable_function_probe_0_2):
        self.variable_function_probe_0_2 = variable_function_probe_0_2

    def get_variable_function_probe_0_1(self):
        return self.variable_function_probe_0_1

    def set_variable_function_probe_0_1(self, variable_function_probe_0_1):
        self.variable_function_probe_0_1 = variable_function_probe_0_1

    def get_variable_function_probe_0_0(self):
        return self.variable_function_probe_0_0

    def set_variable_function_probe_0_0(self, variable_function_probe_0_0):
        self.variable_function_probe_0_0 = variable_function_probe_0_0

    def get_variable_function_probe_0(self):
        return self.variable_function_probe_0

    def set_variable_function_probe_0(self, variable_function_probe_0):
        self.variable_function_probe_0 = variable_function_probe_0

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

    time.sleep(10)
    tb.stop()
    tb.wait()
