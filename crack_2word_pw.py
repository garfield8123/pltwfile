#!/usr/bin/python3
# -*- coding: <encoding name> -*-
from __future__ import print_function

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import pyexcel_xlsx as p

import timeit
import sys


# global variables
dictionary_words = []
guesses = 0

# load the excel file
def load_data():
    global dictionary_words
    data = p.get_data("wordlist_dictionary.xlsx")    
    dictionary_words = data['Sheet1']

# generate a dictionary of words to check
def words_to_match():
    global dictionary_words
    for w in dictionary_words:
        yield w[0]

# try to match two dictionary words
def crack_two_words(password):
    global guesses
    for w1 in words_to_match():
        for w2 in words_to_match():
            guesses = guesses + 1
            phrase = w1 + w2
            if phrase == password:
                return (phrase)
# 
# the main program
#
def main():
    
    # usage
    if len(sys.argv) != 2:
        print("Usage: python crack_pw.py [password]")
        sys.exit(0)

    # store the user's password from the command line
    password = sys.argv[1]      
    
    # call a function to load all dictionary words from the spreadsheet
    print("Loading dictionary words...", end=' ')
    sys.stdout.flush()
    load_data()
    print ("Done") 
    
    print("Attempting to crack...", end=' ')
    sys.stdout.flush()

    # tine the attenpt to crack the pasword with symbol
    t0 = timeit.default_timer()
    found = crack_two_words(password)
    t1 = timeit.default_timer()

    # show results
    if found:
        print("Done.\nFound", found)
    else:
        print("Done.\nCould not crack!")
                
    print("Time:", format((t1-t0), '.8f'))
    print("Guesses:", guesses)

if __name__ == "__main__": main()