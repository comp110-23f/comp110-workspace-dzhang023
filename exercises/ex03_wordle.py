"""Docstring."""
__author__ = '730630815'
def contains_char(word, letter:str) -> bool:
    assert len(letter) == 1
    return letter in word
def emojified(guessword:str, secretword:str) -> str:
    assert len(guessword) == len(secretword)
    boxoutput = ''
    for index, char in enumerate(guessword):
        if char == secretword[index]:
            boxoutput += "\U0001F7E9"
        elif contains_char(secretword, char):
            boxoutput += "\U0001F7E8"
        else:
            boxoutput += "\U00002B1C"
    return boxoutput
def input_guess(properlen: int) -> str:
    guess = input(f'Enter a {properlen} letter word: ')
    while len(guess) != properlen:
        guess = input(f"That wasn't {properlen} chars! Try again: ")
    return guess
def main() -> None:
    secret = 'codes'
    guess = ''
    for index in range(7):
        print(f'=== Turn {index}/6 ===')
        guess = input_guess(len(secret))
        print(emojified(guess,secret))
        if guess == secret:
            print(f"You won in {index}/6 turns!")
            break
    if guess != secret:
        print('X/6 - Sorry, try again tomorrow!')
if __name__ == "__main__":
    main()