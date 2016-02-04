#!/usr/bin/python
#HW 3.5

import sys

sys.stderr.write("reporter:counter:Calls,reducer_calls,1\n")
stripes = {}
current_key = None
current_count = 0
key = None
linecount = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    key, count = line.split("\t", 1)
    count = int(count)
    
    if current_key == key:
        current_count += int(count)
    else:
        if current_key:
            items = current_key.split(",", 1)
            if len(items) == 2:
                stripes.setdefault(items[0], {})
                stripes[items[0]][items[1]]=current_count
            elif items[0] == "linecount":
                linecount = current_count
        current_count = count
        current_key = key

# output the last word
if current_key == key:
    items = current_key.split(",", 1)
    if len(items) == 2:
        stripes.setdefault(items[0], {})
        stripes[items[0]][items[1]]=current_count
    elif items[0] == "linecount":
        linecount = current_count
        

for key, stripe in stripes.items():
    marg_count = sum(stripe.values())
    for key2, count in stripe.items():
        if count >= 100:
            line_freq = round(100.0*count/marg_count, 4)
            #print "%s\t%s\t%s\t%.4f\t%.4f" % \
            #(key, key2, str(count), count*1.0/linecount, count*1.0/marg_count)
            print key + ', ' + key2 + '\t' + str(count) +'\t' + str(line_freq) + '%'