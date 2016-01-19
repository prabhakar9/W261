#!/usr/bin/python
## mapper14.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW1.4

import sys
import re
import string

## collect user input
filename = sys.argv[1]
findwords = re.split(" ",sys.argv[2].lower())

with open (filename, "r") as myfile:
    for line in myfile:
        tokens = line.lower().split('\t')
        word_string = tokens[2] + ' ' + tokens[3].strip()
        word_string = word_string.translate(string.maketrans("",""), string.punctuation)
        
        key = tokens[0] + '\t' + tokens[1] + '\t' + str(len(word_string.split()))
        for word in findwords:
            key += '\t' + word + '\t' + str(word_string.count(word))
        print key
            