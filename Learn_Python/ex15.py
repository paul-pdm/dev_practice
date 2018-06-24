from sys import argv
#this imports arguments from the system module
script, filename = argv
#this requires the user to enter arguments from these variables

txt = open(filename)
#this opens a file and assigns it to a variable
print ("Here's your file %r:" % filename)
print (txt.read())
#this prints out the variable aka the text file
txt.close()
print ("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)
#this just assigns a "new file"
print (txt_again.read())
#and this just opens it
txt_again.close()
#whenever you open a file, close it afterwards....
