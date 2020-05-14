# Author: Samantha MacIlwaine
# Copyright 2020
# Contact: srm2197@columbia.edu

# before we move to testing
# # Take prepared test files and split into 2 files: a partial and regular
# Put the regular in testing-files
# And put the partial in partialized

# script input partial_output rest_of_output
python3 scripts/partialize.py corpus/fisher_test.en.0 src/partialized-files/fisher_test_partial.en.0 corpus/fisher_test.en.0 src/partialized-files/original-partials/fisher_test_partial.en.0 100
python3 scripts/partialize.py corpus/fisher_test.en.1 src/partialized-files/fisher_test_partial.en.1 corpus/ready/fisher_test.en.1 src/partialized-files/original-partials/fisher_test_partial.en.1 90
python3 scripts/partialize.py corpus/fisher_test.en.2 src/partialized-files/fisher_test_partial.en.2 corpus/ready/fisher_test.en.2 src/partialized-files/original-partials/fisher_test_partial.en.2 80
python3 scripts/partialize.py corpus/fisher_test.en.3 src/partialized-files/fisher_test_partial.en.3 corpus/ready/fisher_test.en.3 src/partialized-files/original-partials/fisher_test_partial.en.3 70

# Clean the files
python3 scripts/clean.py corpus/fisher_train.en segmenter/training-files/fisher_train.txt
python3 scripts/clean.py corpus/ready/fisher_test.en.0 scripts/testing-files/fisher_test_0.txt
python3 scripts/clean.py corpus/ready/fisher_test.en.1 scripts/testing-files/fisher_test_1.txt
python3 scripts/clean.py corpus/ready/fisher_test.en.2 scripts/testing-files/fisher_test_2.txt
python3 scripts/clean.py corpus/ready/fisher_test.en.3 scripts/testing-files/fisher_test_3.txt