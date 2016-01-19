#!/usr/bin/python
## reducer.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW1.2-1.4

import sys

filenames = sys.argv[1:]

word_count = {}

for filename in filenames:
    with open(filename, "rU") as myfile:
        for line in myfile:
            word, value = line.split('\t', 1)
            if word not in word_count:
                word_count[word] = int(value)
            else:
                word_count[word] += int(value)

for word in word_count:
    print word + '\t' + str(word_count[word])
    