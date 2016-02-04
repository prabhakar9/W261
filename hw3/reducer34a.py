#!/usr/bin/python
## reducer34a.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW3.4
import sys

sys.stderr.write('reporter:counter:reducer,reducer34a,1\n')

prev_pair = None
counts = 0
total = 0
for line in sys.stdin:
    pair, value = line.strip().split('\t')
    
    if prev_pair != pair:
        if prev_pair is not None:
            print prev_pair + '\t' + str(counts)
        counts = 0
        prev_pair = pair
    counts += eval(value)
print prev_pair + '\t' + str(counts)