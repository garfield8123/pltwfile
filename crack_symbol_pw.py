#!/usr/bin/python3
# -*- coding: <encoding name> -*-
from __future__ import print_function

import timeit
import sys

import warnings
with warnings.catch_warnings():
  warnings.simplefilter("ignore")
  import pyexcel_xlsx as p

# STUDENT WORK AREA:
symbols = ",.?"
#symbols = ".,?~!@#$%^&*()-_+=[{]}|;:'<>/"

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

# try to match words with a symbol before or after the word
def crack_word_and_symbol(password):
  global guesses
  # check all words
  for w in words_to_match():
    # check all symbols
    for s in symbols:
      # symbol comes before word
      phrase = w + s
      guesses = guesses + 1
      if phrase == password:
        return (phrase)
      else:
        # symbol comes after word
        phrase = s + w
        guesses = guesses +1
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

  # time the attempt to crack the pasword
  t0 = timeit.default_timer()
  found = crack_word_and_symbol(password)
  t1 = timeit.default_timer()

  # show results
  if found:
    print("Done.\nFound", found)
  else:
    print("Done.\nCould not crack!")
          
  print("Time:", format((t1-t0), '.8f'))
  print("Guesses:", guesses)

if __name__ == "__main__": main()