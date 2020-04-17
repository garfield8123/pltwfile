import timeit
import sys

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import pyexcel_xlsx as p

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

# try to crack a one word pasword 
def crack_single_word(password):
    global guesses
    for w in words_to_match():
        guesses = guesses + 1
        if w == password:
            return w

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
    
    # time the attempt to crack the pasword
    print("Attempting to crack...", end=' ')
    sys.stdout.flush()
    
    t0 = timeit.default_timer()
    found = crack_single_word(password)
    t1 = timeit.default_timer()
    
    if found:
        print("Done.\nFound", found)
    else:
        print("Done.\nCould not crack!")
        
    print("Time:", format((t1-t0), '.8f'))
    print("Guesses:", guesses)

if __name__ == "__main__":
    main()