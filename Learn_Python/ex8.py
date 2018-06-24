formatter = "%r %r %r %r"

print (formatter % (1,2,3,4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
#this is just kinda meta
print (formatter %(
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight"
))
#we see single quotes because we is that it's represented
#by a string and not a number or symbol
