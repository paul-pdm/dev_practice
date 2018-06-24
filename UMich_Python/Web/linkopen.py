# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags

count = list()
tags = soup('a')
for tag in tags:
    count.append(tag.get('href', None))
print "1", count[17]

p2 = urllib.urlopen(count[17]).read()
soup2 = BeautifulSoup(p2, "html.parser")

count2 = list()
tags2 = soup2('a')
for tag in tags2:
    count2.append(tag.get('href', None))
print "2", count2[17]

p3 = urllib.urlopen(count2[17]).read()
soup3 = BeautifulSoup(p3, "html.parser")

count3 = list()
tags3 = soup3('a')
for tag in tags3:
    count3.append(tag.get('href', None))
print "3", count3[17]

p4 = urllib.urlopen(count3[17]).read()
soup4 = BeautifulSoup(p4, "html.parser")

count4 = list()
tags4 = soup4('a')
for tag in tags4:
    count4.append(tag.get('href', None))
print "4", count4[17]

p5 = urllib.urlopen(count4[17]).read()
soup5 = BeautifulSoup(p5, "html.parser")

count5 = list()
tags5 = soup5('a')
for tag in tags5:
    count5.append(tag.get('href', None))
print "5", count5[17]

p6 = urllib.urlopen(count5[17]).read()
soup6 = BeautifulSoup(p6, "html.parser")

count6 = list()
tags6 = soup6('a')
for tag in tags6:
    count6.append(tag.get('href', None))
print "6", count6[17]

p7 = urllib.urlopen(count6[17]).read()
soup7 = BeautifulSoup(p7, "html.parser")

count7 = list()
tags7 = soup7('a')
for tag in tags7:
    count7.append(tag.get('href', None))
print "7", count7[17]