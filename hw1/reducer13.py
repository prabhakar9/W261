#!/usr/bin/python
## reducer13.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW1.3

import sys
import math

def isspam(true_class):
    if true_class == 1:
        return 'SPAM'
    else:
        return 'HAM'

filenames = sys.argv[1:]

spam_email_count = 0
ham_email_count = 0

spam_word_count = 0
ham_word_count = 0

spam_findword_count = 0
ham_findword_count = 0

total_cases = 0
correct_cases = 0

for filename in filenames:
    with open(filename, "r") as myfile:
        for line in myfile:
            tokens = line.split('\t')
            doc_id = tokens[0]
            true_class = int(tokens[1])
            findword = tokens[2]
            findword_count = int(tokens[4])
            word_count = int(tokens[3])
            
            if true_class == 1:
                spam_email_count += 1
                spam_word_count += word_count
                spam_findword_count += findword_count
            else:
                ham_email_count += 1
                ham_word_count += word_count
                ham_findword_count += findword_count

spam_prior = math.log((1.0*spam_email_count)/(spam_email_count + ham_email_count))
ham_prior = math.log((1.0*ham_email_count)/(ham_email_count + spam_email_count))

spam_findword_prob = math.log((1.0*spam_findword_count/spam_word_count))
ham_findword_prob = math.log((1.0*ham_findword_count/ham_word_count))

# Naive Bayes classification
for filename in filenames:
    with open(filename, "r") as myfile:
        for line in myfile:
            total_cases += 1
            tokens = line.split('\t')
            doc_id = tokens[0]
            true_class = int(tokens[1])
            findword_count = int(tokens[4])
            
            spam_doc_prob = spam_prior + spam_findword_prob*findword_count
            ham_doc_prob = ham_prior + ham_findword_prob*findword_count
            
            result = doc_id.ljust(30) + '\t\t' + isspam(true_class) + '\t\t'
            if spam_doc_prob > ham_doc_prob:
                predicted = 1
            else:
                predicted = 0
            result += isspam(predicted)
            print result
            
            if true_class == predicted:
                correct_cases += 1

accuracy = 1.0*correct_cases/total_cases
print "-----------------------"
print "Accuracy: " + str(accuracy*100) + '%'
            