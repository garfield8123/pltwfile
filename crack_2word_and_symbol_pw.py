#!/usr/bin/python3
# -*- coding: <encoding name> -*-
from __future__ import print_function

import pyexcel_xls
import time
import sys

symbols=".,?~`!@#$%^&*()-_+=[{]}\|;:'<>/"

# global variables
dictionary_words = []
guesses = 0

# load the excel file
def load_data():
    global dictionary_words
    data = pyexcel_xls.get_data("wordlist_common.xlsx")    
    dictionary_words = data['Sheet1']

# generate a dictionary of words to check
def words_to_match():
    global dictionary_words
    for w in dictionary_words:
        yield w[0]

# # try to match two dictionary words with a symbole before or after a word
def crack_two_words_and_symbol(password):
    global guesses
    for w1 in words_to_match():
        for w2 in words_to_match():
            for s in symbols:
                phrase = w1 + w2 + s
                '''
                if phrase == password:
                    return (phrase)
                else:
                    phrase = w1 + s + w2
                    if phrase == password:
                        return(phrase)
                    else:
                        phrase = w1 + w2 + s
                        if phrase == password: 
                            return (phrase)
                '''
                if phrase == password:
                    return(phrase)

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
    t0 = time.time()
    found = crack_two_words_and_symbol(password)
    t1 = time.time()

    # show results
    if found:
        print("Done.\nFound", found)
    else:
        print("Done.\nCould not crack!")
                
    t1 = time.time()
    print("Time:", format((t1-t0), '.8f'))
    print("Guesses:", guesses)

if __name__ == "__main__": main()