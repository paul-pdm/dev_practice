import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "sample1.txt"
handle = open(name)

counts = list()
numlist = list()
for line in handle:
	num = re.findall('[0-9]+',line)
	for n in num:
	    if n > 1:
	        counts.append(n)
print counts
for h in counts:
    numlist.append(int(h))
print sum(numlist)

#import re
#print sum( [ ****** *** * in re.findall('[0-9]+',**************************.read()) ] )