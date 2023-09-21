"""Docstring."""
__author__ = '730630815'


def contains_char(word: str, letter: str) -> bool:
    """Finds if a given letter is in a given word."""
    assert len(letter) == 1
    letterinword = False
    index = 0
    while index != len(word):
        if word[index] == letter:
            letterinword = True
        index += 1
    return letterinword


def emojified(guessword: str, secretword: str) -> str:
    """Gives the boxes that indicate the correctness of each guess."""
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
    """Ensures that the guess is the proper length."""
    guess = input(f'Enter a {properlen} letter word: ')
    if guess.isalpha() and len(guess) == properlen:
        return guess
    else:
        while len(guess) != properlen:
            guess = input(f"That wasn't {properlen} chars! Try again: ")
    return guess


def main() -> None:
    """Main function of code."""
    secret = 'codes'
    guess = ''
    index = 0
    emojified_guess = ''
    while index != 6:
        index += 1
        print(f'=== Turn {index}/6 ===')
        guess = input_guess(len(secret))
        emojified_guess = emojified(guess, secret)
        print(emojified_guess)  
        if guess == secret:
            print(f"You won in {index}/6 turns!")
            break
    if guess != secret:
        print('X/6 - Sorry, try again tomorrow!')


if __name__ == "__main__":
    main()
