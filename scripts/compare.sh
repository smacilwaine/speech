# Author: Samantha MacIlwaine
# Copyright 2020
# Contact: srm2197@columbia.edu

# concatenate src/prediction-file with src/partialized_file
# concatenate.py --> create tmp concatenation


# Append question predictions to non-question predictions
cat ../src/partialized-files/fisher_test_partial.en.0 >> ../src/prediction-files/fisher_test_0.txt.pred.txt 
cat ../src/partialized-files/fisher_test_partial.en.1 >> ../src/prediction-files/fisher_test_1.txt.pred.txt 
cat ../src/partialized-files/fisher_test_partial.en.2 >> ../src/prediction-files/fisher_test_2.txt.pred.txt 
cat ../src/partialized-files/fisher_test_partial.en.3 >> ../src/prediction-files/fisher_test_3.txt.pred.txt 


# Append original question results to original file for comparison
cat ../src/partialized-files/original-partials/fisher_test_partial.en.0 >> testing-files/fisher_test_0.txt
cat ../src/partialized-files/original-partials/fisher_test_partial.en.1 >> testing-files/fisher_test_1.txt
cat ../src/partialized-files/original-partials/fisher_test_partial.en.2 >> testing-files/fisher_test_2.txt
cat ../src/partialized-files/original-partials/fisher_test_partial.en.3 >> testing-files/fisher_test_0.txt

# statistics.py automaticall produces results file

python3 get_statistics.py testing-files/fisher_test_0.txt ../src/prediction-files/fisher_test_0.txt.pred.txt
python3 get_statistics.py testing-files/fisher_test_1.txt ../src/prediction-files/fisher_test_1.txt.pred.txt
python3 get_statistics.py testing-files/fisher_test_2.txt ../src/prediction-files/fisher_test_2.txt.pred.txt
python3 get_statistics.py testing-files/fisher_test_3.txt ../src/prediction-files/fisher_test_3.txt.pred.txt

