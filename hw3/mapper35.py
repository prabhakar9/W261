#!/usr/bin/python
#HW 3.5

import sys
sys.stderr.write("reporter:counter:Calls,mapper_calls,1\n")
linecount = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    products = line.split(" ")
    products = sorted(products)
    linecount += 1   
    # emit the product
    for item in products:
        for item2 in products[products.index(item)+1:]:
            print "%s,%s\t1" % (item, item2)
    
print "linecount\t"+str(linecount)