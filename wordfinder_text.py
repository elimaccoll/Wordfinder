import itertools
import time
import sys

# Do this in a better way
dicts = ["dictionary_alpha.txt",
         "dictionary_alpha_num_symbol.txt",
         "dictionary_test.txt"]

dicts_labels = ["Letters only",
                "Letters, Numbers, and Symbols",
                "Test file"]


def getDictionaries():
    return dicts


def getDictionaryLabels():
    return dicts_labels


def getNumDictionaries():
    return len(dicts)


def convertTuple(tup):
    str = ''.join(tup)
    return str


# Change this to support using different dictionaries
def getDictionaryWords(num):
    dictionary_file = open(dicts[num - 1], "r")
    dictionary_words = dictionary_file.readlines()
    for i in range(len(dictionary_words)):
        dictionary_words[i] = dictionary_words[i].strip('\n')
    return dictionary_words


def getUserInput():
    user_letters = input("Time to enter your characters!\n"
                         "Example of valid input: abc\n"
                         "Enter your characters and hit the 'Enter' key: ")
    return user_letters


def verifyUserInput(user_letters):
    # Checks if lowercase, converts if not
    if not user_letters.islower():
        user_letters = user_letters.lower()
    # Creates official string to be used in search
    letters = ""
    for c in user_letters:
        if c not in letters:
            letters += c
    return letters


def findWords(letters, dictionary):
    words = []
    words_found = 0
    print(f"Finding words using '{letters}'...")
    for i in range(1, len(letters) + 1):
        for combination in itertools.permutations(letters, i):
            word = convertTuple(combination)
            if word in dictionary:
                words_found += 1
                words.append(word)
    return words


def menu(words):
    sel = 0
    while int(sel) < 1 or int(sel) > 3:
        sel = input("\n1. Enter new characters\n"
                    "2. Print words to text file\n"
                    "3. Exit\n"
                    "Enter the number of our selection: ")
        if not sel.isdigit():
            sel = 0
            print("\n === Please enter a valid selection ===\n")

    sel = int(sel)
    if sel == 1:
        print("\nTime to enter new characters!")
        return 0
    if sel == 2:
        printToTextFile(words)
        return 1
    if sel == 3:
        print("Quitting...")
        return -1


def printToTextFile(words):
    print("\nYou chose to print your words to a text file. This will override an existing text file if you have "
          "done this previously.")
    text_sel = 0
    while int(text_sel) < 1 or int(text_sel) > 2:
        text_sel = input("Do you wish to continue?\n"
                         "1. Yes\n"
                         "2. No\n"
                         "Enter the number of your selection: ")
        if not text_sel.isdigit():
            text_sel = 0
            print("\n === Please enter a valid selection ===\n")

    if int(text_sel) == 2:
        return 0
    else:
        with open("wordfinder_output.txt", "w") as txt_file:
            for i in range(len(words)):
                word = words[i]
                if i != len(words) - 1:
                    word += '\n'
                txt_file.write(word)
        print("Created text file named 'wordfinder_output.txt'")
        return 0


def dictionary_select():
    dict_num = 0
    # Use a dictionary to hold dictionary files
    dict1 = "Letters only"
    dict2 = "Letters, Symbols, and Numbers"
    dict3 = "Test file"
    dicts = [dict1, dict2, dict3]
    while int(dict_num) < 1 or int(dict_num) > len(dicts):
        dict_num = input("Select the dictionary you would like to use to search for words.\n"
                         f"1. {dict1}\n"
                         f"2. {dict2}\n"
                         f"3. {dict3}\n"
                         "Enter the number of your selection: ")
        if not dict_num.isdigit():
            dict_num = 0
            print("\n === Please enter a valid selection ===\n")
    print(f"You selected the {dicts[int(dict_num) - 1]} dictionary.\n")
    return int(dict_num)


def main():
    # TODO:
    #       1. Add option to switch dictionaries from the menu instead of asking which dictionary every time
    #       2. Test the code with symbols as characters - need to implement new dictionaries for this
    #             - Doesn't really work because of case sensitivity at the moment
    run = True
    print("=" * 60)
    print(" __          __           _ ______ _           _\n"
          " \ \        / /          | |  ____(_)         | |\n"
          "  \ \  /\  / /__  _ __ __| | |__   _ _ __   __| | ___ _ __ \n"
          "   \ \/  \/ / _ \| '__/ _` |  __| | | '_ \ / _` |/ _ \ '__|\n"
          "    \  /\  / (_) | | | (_| | |    | | | | | (_| |  __/ |\n"
          "     \/  \/ \___/|_|  \__,_|_|    |_|_| |_|\__,_|\___|_|")
    print("=" * 60)
    print("This program will find all possible words with the provided characters.")
    while run:
        dict_num = dictionary_select()
        user_letters = getUserInput()
        letters = verifyUserInput(user_letters)
        dictionary = getDictionaryWords(dict_num)
        words = findWords(letters, dictionary)
        if len(words) > 0:
            print(f"{len(words)} possible words found with the characters '{letters}':")
            out = ""
            for i in range(len(words)):
                out += words[i]
                if i != len(words) - 1:
                    out += ", "
                    # 25 words per line when printed in terminal
                    if i % 25 == 0 and i != 0:
                        out += "\n"
        else:
            out = f"No words found with the characters '{letters}'"
        print(out)

        m = 1
        while m == 1:
            m = menu(words)
        if m == 0:
            continue
        if m == -1:
            run = False

if __name__ == "__main__":
    main()
