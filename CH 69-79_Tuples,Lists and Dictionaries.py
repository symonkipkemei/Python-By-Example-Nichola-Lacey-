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







