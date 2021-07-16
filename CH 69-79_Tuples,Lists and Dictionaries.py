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


