#!/usr/bin/python
## reducer32b.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW3.2b
import sys

sys.stderr.write('reporter:counter:reducer32b,Reducer,1\n')
prev_word = None
counts = 0

for line in sys.stdin:
    word, value = line.strip().split('\t')
    
    if prev_word != word:
        if prev_word is not None:
            print prev_word + '\t' + str(counts)
        prev_word = word
        counts = 0
    counts += eval(value)
print prev_word + '\t' + str(counts)