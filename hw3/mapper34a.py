#!/usr/bin/python
## mapper34a.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW3.4
import sys
import itertools

sys.stderr.write('reporter:counter:mapper,mapper34a,1\n')

record_count = 0

for line in sys.stdin:
    products = line.strip().split()
    
    product_pairs = list(itertools.combinations(set(products),2))
    
    for product_pair in product_pairs:
        pair = sorted(product_pair)
        print pair[0] + ', ' + pair[1] + '\t' + str(1)
    
    record_count += 1

print '0000RECORDCOUNT' +'\t' + str(record_count)