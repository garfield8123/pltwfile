#!/usr/bin/python3
# -*- coding: <encoding name> -*-
from __future__ import print_function
    
import random
import sys

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import pyexcel_xlsx as p

dictionary_words = []
numbers="0123456789"
symbols="~`!@#$%^&*()--+=[{]}|;:',<.>/?"

def load_data():
    global dictionary_words
    data = p.get_data("wordlist_dictionary.xlsx")    
    dictionary_words = data['Sheet1']

def words():
    global dictionary_words
    for w in dictionary_words:
        yield w[0]

def main():
    # usage
    if len(sys.argv) != 1:
        print("Usage: python gen_pw.py")
        sys.exit(0)
    
    words_in_pw = int(input("How many words do you want in your password (2-5)? " ))
        
    # call a function to load all dictionary words from the spreadsheet
    print("Loading dictionary words...", end=' ')
    sys.stdout.flush()
    load_data()
    print ("Done") 
    
    # begin with random number
    ran_num = numbers[random.randint(0,9)] 
    phrase = [ran_num]

    # select 2-5 random words from dictionary
    for i in range(words_in_pw):
      word = dictionary_words[random.randint(0,len(dictionary_words))]
      str_word = str(word[0])
      phrase = phrase + [str_word[0].upper() + str_word[1:] ]
    
    # finish with random symbol
    s = symbols[random.randint(0, len(symbols)-1)]
    phrase = phrase + [s]
    print (''.join(phrase))


    '''
    word1 = dictionary_words[random.randint(0,num_words)]
    str_word1 = str(word1[0])
    word2 = dictionary_words[random.randint(0,num_words)] # could be same word!
    str_word2 = str(word2[0]) 
    
    r = random.randint(0, len(str_word1)-1)
    str_word1 = str_word1[:r] + str_word1[r].upper() + str_word1[r+1:]
    r = random.randint(0, len(str_word2)-1)
    str_word2 = str_word2[:r] + str_word2[r].upper() + str_word2[r+1:]
    
    n = numbers[random.randint(0,9)] 
    s = symbols[random.randint(0, len(symbols)-1)]
    
    phrases = [ str_word1, str_word2, n, s]
    # randomly order
    for i in range(0,2):
        j = random.randint(i, 3)
        t = phrases[i]
        phrases[i] = phrases[j]
        phrases[j] = t
        
    # and the password is....
    print (''.join(phrases)
    '''
 
if __name__ == "__main__": main()