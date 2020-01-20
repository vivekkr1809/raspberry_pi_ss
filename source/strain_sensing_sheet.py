#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Python modules
import numpy as np
import pandas as pd
import math
import random
import time
import sys
import getopt

# MCC daq modules
import uldaq


"""
TO DO:
1. Read the baseline and store the baseline values
"""


def main(argv):
	current_time = time.localtime()
	current_time = time.strftime("%H_%M_%S", current_time)

	baseline_vector_file_name  = ''
	measurement_vector_file_name = ''
	try:
		opts, args = getopt.getopt(argv,"hb:m:",["bfile=","mfile="])
	except getopt.GetoptError:
		print ('strain_sensing_sheet.py -b <baseline_vector_file_name> -m <measurement_vector_file_name>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('strain_sensing_sheet.py -b <baseline_vector_file_name> -m <measurement_vector_file_name>')
			sys.exit()
		elif opt in ("-b", "--bfile"):
			baseline_vector_file_name = arg+current_time+'.csv'
		elif opt in ("-m", "--mfile"):
			measurement_vector_file_name = arg+current_time+'.csv'

	# Properties of the resistive strain gage
	gage_factor = 2.0
	# The amplifier gain
	gain = 200.
	
	return 0

if __name__ == '__main__':
	main(sys.argv[1:])