


### 'punctuate.py' punctuates the model
### this is what we will edit
### basically, we will 

(1) use the original test file to check for which lines include question marks
(2) remove all of these corresponding lines from the unpunctuated test file, creating modified_test
(3) 





BEFORE YOU TURN IT IN

-- restore training data in to_be_cleaned folder to original length


-----------------------------------

srm2197
Samantha MacIlwaine
14 May 2020
****************************PROJECT TITLE
jfkdsjfldsa;f

**************************** PROJECT ABSTRACT
akdsjlfsj;afdjf

TOOLS NEEDED:
* All dependency installation requirements listed in this open-source code:
--> https://github.com/michaelbironneau/rnn-punctuation
* Python 3
* Keras
* Tensorflow
* NLTK
* ffmpy
* pydub


!!!!!!!!!!!!!!!
IMPORTANT: Please read the ENTIRE instructions before you begin.
You may not want to run all of the commands, to save time.
We recommend using a pre-saved model in /models if your machine does not have a GPU.
!!!!!!!!!!!!!!!

NOTE: All file names and directory names not listed below are already hardcoded and need not be edited.

Instructions:
===================================

1 *******
Complete all downloads and installations from the above URL.

******* START HERE TO BUILD THE MODEL FROM SCRATCH *********

2 *******
From the root directory, run these commands in sequence:
./scripts/normalize.sh
./scripts/clean.sh
./segmenter/top_n_corpus.sh

3 *******
cd segmenter
From the /segmenter directory, run these commands in sequence:
./create-trainingset.sh
python3 model.py train data/fisher_train.txt

# shortened training file is 1105071 bytes

If the last command fails for lack of memory, run this instead, multiple times:
find data/fisher_train.txt | head -c 7000000 | xargs python3 model.py train

If that command also fails, then exchange 7000000 for a smaller number until it works.
It will depend on the memory size of your machine.

******* START HERE IF THE MODEL IS ALREADY PRE-TRAINED *********
If there exists a segmenter/model.h5 file, then the model is already pre-trained and you can skip the steps above.

4 ******
From the root directory, run these commands in sequence:
./scripts/prepare_test_files.sh

Intermediate step: If you're building a custom model instead of importing the open-source pre-trained one, edit the model path field of 'options.txt' to be to '../segmenter/model.h5' before running Step 5.

5 *******
cd src
From the src directory, run these commands in sequence:
python3 run.py options.json

******* START HERE IF TESTS ARE ALREADY COMPLETED *********
The tests are already completed if the segmenter/prediction_files directory contains any files, and you can skip the steps above.

6 *******
cd ../scripts
From the scripts directory, run these commands in sequence:
./compare.sh
Then navigate to src/results-files to view the results.

Overview of Original Authored Scripts
=====================================

1. clean.sh -> runs clean.py for on the training data
2. clean.py -> removes all punctuation except for ,.?! on the training data
3. prepare_test_files.sh -> runs all test files through unpunctuate.py
4. unpunctuate.py -> removes punctuation (and optionally converts all characters to lowercase) from file
5. space_punctuation.py -> inserts buffer around every punctuation mark to mimic prepared-training-data format
6. compare -> runs get_statistics.py for every original-predicted test file combination
6. get_statistics.py -> performs comparative statistical analysis on original and predicted files
7. normalize.sh -> runs clean.py then normalize.py on both training and test data
8. normalize.py -> fits file to a 50-50 distribution of periods approximately equal to the number of question marks, not counting commas
9. partialize.py -> split question-turn sentences from non-question sentences based on output accuracy variable

Overview of Improved Open-Source Scripts
=========================================

1. run.py -> (1) completely reworked to prepare processed test files for comparison and analysis, (2) created new subscriptable transcription object that functioned in tandem with all other codes, (3) sorted and processed multiple output files to prepare for data extraction, (4) eliminated unnecessary & expensive processes like converting to docx
2. model.py -> (1) expanded set of ignored tokens to limit model's output vocabulary to just 3 target punctuation symbols, (2) redirected output to prediction file set for further analysis
3. punctuate.py -> (1) expanded set of ignored tokens to limit model's output vocabulary to just 3 target punctuation symbols, (2) redirected output from string to file for further manipulation, and (3) disabled tendency of the prediction function to automatically add periods to the end of sentences (which was largely skewing the data by increasing the number of periods overall)
3. fix_spacing.py -> added multiple characters to replacement schema
4. options.json -> converted text_file field into a list







