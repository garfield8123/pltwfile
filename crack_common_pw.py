#!/usr/bin/python3
# -*- coding: <encoding name> -*-
from __future__ import print_function

import sys

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import pyexcel_xlsx as p

common_pws = []

# load the excel file into a python dictionar called common_pws
def load_data():
    data = p.get_data("wordlist_common.xlsx")    
  
    global common_pws
    common_pws = data['Sheet1']

# returns a list of passwords that is iterable
def words_to_match():
    global common_pws
    for w in common_pws:
        yield w[0]

# searches the words loaded in dictionary for the password
def check_password(password):
    for w in words_to_match():
        if w == password:
            return w

def main():
    # usage
    if len(sys.argv) != 2:
        print("Usage: python crack_pw.py [password]")
        sys.exit(0)
        
    # store the user's password they provided in the command line
    password = sys.argv[1]
    
    # load all dictionary words from the spreadsheet
    load_data()

    if check_password(password):
        print("Found! Your password is one of the most common ones, you might consider changing it.")
    else:
        print("Congratulations, you have a unique password!")
        
# call the main function
if __name__ == "__main__": main()