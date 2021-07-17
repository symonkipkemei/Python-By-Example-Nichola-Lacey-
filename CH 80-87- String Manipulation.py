

print('''
080
Ask the user to enter their
first name and then display
the length of their first name.
Then ask for their surname
and display the length of
their surname. Join their first
name and surname together
with a space between and
display the result. Finally,
display the length of their full
name (including space)
''')

firstName = input("enter your first name: ")
print(len(firstName))

surname = input("enter your surname: ")
print(len(surname))
joinedName = firstName + " " + surname
print(joinedName)
print(len(joinedName))

'''
081
Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.

'''

favoriteSubject = input("enter your favorite subject: ")

for x in favoriteSubject:
    print(x, end="-")

# By adding end to the iterable item, they are no longer displayed each on their line but on one line


'''
082
Show the user a line of text from your favourite poem
and ask for a starting and ending point. Display the
characters between those two points.
'''

poemLine = " Without you, I cannot breathe, I need you in my life"
print(poemLine)
start = int(input("enter a starting point: "))
end = int(input("enter an ending point: "))

print(poemLine[start: end-1])


'''
083
Ask the user to type in a word in upper case. If they
type it in lower case, ask them to try again. Keep
repeating this until they type in a message all in
uppercase.
'''

correct = False
while not correct:
    word = input("Type a word in uppercase: ")
    if word.islower():
        print("try again")
        correct = False
    else:
        print("You got it correct,thanks.")
        correct = True

'''


084
Ask the user to type in their
postcode. Display the first
two letters in uppercase
'''

postcode = input("type in your postcode: ")
firstTwo = postcode[0:2]
print(firstTwo.upper())



'''

085
Ask the user to type in their name
and then tell them how many vowels
are in their name.
'''

firstName = input("enter your first name: ")

vowels = ["a", "e", "i", "0", "u"]
count = 0
for x in firstName:
    if x in vowels:
        count += 1

print("Your name has ", count, "vowels")



'''
086
Ask the user to enter a new password. Ask
them to enter it again. If the two passwords
match, display “Thank you”. If the letters are
correct but in the wrong case, display the
message “They must be in the same case”,
otherwise display the message “Incorrect”.
'''



correct = False

while not correct:
    pswd1 = input("Hello user, Enter your new password: ")
    pswd2 = input("Enter your password again: ")

    if pswd1 == pswd2:
        print("Correct, Thank you")
        correct = True

    elif pswd1.islower() and pswd2.isupper():
        print("They must be in the same case")
        correct = False

    elif pswd2.islower() and pswd1.isupper():
        print("They must be in the same case")
        correct = False

    else:
        print("Incorrect")
        correct = False
