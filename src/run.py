from punctuate import Punctuate 
from to_docx import ToDocX 
from to_text import ToText 
from to_wav import ToWav 
from capitalize import Capitalize
from fix_spacing import FixSpacing
from split_paragraphs import SplitParagraphs
from transcription import new_transcription, read_options
import sys, os
import logging

# Contributor: Samantha MacIlwaine
# Copyright 2020
# Contact: srm2197@columbia.edu

def test(test_file):
	logging.basicConfig(format='%(asctime)s %(message)s')

	if len(sys.argv) < 2:
		print("Usage python3 run.py /path/to/options/file")
		sys.exit(1)

	options = read_options(sys.argv[1])
	input_file_base = open(test_file, 'r')
	input_file = input_file_base.read().splitlines()
	transcription = {}
	paragraphs = {}

	i = 0
	while i < len(input_file):
		chunk = {}
		chunk['content'] = str(input_file[i])
		paragraphs[i] = chunk
		i += 1
	transcription['paragraphs'] = paragraphs

	# need: transcription[i][content] = line for that text

	#transcription = new_transcription(options['audio_file'], title=options['title'])
	#toWav = ToWav(**options)
	#toText = ToText(options['watson_credentials'], **options)
	#oDocx = ToDocX(**options)
	punc = Punctuate(options['punctuate_model'], options['wordlist'], **options)
	caps = Capitalize()
	space = FixSpacing()
	splitParas = SplitParagraphs(options['paragraph_splitter_model'], **options)

	#toDocx(splitParas(space(caps(punc(toText(toWav(transcription)))))))
	base=os.path.basename(test_file)
	output_file = open('prediction-files/'+base+'.pred.txt', 'w')

	final_trans = punc(transcription)
	print(len(final_trans))
	output_text = ''
	for i in range(len(final_trans['paragraphs'])):
		output_text += final_trans['paragraphs'][i]['content']+'\n'
	if len(output_text) > 0:
		output_file.write(output_text)
		#print(output_text)
	else:
		print("It didn't work.")


	logging.info('Done! Check output.txt')
	print('Added 1 prediction file to prediction-files.')
	output_file.close()
	input_file_base.close()

def main():
	options = read_options(sys.argv[1])
	for test_file in options['text_file']:
		test(test_file)

if __name__ == "__main__":
	main()
