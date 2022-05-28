
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

with open("./words.txt", "r") as f:
    for line in f.readlines():
        words.append(line.strip().upper())

with open("./stats.json", "r") as json_file:
    data = json.load(json_file)
    json_file.close()

# ------------------------------- choosing a word -------------------------------------- #

chosen_word = str(choice(words))

# ------------------------------ display statistics ------------------------------------ #

def display_stats(data_):
    print(Fore.CYAN, '---------- [STATS] ----------')
    for key, value in data_.items():
        if key.isnumeric():
            print(Fore.CYAN, f"attempt {int(key) + 1}      : {'/' * value}")
        else:
            # len of the longest string is 'current_streak' is 14 chars.
            # So to make the spaces of all stats even, we subtract the 
            # number of chars in the key to calculate the amount of spaces required.
            print(Fore.CYAN, f"{key}{' ' * (14 - len(key))} : {value}")

# ------------------------------ compare two words ------------------------------------ #

def check_word(guess, word):
    global guessed_crct
    if guess == word:
        print(Fore.GREEN, word)
        print()
        print("[NOICE]\n")
        guessed_crct = True
        data[str(current_chance)] += 1
        data['current_streak'] += 1
        data['max_streak'] = max(data['current_streak'], data['max_streak'])
        with open("./stats.json", "w") as json_file:
            json.dump(data, json_file)
            json_file.close()
        display_stats(data)
        quit()

    else:
        for index in range(len(word)):
            if guess[index] not in word:
                color = Fore.WHITE
                try:
                    alphabets.remove(guess[index])
                except ValueError:
                    pass
            if guess[index] in word:
                color = Fore.RED
            if word[index] == guess[index]:
                color = Fore.GREEN

            print(color, f"{guess[index]}", end='')

        print(Style.RESET_ALL)
        print(f"[{' '.join(alphabets)}]")
        print()

# ------------------------------- main game func -------------------------------------- #

def main():
    print("Welcome to wordle, guess a 5 letter word")
    global current_chance, total_chances, guessed_crct
    while current_chance < total_chances:
        guessed_word = input().strip().upper()
        while guessed_word not in words:
            print(Fore.RED, "[INVALID]\n")
            print(Style.RESET_ALL, end = '')
            guessed_word = input().strip().upper()

        check_word(guessed_word, chosen_word)
        current_chance += 1

    print(chosen_word)

    if current_chance >= total_chances:
        data["current_streak"] = 0
        with open("./stats.json", "w") as json_file:
            json.dump(data, json_file)
            json_file.close()

    display_stats(data)


# ---------------------------- initializing the game ----------------------------------- #

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------------------------- #
