'''
105
Write a new file
called
“Numbers.txt”.
Add five numbers
to the document
which are stored
on the same line
and only
separated by a
comma. Once you
have run the
program, look in
the location where
your program is
stored and you
should see that
the file has been
created. The
easiest way to
view the contents
of the new text file
on a Windows
system is to read it
using Notepad.
'''

# create a file
# therefore assign a variable to open a file
num = [1, 56, 67, 34, 34]
file = open("Numbers.txt", "w")

# the function above first writes all the variables in to the loop before saving
for x in num:
    file.write(str(x) + ",")

file.close()
# The function file close not only closes the file but also saves the changes

num1 = [43, 67, 76, 54, 90, 23]

for x in num1:
    file = open("Numbers.txt", "a")
    file.write(str(x) + ",")
    file.close()
# the function above appends individual data into the text file

'''
106
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.
'''

# create a new file
names = open("Names.txt", "w")

namesAdded = ["sam", "kipchumba", "soma", "were", "samido", "erastus"]

for y in namesAdded:
    names.write(y + "\n")
names.close()

'''
107
Open the
Names.txt
file and
display
the data
in Python.
'''

names = open("Names.txt", "r")
print(names.read())
names.close()
'''
108
Open the Names.txt file. Ask the user to input a
new name. Add this to the end of the file and
display the entire file.
'''
names = open("Names.txt", "a")
newName = input("input a new name: ")
names.write(newName + "\n")
names.close()

names = open("Names.txt", "r")
print(names.read())
names.close()

