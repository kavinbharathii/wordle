
# -------------------------------- required packages ------------------------------------ #
from random import choice
from colorama import init
from colorama import Fore, Style
import json
init()

# -------------------------------- global variables ------------------------------------ #

words = []
alphabets = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
current_chance = 0
total_chances = 6
guessed_crct = False

# --------------------------------- file handling -------------------------------------- #

with open("[path to words.txt]", "r") as f:
    for line in f.readlines():
        words.append(line.strip().upper())

with open("[path to stats.json]", "r") as json_file:
    data = json.load(json_file)
    json_file.close()

# ------------------------------- choosing a word -------------------------------------- #

chosen_word = str(choice(words))

# ------------------------------ display statistics ------------------------------------ #

def display_stats(data_):
    print(Fore.CYAN, '---------- [STATS] ----------')
    for key, value in data_.items():
        print(Fore.CYAN, f"attempt {int(key) + 1} : {'/' * value}")

# ------------------------------ compare two words ------------------------------------ #

def check_word(guess, word):
    global guessed_crct
    if guess == word:
        print(Fore.GREEN, word)
        print()
        print("[NOICE]\n")
        guessed_crct = True
        data[str(current_chance)] += 1
        with open("[path to stats.json]", "w") as json_file:
            json.dump(data, json_file)
            json_file.close()
        display_stats(data)
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

# ------------------------------- main game func -------------------------------------- #

def main():
    global current_chance, total_chances, guessed_crct
    while current_chance < total_chances:
        guessed_word = input().strip().upper()
        while guessed_word not in words:
            print("[INVALID]\n")
            guessed_word = input().strip().upper()

        check_word(guessed_word, chosen_word)
        current_chance += 1

    print(chosen_word)


# ---------------------------- initializing the game ----------------------------------- #

if __name__ == "__main__":
    print("Welcome to wordle, guess a 5 letter word")
    main()
