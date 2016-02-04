#!/usr/bin/python
## reducer.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW3.1

import sys

prev_word = None
counts = 0
for line in sys.stdin:
    word, value = line.strip().split('\t')
    
    if prev_word != word:
        if prev_word is not None:
            print prev_word + '\t' + str(counts)
            sys.stderr.write('reporter:counter:ReducerTokens,' 
                             + prev_word + ',' + str(counts) + '\n')
        
        prev_word = word
        counts = 0
    counts += 1

print prev_word + '\t' + str(counts)
sys.stderr.write('reporter:counter:ReducerTokens,' + prev_word + ',' + str(counts) + '\n')
        