#!/usr/bin/python
#HW 3.5

import sys
topN = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    if topN < 50:
        print line
        topN += 1