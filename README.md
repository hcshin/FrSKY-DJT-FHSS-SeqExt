# Source codes for the WISA2015 paper: Security Analysis of FHSS-type Drone Controller
Paper URL: 1) https://link.springer.com/chapter/10.1007/978-3-319-31875-2_20 2) https://syssec.kaist.ac.kr/pub/2015/shin_wisa2015.pdf

## NOTICE 
Source codes used for the experiments on FrSKY DJT Telemetry system that utilizes FHSS. Note that, these codes are uploaded just for the reference not for being run directly. If you want to run them, a considerable amount of modification would be required.

## Contents and Descriptions
* GRCs - Gnuradio-Companion files used for generating skeletal python scripts
	* Follow_with_single_filesource_1CH.grc - Signal flowgraph for implementing FHSS sequence tracker. Uses a recorded file source instead of an USRP, and monitors 1 channel at a time.
	* Follow_with_single_filesource_3CH.grc - Signal flowgraph for implementing FHSS sequence tracker. Uses a recorded file source instead of an USRP, and monitors 3 channels at a time.
	* Follow_with_dual_usrp.grc - Signal flowgraph for implementing FHSS sequence tracker. Designed to used two USRPs connected with a MIMO cable.
	* Baseband_extractor.grc - Signal flowgraph for extracting baseband of FrSKY DJT Telemetry system
	* Controller_rand_jammer.grc - Signal flowgraph for implementing a random jammer used as a reference in comparison with the implemented adaptive jammer.
	* Sequence_extractor_singlechannel.grc - Signal flowgraph for implementing skeletal python script that automatically extracts FHSS hopping sequence. Monitors 1 channel only.
	* Sequence_extractor_multichannel.grc - Signal flowgraph for implementing skeletal python script that automatically extracts FHSS hopping sequence. Monitors 5 channels simutaneously.

* Pythons - Python scripts modified from skeletal python scripts generated by GRC
	* baseband_extractor.py - Script that extracts baseband signal of FrSKY DJT Telemetry system. followes the FHSS hopping s
	* Controller_jammer2_log_ver.py - Script that reactively jams the ongoing FHSS transmission of FrSKY DJT Telemetry system based on the extracted FHSS sequence. Logs the details into a file.
	* Controller_jammer2_print_ver.py - Script that reactively jams the ongoing FHSS transmission of FrSKY DJT Telemetry system based on the extracted FHSS sequence. Prints the details into a file.
	* Controller_rand_jammer.py - Script that randomly jamms FHSS subchannels of FrSKY DJT Telemetry system.
	* Follow_with_dual_usrp.py - Script for FHSS sequence tracker. Derived from the skeletal script generated by Follow_with_dual_usrp.grc.
	* Follow_with_dual_usrp_dual_squelch(2).py - Added one more squelch to Follow_with_dual_usrp.py
	* Follow_with_single_filesource_1CH.py - Script for FHSS sequence tracker. Derived from the skeletal script generated by Follow_with_single_filesource_1CH.grc.
	* Follow_with_single_usrp.py - Script for FHSS sequence tracker. Uses a single USRP.
	* Follow_with_single_usrp_pll.py - Script for FHSS sequence tracker. PLL module added to fine-tune into the FHSS subchannel. 
	* Follow_with_single_usrp_pll_wxgui.py - Script for FHSS sequence tracker. PLL module and wxgui visualization added for subchannel fine-tuning and visualizing the baseband waveform. 
	* Follow_with_single_usrp_wxgui.py - Script for FHSS sequence tracker. wxgui visualization added for visualizing the baseband waveform. 
	* seq_ext+period_deriv_usrp_ver0~2.py - Script for automatic sequence extraction and period derivation. Uses a USRP source. N.B. experimental. Cannot guarantee these work.
	* Sequence_full_extractor_version1~5.py - Script for automatic sequence extraction. N.B. experimental. Cannot guarantee these work.