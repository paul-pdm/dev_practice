x = "There are %d types of people." % 10
#This a string with a variable place holder
binary = "binary"
#this is a variable
do_not = "don't"
# this is another variable
y = "Those who know %s and those who %s" % (binary, do_not)
#this a string with 2 variables

print (x)
print (y)
#these print out the strings along with the according variables

print ("I said: %r." % x)
print ("I also said: '%s'." % y)
#these print a string with other string variables

hilarious = False
joke_evaluation = "Isn't that joke so funny!? %r"
#variables...strings...i think you get the theme by  now

print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."
# just two strings as variables....

print (w + e)
#catation = two strings added together
