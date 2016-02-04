#!/usr/bin/python
## mapper13.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW1.3

import sys
import re
import string

## collect user input
filename = sys.argv[1]
findwords = re.split(" ",sys.argv[2].lower())

with open (filename, "rU") as myfile:
    for line in myfile:
        tokens = line.lower().split('\t')
        word_string = tokens[2] + ' ' + tokens[3].strip()
        word_string = word_string.translate(string.maketrans("",""), string.punctuation)
        
        for word in findwords:
            key = tokens[0] + '\t' + tokens[1] + '\t' + word + '\t' + str(len(word_string.split()))
            print key + '\t' + str(word_string.count(word))
            