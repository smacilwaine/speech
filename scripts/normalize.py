#!/usr/bin/env python

'''
Author: Samantha MacIlwaine
Copyright 2020
Contact: srm2197@columbia.edu
'''

import os, sys

# we want number of question marks to equal number of periods
# count question marks and periods
# then go through again
# for each line, count periods and question marks
	# if no question marks && if total periods > question_marks:
	# then remove (and adjust count)
# any sentence that has a period but no question marks, remove
# do this recursively until question marks >= periods

def countTotalQuestionMarksAndPeriods(file):
	print("Doing initial count")
	q = 0
	p = 0
	for line in file:
		for char in line:
			if char == '?':
				q += 1
			elif char == '.':
				p += 1
	print("Got "+str(q)+" question marks and "+str(p)+" periods.")
	return q, p

def countQuestionsMarksAndPeriodsInLine(line):
	q = 0
	p = 0
	for char in line:
		if char == '?':
			q += 1
		elif char == '.':
			p += 1
	return q, p

# dynamically normalize amount of question marks to equal amount of periods 
def normalizeFile(input_path, output_path):
	print("Normalizing new file...")
	input_file = open(input_path, "r")
	output_file = open(output_path, 'w')

	# first count total question marks and periods
	corpus = input_file.read().splitlines()
	new_corpus = []

	questions, periods = countTotalQuestionMarksAndPeriods(corpus)

	for line in corpus:
		q, p = countQuestionsMarksAndPeriodsInLine(line)
		if questions < periods:
			if q == 0:
				# if you want to remove lines with no ending punctuation, do it here
				periods -= p
			elif q > 0:
				questions += q
				periods += p
				new_corpus.append(line)
			else:
				new_corpus.append(line)
		else:
			questions += q
			periods += p
			new_corpus.append(line)

	print("Done adjusting.")
	new_q, new_p = countTotalQuestionMarksAndPeriods(new_corpus)

	for line in new_corpus:
		output_file.write(line+'\n')

	input_file.close()
	output_file.close()

def main():
	if len(sys.argv) == 3:
		input_path = sys.argv[1]
		output_path = sys.argv[2]
		normalizeFile(input_path, output_path)
	else:
		print("No file found. Please run the program correctly:\npython3 normalize.py /path/to/source.file /path/to/output.file")
		sys.exit()

if __name__ == "__main__":
	main()