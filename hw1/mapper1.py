#!/usr/bin/python
## mapper.py
## Author: PG
## Description: mapper code for HW1.2

import sys
import re
import string

# Collect input
filename = sys.argv[1]
findwords = re.split(" ",sys.argv[2].lower())

# Initialize dictionary to empty
wordcount = {}

with open(filename, "rU") as myfile:
    for line in myfile:
        # Format each line, fields separated by \t according to enronemail_README.txt
        # Remove \n text at end of each line
        fields = line.split("\t")
        fields[3] = fields[3].replace("\n", "")
        subj = fields[2].translate(string.maketrans("",""), string.punctuation)
        body = fields[3].translate(string.maketrans("",""), string.punctuation)
        
        # For each word in list provided by user, count occurrences in subj and body
        for word in findwords:
            if word not in wordcount:
                wordcount[word] = 0 
            wordcount[word] += subj.count(word) + body.count(word)

for word in wordcount:
    print [word, wordcount[word]]