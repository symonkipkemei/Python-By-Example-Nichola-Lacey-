'''
110
Using the Names.txt file you
created earlier, display the list of
names in Python. Ask the user to
type in one of the names and then
save all the names except the one
they entered into a new file called
Names2.txt
'''

names = open("Names.txt","r")
print(names.read())

userType = input("Type one of the names:")

for x in names:
    print(x)


n = open("Names2.txt", "r")
print(n.read())


