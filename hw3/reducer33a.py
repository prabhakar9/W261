#!/usr/bin/python
## reducer33.py
## Author: Prabhakar Gundugola
## Description: reducer code for HW3.3
import sys

sys.stderr.write('reporter:counter:reducer,reducer33,1\n')
prev_product = None
counts = 0
total = 0
unique_count = 0
largest_basket = 0
for line in sys.stdin:
    product, value = line.strip().split('\t')
    if prev_product != product:
        if prev_product is not None:
            if prev_product != '0000LARGESTBASKET':
                print prev_product + '\t' + str(counts)
                if prev_product != '0000TOTALWORDS':
                    unique_count += 1
            else:
                print prev_product + '\t' + str(largest_basket)
                       
        prev_product = product
        counts = 0
    if product == '0000LARGESTBASKET':
        if int(value) > largest_basket:
            largest_basket = int(value)
    else:
        counts += int(value)
unique_count += 1
print prev_product + '\t' + str(counts)
print '0000UNIQUECOUNT' + '\t' + str(unique_count)