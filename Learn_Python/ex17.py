from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

# we could do these on one line, how?
in_file = open(from_file)
indata = in_file.read()
#indata = (open(from_file, 'r'))

print ("The input file is %d bytes long" % len(indata))
#this doesn't work anymore for some reason?
#is it because of the way I'm opening the file....?

print ("Does the output file exists? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

print ("Alright, all done.")

out_file = open(to_file, 'w')
out_file.write(indata)
#out_file = (open(to_file, 'w')).write(indata)

out_file.close()
in_file.close()
