#!/usr/bin/env python

'''
Author: Samantha MacIlwaine
Copyright 2020
Contact: srm2197@columbia.edu
'''

import os, sys

def unpunctuateFile(file_path, lowercase):
	punctuation_options = ["\`", "\'", ","  ,"-", ".", "!", "?", ":", ";"]

	file = open(file_path, "r")
	file_path_split = file_path.split('/')
	last_file = file_path_split.pop()
	output_file = open('./src/prepared-testing-files/'+last_file, 'w')
	

	for line in file:
		x = str(line)
		i = 0
		while i < len(punctuation_options):
			x = x.replace(punctuation_options[i], '')
			i += 1
		if lowercase: x = str.lower(x)
		output_file.write(x)

	file.close()
	output_file.close()

def main():
	if len(sys.argv) == 2:
		file_path = sys.argv[1]
		lowercase = False
		unpunctuateFile(file_path, lowercase)
	elif len(sys.argv) == 3:
		file_path = sys.argv[1]
		if sys.argv[2] == "-lowercase":
			lowercase = True
			unpunctuateFile(file_path, lowercase)
	else:
		print("No file found. Please run the program correctly:\npython3 unpunctuate.py file.txt [optional: -lowercase]")
		sys.exit()

if __name__ == "__main__":
	main()