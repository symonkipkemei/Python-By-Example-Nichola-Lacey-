'''
My understanding of for loop is that
It allows one to loop through an iterable
Iterable can be a string,array, tuple,range of integers or list with items that can be looped through
'''


'''
035
Ask the user to enter
their name and then
display their name
three times.

'''

userName = input("please insert your name:")
for x in range(0, 3):
    print(userName)


'''
036
Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times.

'''


userNo = int(input("please insert your a number:"))

for y in range(0, userNo):
    print(userName)


'''
037
Ask the user to enter their name and display each letter in
their name on a separate line.
'''

for z in userName:
    print(z)

'''
038
Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.
'''

for y in range(0, userNo):
    for r in userName:
        print(r)

'''
039
Ask the user to enter a number between 1
and 12 and then display the times table for
that number.
'''

# ask for a number between 1 and 12
userNumbers = int(input("please insert a number between 1 and 12:"))

# est range
# loop through range
# for every loop variable,
# print loop variable multiplied by user number
for no in range(1, (userNumbers + 1)):
    print(no, "x", userNumbers)


'''
040
Ask for a number below 50 and then count down from
50 to that number, making sure you show the number
they entered in the output.
'''

# ask for number below 50
userNo50 = int(input("please insert number below 50:"))
# est a negative range to be used
range(userNo50, 0, -1)

# when counting downwards the range is reversed starting
# from the top number followed by the lower number
# then the variation length
for x in range(userNo50, 0, -1):
    print(x, "from", userNo50)

'''
041 
Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times
'''

# ask for number and name
userNambari = int(input("please insert a number: "))
userJina = input("please insert your name: ")
# check number condition is < 10
# if true
# print name 3 times by looping
if userNambari < 10:
    for x in range(0, userNambari):
        print(userJina)
# If false
# print "too high" 3 times by looping
else:
    for y in range(0, 3):
        print("Too high")

'''
042
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.
'''

# create variable total with 0
total = 0
# ask five numbers ( for loop input 5 times)
# Each time ask if they want that number added (y/n)
# if yes add
# if no do not add
for ask in range(0, 5):
    useNumber = int(input("please enter a number: "))
    uliza = input("Do you want the number added to the total? (y/n): ")
    if uliza == "y":
        total = total+useNumber
    else:
        total = total

# after looping, display  the total
print(total)

'''
043
Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”.

'''

# ask direction up or down (up or down)
direction = str.lower(input("which direction do you want to count? (up/down): "))
# if up
# ask for top number
# count from 1 to top number ( range 1 to (top number + 1 )
if direction == "up":
    topNumber = int(input("insert the top number: "))
    for x in range(1, (topNumber + 1)):
        print(x)
elif direction == "down":
    belowNumber = int(input("insert a number below 20: "))
    for s in range(20, (belowNumber-1), -1):
        print(s)

# if down
# ask for number below 20
# count down from 20 to that number
# if they entered sth else print i don't understand
else:
    print(" I don\'t understand")


'''
044
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.

'''

# ask number of party goers
# if below 10
# ask for name
# print below [name] has been invited
# if number larger 10, display too many people

partyGoers = int(input("how many people are attending the party?: "))
if partyGoers < 10:
    for z in range(0, partyGoers):
        goersName = input("please insert their name")
        print("[", goersName, "] has been invited")

else:
    print("Too many people")