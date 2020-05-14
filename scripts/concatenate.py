#!/usr/bin/env python

'''
Author: Samantha MacIlwaine
Copyright 2020
Contact: srm2197@columbia.edu
'''

import os, sys
import random

def concatenateFile(input_path, partial_path, default_path, accuracy):

	# remove all punctuation except question marks

	file = open(input_path, 'r')
	partial = open(partial_path, 'w')
	default = open(default_path, 'w')

	for line in file:
		if '?' not in line:
			default.write(line)
		else: # question turn exists
			# introduce element of randomness
			prob = random.randint(0,100)
			if prob <= int(accuracy):
				# simulate question turn being identified
				partial.write(line)
			else:
				# simulate question turn being missed by less-than-accurate models
				default.write(line)
		
	file.close()
	partial.close()
	default.close()

def main():
	if len(sys.argv) == 4:
		original_file_path = sys.argv[1]
		partial_output_path = sys.argv[2]
		default_output_path = sys.argv[3]
		concatenateFile(original_file_path, partial_output_path, default_output_path)
	else:
		print("No file found. Please run the program correctly:\npython3 partialize.py /path/to/input /path/to/partial/output /path/to/default/output")
		sys.exit()

if __name__ == "__main__":
	main()