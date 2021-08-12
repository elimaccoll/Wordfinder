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
    for i in range(1, len(letters) + 1):
        for combination in itertools.permutations(letters, i):
            word = convertTuple(combination)
            if word in dictionary:
                words_found += 1
                words.append(word)
    return words


def printToTextFile(words):
    with open("wordfinder.txt", "w") as txt_file:
        for i in range(len(words)):
            word = words[i]
            if i != len(words) - 1:
                word += '\n'
            txt_file.write(word)


def backend(user_letters, dict_num):
    letters = verifyUserInput(user_letters)
    dictionary = getDictionaryWords(dict_num)
    words = findWords(letters, dictionary)
    return words
