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

