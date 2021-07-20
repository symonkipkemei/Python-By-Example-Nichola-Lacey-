'''
102
Ask the user to enter the name, age and shoe size for four
people. Ask for the name of one of the people in the list and
display their age and shoe size.
'''

print("Input name, age and shoe size data for four people")
listA = {}
for y in range(0, 4):
    name = input("Input your name: ")
    age = input("Input your age: ")
    shoeSize = input("Input your shoe size: ")
    listA[name] = {"age": age, "shoeSize": shoeSize}
    # this line of code updates the dict with a new pair of key and data

print(listA)
userName = input("enter name of one person in the list: ")
print(listA[userName])
print(listA)

'''
103
Adapt program 102
to display the
names and ages of
all the people in
the list but do not
show their shoe
size.
'''

for y in listA:
    print(y, listA[y]["age"])


'''
104
After gathering the four names, ages and shoe sizes, ask the
user to enter the name of the person they want to remove from
the list. Delete this row from the data and display the other rows
on separate lines
'''

removeName = input("input the name you want removed:")


del listA[removeName]

for x in listA:
    print(x, listA[x]["age"], listA[x]["shoeSize"])
