#!/usr/bin/python
## reducer32d.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW3.2d
import sys

sys.stderr.write('reporter:counter:reducer,Reducer32d,1\n')

total = 0
for line in sys.stdin:
    value, word = line.strip().split('\t')
    # First word should be 0000TOTALWORDS
    if word == '0000TOTALWORDS':
        total = int(value)        
    else:
        term_freq = 100.0 * int(value)/total
        print word.ljust(20) + '\t' + value + '\t' + str(round(term_freq,4)) + '%'