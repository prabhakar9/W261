#!/usr/bin/python
## reducer34b.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW3.4
import sys

sys.stderr.write('reporter:counter:reducer,Reducer34b,1\n')

total = 0
for line in sys.stdin:
    value, pair = line.strip().split('\t')
    # First word should be 0000TOTALWORDS
    if pair == '0000RECORDCOUNT':
        total = int(value)
    else:
        term_freq = round(100.0 * int(value)/total, 3)
        print pair.ljust(20) + '\t' + value + '\t' + str(term_freq) + '%'