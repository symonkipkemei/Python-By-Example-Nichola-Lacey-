"""
069
Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.

"""

countries = ("Kenya", "Uganda", "Tanzania", "Cameroon", "Sudan")
print(countries)

userInput = input("Enter one of the countries displayed above: ")
userInput = str.capitalize(userInput)
if userInput in countries:
    print(userInput, "is index number", countries.index(userInput))
else:
    print("wrong input")

'''
070
Add to program 069 to ask the
user to enter a number and
display the country in that
position.
'''

userNo = int(input("enter a number: "))

if 0 <= userNo <= 4:
    print(countries[userNo])

else:
    print("Number out of range")

'''
071
Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.

'''

sports = ["football", "basketball"]
userSport = input("what is your favorite sport?")

sports.append(userSport)

print(sorted(sports))

'''
072
Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again.
'''

subjects = ["Maths", "English", "history", "Geography", "Chemistry"]
print(subjects)
subjectDislike = input("which subject don\'t you like?: ")
# list followed by an attribute (index) then when you insert the name of the item, you get the index of the item
index = subjects.index(subjectDislike)
del subjects[index]

print(subjects)



'''

074
Enter a list of ten colours.
Ask the user for a starting
number between 0 and 4
and an end number
between 5 and 9. Display
the list for those colours
between the start and end
numbers the user input.
'''

colors = ["red", "yellow", "green", "orange", "brown", "purple", "white", "blue", "pink", "black"]
startNo = int(input("enter a number between 0 and 4: "))
endNo = int(input("enter a number between 5 and 9: "))
print(colors[startNo + 1:endNo])



'''
075
Create a list of four three-digit
numbers. Display the list to the
user, showing each item from
the list on a separate line. Ask
the user to enter a three-digit
number. If the number they
have typed in matches one in
the list, display the position of
that number in the list,
otherwise display the message
“That is not in the list”.
'''

num = [356, 789, 678, 453]
for x in num:
    print(x)
userNum = int(input("Enter a number: "))

if userNum in num:
    print("The number is in index position", num.index(userNum))
else:
    print("That is not in the list")

'''
076
Ask the user to enter the names of three people they want to
invite to a party and store them in a list. After they have entered
all three names, ask them if they want to add another. If they do,
allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party.
'''

'''
077
Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again.
'''

invitationCard = []
for x in range(0,3):
    invitee = input("Enter the name of your invitee: ")
    invitationCard.append(invitee)

print(invitationCard)

correct = False

while not correct:
    option = input("Do you want to invite another person? (y/n): ")
    if option == "y":
        invitee = input("Enter the name of your invitee: ")
        invitationCard.append(invitee)
    elif option == "n":
        print("You have invited", len(invitationCard), "people")
        correct = True
    else:
        print("You entered a wrong input")


print(invitationCard)
userType = input("Type one of the names on the list: ")
print(invitationCard.index(userType))
cancelOrNot = input("Do you still want that person to come to the party?(y)es or (n)o: ")
if cancelOrNot == "n":
    del invitationCard[invitationCard.index(userType)]
    print(invitationCard)
else:
    print(invitationCard)


'''

078
Create a list containing the titles of
four TV programmes and display
them on separate lines. Ask the
user to enter another show and a
position they want it inserted into
the list. Display the list again,
showing all five TV programmes in
their new positions.
'''

tvPrograms = ["Zora", "Passion", "Tahidi", "Roy"]
for x in tvPrograms:
    print(x)

anotherShow = input("Enter another show: ")
showPosition = int(input("which position do you want it added?: "))

# if you want to add an item to a list with a pre determined position,
# use attribute insert() instead of attribute append().
# the attribute append does not support the position object
tvPrograms.insert(showPosition, anotherShow)
print(tvPrograms)



'''

079
Create an empty list called “nums”.
Ask the user to enter numbers.
After each number is entered, add
it to the end of the nums list and
display the list. Once they have
entered three numbers, ask them if
they still want the last number they
entered saved. If they say “no”,
remove the last item from the list.
Display the list of numbers.
'''

num = []

for x in range(0, 3):
    userNum = int(input("enter a number: "))
    num.append(userNum)
print(num)
option = input("Do you still want the last number saved? (y)es or (n)o : ")
if option == "n":
    num.remove(userNum)

print(num)



