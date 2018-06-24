import json
import urllib

address = raw_input('Enter website: ')


url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data
info = json.loads(data)

#print info
lst = list()

#print info['comments'][1]
for c in info['comments']:
    lst.append(int(c['count']))

print lst
print "Sum of counts:", sum(lst)