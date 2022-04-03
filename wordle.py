# FUCK IT, a wordle clone it is. Yes I know, completely original. But I am bored, so deal with it.


# TODO:
# [ ] lookup of around 3000 words
# [ ] all functionalities of Wordle.com
# [ ] STRICTLY A TERMINAL APPLICATION

from random import choice
from colorama import init
from colorama import Fore, Back, Style
init()

words = []

with open("words.txt", "r") as f:
    for line in f.readlines():
        words.append(line.strip().upper())

chosen_word = str(choice(words))
current_chance = 0
total_chances = 6
guessed_crct = False

def check_word(guess, word):
    global guessed_crct
    if guess == word:
        print(Fore.GREEN, word)
        print("noice\n")
        guessed_crct = True
        quit()

    else:
        for index in range(len(word)):
            if guess[index] not in word[index]:
                color = Fore.WHITE
            if guess[index] in word:
                color = Fore.YELLOW
            if word[index] == guess[index]:
                color = Fore.GREEN

            print(color, f"{guess[index]}", end='')

        print(Style.RESET_ALL)
        print()


while current_chance < total_chances:
    guessed_word = guessed_word = input().strip().upper()
    while guessed_word not in words:
        print("Invalid\n")
        guessed_word = input().strip().upper()

    check_word(guessed_word, chosen_word)
    current_chance += 1

print(chosen_word)
