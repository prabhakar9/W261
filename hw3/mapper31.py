#!/usr/bin/python
## mapper31.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW3.1

import sys

for line in sys.stdin:
    tokens = line.strip().split(",")
    
    # Skip the Header
    if tokens[0] == 'Complaint ID':
        continue
    
    product = 'none'
    if 'Debt' in tokens[1]:
        product = 'debt'
    elif 'Mortgage' in tokens[1]:
        product = 'mortgage'
    else:
        product = 'others'
    
    sys.stderr.write("reporter:counter:MapperTokens," + product + ',1\n')
    print product + '\t' + str(1)