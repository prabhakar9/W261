#!/usr/bin/python
## mapper32a.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW3.2
import sys

sys.stderr.write('reporter:counter:mapper,Mapper,1\n')

for line in sys.stdin:
    words = line.strip().split()
    
    for word in words:
        print word + '\t' + str(1)        