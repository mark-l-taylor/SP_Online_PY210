#! /usr/bin/env python3
## Lesson 4 Assignment 3, Trigrams Kata 14
## By: B. Matthews
## https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/kata_fourteen.html
## Note: this somewhat works, but could be better. I'm not sure how to keep the new
## text going after it doesn't find a key match in the dictionary

import os
import sys
import string
import random

new_text = ""
max_size = 200

def read_in_data(fn):
    """gets text from a file to use in generating new text file"""

    with open(fn, 'r') as f:
        all_lines = f.readlines()

    return all_lines

def make_words(data):
    """strips out the words from a big chunk of text file, returns list of strings"""
    lots_of_words = []

    for eachLine in data:
        lots_of_words = lots_of_words + eachLine.split()

    for thing in lots_of_words:
        lots_of_words[lots_of_words.index(thing)] = lots_of_words[lots_of_words.index(thing)].replace('-', ' ')

    print(lots_of_words)

    return lots_of_words

def build_trigram(w):
    """build a dictionary using word pairs from the file as keys"""

    trigrams = {}

    for i in range(len(w)-2):
        key_words = tuple(w[i:i + 2])
        third_word = w[i + 2]

        if key_words in trigrams:
            trigrams[key_words].append(third_word)
        else:
            trigrams[key_words]=[third_word]

    for k in trigrams.keys(): print(k, trigrams[k])

    return trigrams

def build_text(wp):
    """generate a new story using the words from the input file"""

    start_key = ('I', 'rang')       #just picked one from the text in sherlock_small.txt
    #start_key = ('the', 'cat')       # for testing with sample.txt
    current_key = start_key
    text = " ".join(start_key) + " "    #initialize the new story beginning

    while (current_key in wp.keys() and len(text) <= max_size):
        w = random.choice(wp[current_key])      #get a random word from dictonary
        text = text + " " + w
        current_key = current_key[1], w         #new key of 2nd word and new word

    return text


if __name__ == "__main__":
    ## get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Please enter a filename of a text file after the executable name")
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = build_trigram(words)
    new_text = build_text(word_pairs)

    print(new_text)


