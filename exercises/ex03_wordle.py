"""Docstring."""
__author__ = '730630815'
def contains_char(word, letter:str) -> bool:
    assert len(letter) == 1
    letterinword = False
    index = 0
    while index != len(word):
        if word[index] == letter:
            letterinword = True
        index += 1
    return letterinword
def emojified(guessword:str, secretword:str) -> str:
    assert len(guessword) == len(secretword)
    boxoutput = ''
    index = 0
    while index != len(guessword):
        if guessword[index] == secretword[index]:
            boxoutput += "\U0001F7E9"
        elif contains_char(secretword, guessword[index]):
            boxoutput += "\U0001F7E8"
        else:
            boxoutput += "\U00002B1C"
        index += 1
    return boxoutput
def input_guess(properlen: int) -> str:
    guess = input(f'Enter a {properlen} letter word: ')
    while len(guess) != properlen:
        guess = input(f"That wasn't {properlen} chars! Try again: ")
    return guess
def main() -> None:
    secret = 'codes'
    guess = ''
    index = 0
    while index != 7:
        print(f'=== Turn {index}/6 ===')
        guess = input_guess(len(secret))
        print(emojified(guess,secret))
        if guess == secret:
            print(f"You won in {index}/6 turns!")
            break
        index += 1
    if guess != secret:
        print('X/6 - Sorry, try again tomorrow!')
if __name__ == "__main__":
    main()