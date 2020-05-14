#!/usr/bin/env python

'''
Author: Samantha MacIlwaine
Copyright 2020
Contact: srm2197@columbia.edu

Note: These statistics are only related to punctuation.
'''

import os, sys
import re

def getStats(real, predicted):
	# correct punctuation identified over all punctuation identified
	# for each line in predicted, check if this is also the case in real, if not, wrong

	punc_marks = ['.', ',', '?']
	bad_marks = ["`", "'","-", ":", ";", "(", ")", "!"]

	true_positives = 0 # punctuation, predicted
	false_positives = 0 # not punctuation, predicted
	false_negatives = 0 # punctuation, not predicted
	true_negatives = 0 # not punctuation, not predicted 

	l = 0
	while l < len(predicted) and l < len(real):
		rline = real[l].strip().lower()
		pline = predicted[l].strip().lower()

		c1 = 0
		c2 = 0

		while (c1 < len(rline)) and (c2 < len(pline)):
			if rline[c1] in bad_marks:
				c1 += 1
			elif pline[c2] in bad_marks:
				c2 += 1
			else:
				if rline[c1] == pline[c2]:

					# if punctuation
					if rline[c1] in punc_marks:
						# true positive
						true_positives += 1

					# if not punctuation
					else:
						true_negatives += 0
				else:
					# one is punctuation

					# if real one is punctuation & predicted missed it
					if rline[c1] in punc_marks:
						false_negatives += 1
						c2 += 1

					# else predicted added it but it's not punctuation
					else:
						false_positives += 1
						c2 += 1
				c1 += 1
				c2 += 1
		# now check if anything left
		if c1 != c2:
			if c2 > c1:
				false_positives += len(pline[c2:])
			else:
				false_negatives += len(rline[c1:])
		l += 1
	# end of line logic
	precision = float(true_positives) / float(true_positives + false_positives)
	recall = float(true_positives) / float(true_positives + false_negatives)
	f_measure = float(2 * precision * recall) / float(precision + recall)
	return precision, recall, f_measure

def getTextStats(text, output_file):
	count_comma = 0
	count_period = 0
	count_question_mark = 0

	for line in text:
		for char in line:
			if char == ",": 
				count_comma += 1
			elif char == ".": 
				count_period += 1
			elif char == "?":
				count_question_mark += 1

	total = count_comma + count_period + count_question_mark

	output_file.write("Commas:"+str(count_comma)+" "+str(float(100*count_comma)/float(total))+'\n')
	output_file.write("Periods:"+str(count_period)+" "+str(float(100*count_period)/float(total))+'\n')
	output_file.write("Question Marks:"+str(count_question_mark)+" "+str(float(100*count_question_mark)/float(total))+'\n')

def main():
	if len(sys.argv) == 3:
		real_file_path = sys.argv[1]
		real_file = open(real_file_path, 'r')
		real = real_file.read().splitlines()

		predicted_file_path = sys.argv[2]
		predicted_file = open(predicted_file_path, 'r')
		predicted = predicted_file.read().splitlines()

		file_base=os.path.basename(real_file_path)
		splits = file_base.split('.')
		output_file = open('../src/results-files/'+splits[0]+'_results.txt', 'w')

		precision, recall, f_measure = getStats(real, predicted)

		output_file.write('\n')
		output_file.write('Statistics for Real File\n')
		output_file.write('------------------------\n')
		getTextStats(real, output_file)

		output_file.write('\n')
		output_file.write('Statistics for Predicted File\n')
		output_file.write('------------------------\n')
		getTextStats(predicted, output_file)

		output_file.write('\n')
		output_file.write('FEEDBACK FOR MODEL\n')
		output_file.write('------------------------\n')
		output_file.write('Precision: '+str(100*precision)+'\n')
		output_file.write('Recall: '+str(100*recall)+'\n')
		output_file.write('F-Measure: '+str(100*f_measure)+'\n')

		predicted_file.close()
		real_file.close()
	else:
		print("Error. Please run the program correctly:\npython3 get_statistics.py /path/to/real/file.txt /path/to/predicted/file.txt")
		sys.exit()

if __name__ == "__main__":
	main()