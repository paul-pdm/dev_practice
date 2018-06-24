import urllib
import xml.etree.ElementTree as ET


address = raw_input('Enter website: ')


url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

lst = list()
for count in tree.iter('count'):
    lst.append(int(count.text))
print lst
print "Sum of comments:", sum(lst)
