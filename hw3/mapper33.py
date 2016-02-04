#!/usr/bin/python
## mapper33.py
## Author: Prabhakar Gundugola
## Description: mapper code for HW3.3
import sys

sys.stderr.write('reporter:counter:mapper,mapper33,1\n')
total_products = 0
basket = 0
largest_basket = 0
for line in sys.stdin:
    products = line.strip().split()
    for product in products:
        total_products += 1
        basket += 1
        print product + '\t' + str(1)
    if basket > largest_basket:
        largest_basket = basket
print '0000TOTALPRODUCTS' + '\t' + str(total_products)
print '0000LARGESTBASKET' + '\t' + str(largest_basket)