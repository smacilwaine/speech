#!/usr/bin/env python

'''
Author: Samantha MacIlwaine
Copyright 2020
Contact: srm2197@columbia.edu
'''

import os, sys

def fix_spaces(file_path):
	punctuation_options = ["``", "''", ","  ,"--", ".", "!", "?", ":"]

	file = open(file_path, "r")
	file_path_split = file_path.split('/')
	last_file = file_path_split.pop()
	output_file = open('fixed_spaces_'+last_file, 'w')
	
	# find all spaces
	# if punctuation is the next character
	# then delete the space

	for line in file:
		new_line = ''
		i = 0
		while i < len(line):
			if not ((line[i] == " ") && (line[i+1] in punctuation_options)):
				new_line += char[i]
		output_file.write(new_line)

	file.close()
	output_file.close()

def main():
	if len(sys.argv) == 2:
		file_path = sys.argv[1]
		unpunctuateFile(file_path)
	else:
		print("No file found. Please run the program correctly:\npython3 fix_spaces.py file.txt ")
		sys.exit()

if __name__ == "__main__":
	main()