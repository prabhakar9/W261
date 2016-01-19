#!/usr/bin/python
## reducer13.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW1.4

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

spam_findword = {}
ham_findword = {}

total_cases = 0
correct_cases = 0

for filename in filenames:
    with open(filename, "r") as myfile:
        for line in myfile:
            tokens = line.split('\t')
            doc_id = tokens[0]
            true_class = int(tokens[1])
            #findword = tokens[3]
            #findword_count = int(tokens[4])
            word_count = int(tokens[2])
            
            if true_class == 1:
                spam_email_count += 1
                spam_word_count += word_count
            else:
                ham_email_count += 1
                ham_word_count += word_count
            
            if len(tokens) > 3:
                for i in range(3, len(tokens), 2):
                    findword = tokens[i]
                    findword_count = int(tokens[i+1])
                    
                    if true_class == 1:
                        if findword not in spam_findword:
                            spam_findword[findword] = findword_count
                        else:
                            spam_findword[findword] += findword_count
                    else:
                        if findword not in ham_findword:
                            ham_findword[findword] = findword_count
                        else:
                            ham_findword[findword] += findword_count

print "spam_email_count: ", spam_email_count
print "ham_email_count: ", ham_email_count
print "spam_word_count: ", spam_word_count
print "ham_word_count: ", ham_word_count

spam_prior = math.log((1.0*spam_email_count)/(spam_email_count + ham_email_count))
ham_prior = math.log((1.0*ham_email_count)/(ham_email_count + spam_email_count))
spam_findword_prob = {}
ham_findword_prob = {}

print "spam_prior: ", spam_prior
print "ham_prior: ", ham_prior

for word in spam_findword:
    if spam_findword[word] > 0:
        spam_findword_prob[word] = math.log((1.0*spam_findword[word]/spam_word_count))
    else:
        spam_findword_prob[word] = float('-inf')
for word in ham_findword:
    if ham_findword[word] > 0:
        ham_findword_prob[word] = math.log((1.0*ham_findword[word]/ham_word_count))
    else:
        ham_findword_prob[word] = float('-inf')

# Naive Bayes classification
for filename in filenames:
    with open(filename, "r") as myfile:
        for line in myfile:
            total_cases += 1
            tokens = line.split('\t')
            doc_id = tokens[0]
            true_class = int(tokens[1])
            vocab = {}
            if len(tokens) > 3:
                for i in range(3, len(tokens), 2):
                    findword = tokens[i]
                    findword_count = int(tokens[i+1])
                    vocab[findword] = findword_count
            
            spam_doc_prob, ham_doc_prob = 0.0, 0.0
            for key, value in vocab.iteritems():
                if spam_findword_prob[key] == float('-inf'):
                    if value == 0:
                        spam_doc_prob += 0
                    else:
                        spam_doc_prob += float('-inf')
                else:
                    spam_doc_prob += spam_findword_prob[key]*value

            for key, value in vocab.iteritems():
                if ham_findword_prob[key] == float('-inf'):
                    if value == 0:
                        ham_doc_prob += 0
                    else:
                        ham_doc_prob += float('-inf')
                else:
                    ham_doc_prob += ham_findword_prob[key]*value
                    
            spam_doc_prob += spam_prior
            ham_doc_prob += ham_prior
            
            result = doc_id.ljust(30) + '\t\t' + isspam(true_class) + '\t\t'
            if spam_doc_prob > ham_doc_prob:
                predicted = 1
            else:
                predicted = 0
            result += isspam(predicted)
            print result

            if true_class == predicted:
                correct_cases += 1

accuracy = 100.0*correct_cases/total_cases
print "-----------------------"
print "Accuracy: " + str(accuracy) + '%'

            