from sys import argv
#alright this imports the argu function from "sys" module
script, input_file = argv
#script is the name of python script and argv will be our
#text file that we open along with the script
def print_all(f):
    print (f.read())
#this is a function that opens our text file and reads
#the strings

def rewind(f):
    f.seek(0)
#I think is function reads our text file line
#or it does restarts the file back to its first character
def print_a_line(line_count, f):
    print (line_count, f.readline())
#it looks like this function prints out the line #
#along with what's one the actual line
current_file = open(input_file)
# this is our first script that assigns our text(txt) to
# a variable
print ("First let's print the whole file: \n")
#just a print statement
print_all(current_file)
#Now we call one of our functions and it read our entire
#txt file
print ("Now let's rewind, kind of like a tape. \n")
#just a print statement
#this helps us know where we are when looking at the
#terminal when our file is running
rewind(current_file)
#we call our next functions
print ("Let's print three lines: ")
#print statement
current_line = 1
print_a_line(current_line, current_file)
#we now set a variable
#the we call our function with a couple of set variables
current_line = current_line + 1
print_a_line(current_line, current_file)
#rinse and repeat with a new variable
current_line = current_line + 1
print_a_line(current_line, current_file)
#rinse and repeat with a new variable 
