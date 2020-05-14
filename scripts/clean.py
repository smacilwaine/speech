#!/usr/bin/env python

'''
Author: Samantha MacIlwaine
Copyright 2020
Contact: srm2197@columbia.edu
'''

import os, sys

 # treat apostraphes as letters
 # keep ?!,.
 # replace or delete all others

def cleanData(file_path, output_file_path):
	punctuation_to_replace = {
		"-":" ",
		":":",",
		"`":"",
		"(":"",
		")":"",
		";":".",
		"!":".",
		"?":" ? ",
		".":" . ",
		",":" , ",
		"...":" ",
	}

	file = open(file_path, "r")
	output_file = open(output_file_path, 'w')

	for line in file:
		x = str(line)
		i = 0
		for mark in punctuation_to_replace:
			x = x.replace(mark, punctuation_to_replace[mark])
		output_file.write(x)

	file.close()
	output_file.close()

def main():
	if len(sys.argv) == 3:
		file_path = sys.argv[1]
		output_file_path = sys.argv[2]
		cleanData(file_path, output_file_path)
	else:
		print("No file found. Please run the program correctly:\npython3 clean.py /path/to/input_file /path/to/output_file")
		sys.exit()

if __name__ == "__main__":
	main()