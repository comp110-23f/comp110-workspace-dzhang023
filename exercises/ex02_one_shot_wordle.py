"""Docstring."""
__author__ = "730630815"
index : int = 0
boxoutput : str = ''
secret : str = "python"
guess : str = input("What is your 6-letter guess? ")
while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")
while index != len(secret):
    if secret[index] == guess[index]:
        boxoutput += "\U0001F7E9"
    elif guess[index] in secret:
        boxoutput += "\U0001F7E8"
    else:
        boxoutput += "\U00002B1C"
    index += 1
print(boxoutput)
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")