#!/usr/bin/python
## mapper.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW1.2-1.4

import sys
import re
import string

# test
#filename = 'enronemail_1h.txt'
#findwords = 'assistance'
#findwords = re.split(" ",findwords.lower())

## collect user input
filename = sys.argv[1]
findwords = re.split(" ",sys.argv[2].lower())

with open (filename, "rU") as myfile:
    for line in myfile:
        tokens = line.lower().split('\t')
        word_string = tokens[2] + ' ' + tokens[3].strip()
        word_string = word_string.translate(string.maketrans("",""), string.punctuation)
        
        for word in findwords:
            if word in word_string:
                print word + '\t' + str(word_string.count(word))