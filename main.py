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
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = [letter for letter in alphabets]

with open("[path to words.txt]", "r") as f:
    for line in f.readlines():
        words.append(line.strip().upper())

print("Welcome to wordle, guess a 5 letter word")
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
                try:
                    alphabets.remove(guess[index])
                except:
                    pass
            if guess[index] in word:
                color = Fore.RED
            if word[index] == guess[index]:
                color = Fore.GREEN

            print(color, f"{guess[index]}", end='')

        print(Style.RESET_ALL)
        print(alphabets)
        print()


def main():
    global current_chance, total_chances, guessed_crct
    while current_chance < total_chances:
        guessed_word = guessed_word = input().strip().upper()
        while guessed_word not in words:
            print("Invalid\n")
            guessed_word = input().strip().upper()

        check_word(guessed_word, chosen_word)
        current_chance += 1

    print(chosen_word)

if __name__ == "__main__":
    main()
