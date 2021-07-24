"""
059
Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly

"""

import random

correct = False
while not correct:
    # list of colors
    colors = ["red", "orange", "brown", "white", "black"]
    computerChoice = random.choice(colors)

    userColor = input("please select your favorite color: ")
    if userColor == computerChoice:
        print("well done")
        correct = True
    else:
        print("I bet you are", computerChoice, "with envy")
        correct = False
