__author__ = "730630815"
charcnt = 0
charfound = False
word = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
char = input("Enter a single character:")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()
if word[0] == char:
    charfound = True
    charcnt += 1
    print(char + " found at index 0")
if word[1] == char:
    charfound = True
    charcnt += 1
    print(char + " found at index 1")
if word[2] == char:
    charfound = True
    charcnt += 1
    print(char + " found at index 2")
if word[3] == char:
    charfound = True
    charcnt += 1
    print(char + " found at index 3")
if word[4] == char:
    charfound = True
    charcnt += 1
    print(char + " found at index 4")
if charfound and charcnt == 1:
    print("1 instance of " + char + " found in " + word)
if charfound and charcnt != 1:
    print(str(charcnt) + " instances of " + char + " found in " + word)
if not charfound:
    print("No instances of " + char + " found in " + word)