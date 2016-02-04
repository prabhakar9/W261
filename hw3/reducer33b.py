#!/usr/bin/python
## reducer33b.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW3.3
import sys

sys.stderr.write('reporter:counter:reducer,Reducer32d,1\n')

total = 0
for line in sys.stdin:
    value, word = line.strip().split('\t')
    # First word should be 0000TOTALWORDS
    if word == '0000TOTALPRODUCTS':
        total = int(value)
    elif word == '0000UNIQUECOUNT':
        print word.ljust(20) + '\t' + value
    elif word == '0000LARGESTBASKET':
        print word.ljust(20) + '\t' + value
    else:
        term_freq = round(100.0 * int(value)/total, 3)
        print word.ljust(20) + '\t' + value + '\t' + str(term_freq) + '%'