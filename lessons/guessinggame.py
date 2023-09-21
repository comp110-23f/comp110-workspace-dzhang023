"""Docstring."""
__author__ = '730630815'
from random import randint
secret: int = randint(1,10)
guess = 0
guess = int(input("Guess a num between 1-10: "))
while guess != secret:
    guess = int(input("wrong asf, guess again: "))
print("grats")
