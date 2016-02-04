#!/usr/bin/python
## mapper32b.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW3.2b
import sys
import string

sys.stderr.write('reporter:counter:mapper32b,Mapper,1\n')
total_words = 0
for line in sys.stdin:
    tokens = line.strip().split(",")
    if 'Complaint' in tokens[0]:
        continue
    
    word_string = tokens[3].replace(',', ' ').replace('/', ' ').replace('"', '')
    for word in word_string.lower().split():
        total_words += 1
        print word + '\t' + str(1)
print '0000TOTALWORDS' + '\t' + str(total_words)