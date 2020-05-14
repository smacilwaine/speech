# Author: Samantha MacIlwaine
# Copyright 2020
# Contact: srm2197@columbia.edu

# replace files in 'original' folder with cleaned files (no extraneous punctuation marks)

python3 scripts/clean.py corpus/to_be_cleaned/fisher_train.en corpus/original/fisher_train.en
python3 scripts/clean.py corpus/to_be_cleaned/fisher_test.en.0 corpus/original/fisher_test.en.0
python3 scripts/clean.py corpus/to_be_cleaned/fisher_test.en.1 corpus/original/fisher_test.en.1
python3 scripts/clean.py corpus/to_be_cleaned/fisher_test.en.2 corpus/original/fisher_test.en.2
python3 scripts/clean.py corpus/to_be_cleaned/fisher_test.en.2 corpus/original/fisher_test.en.2

# normalize (shorten) files to represent 50% periods and 50% question marks as terminal sentence tokens

python3 scripts/normalize.py corpus/original/fisher_train.en corpus/fisher_train.en
python3 scripts/normalize.py corpus/original/fisher_test.en.0 corpus/fisher_test.en.0
python3 scripts/normalize.py corpus/original/fisher_test.en.1 corpus/fisher_test.en.1
python3 scripts/normalize.py corpus/original/fisher_test.en.2 corpus/fisher_test.en.2
python3 scripts/normalize.py corpus/original/fisher_test.en.3 corpus/fisher_test.en.3