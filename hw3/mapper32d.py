#!/usr/bin/python
## mapper32d.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW3.2d that takes the output of HW3.2c as input
import sys

sys.stderr.write('reporter:counter:mapper,Mapper32d,1\n')

for line in sys.stdin:
    word, value = line.strip().split('\t')
    print value + '\t' + word