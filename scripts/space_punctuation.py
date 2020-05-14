#!/usr/bin/env python

'''
Author: Samantha MacIlwaine
Copyright 2020
Contact: srm2197@columbia.edu
'''

import os, sys

def spacePunctuation(file_path):
	punctuation_options = ["\`", "\'", ","  ,"-", ".", "!", "?", ":", ";"]

	file = open(file_path, "r")
	file_path_split = file_path.split('/')
	last_file = file_path_split.pop()
	output_file = open(last_file+'.fixed', 'w')

	for line in file:
		x = str(line)
		x = x.replace(".", " . ")
		x = x.replace("?", " ? ")
		x = x.replace("!", " ! ")
		x = x.replace(",", " , ")
		
		output_file.write(x)

	file.close()
	output_file.close()

def main():
	if len(sys.argv) == 2:
		file_path = sys.argv[1]
		spacePunctuation(file_path)
	else:
		print("No file found. Please run the program correctly:\npython3 space_punctuation.py file.txt")
		sys.exit()

if __name__ == "__main__":
	main()