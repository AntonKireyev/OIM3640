''' PROBLEM SET 12

Instructions:
Write a function that returns a list of stock symbols. 
The function should prompt users for a symbol to add until an empty string is entered 
(the user hits enter without typing anything first). 
The function should return a sorted version of the watch list with no duplicates as a list

Write a function that removes common punctuation marks from a string, i.e. .,?!:;” and returns the string cleaned

Write a function that replaces vowels in a string with numbers a : 4, e : 3 i : 1, o : 0, u : 8 and returns the rewritten string

An anagram is a word or phrase with the same letters as another word or phrase in a different order, 
resulting in a different word or phrase, i.e. debit card and bad credit or dirty room and dormitory. 
Write a function that determines if two string inputs are anagrams of each other'''


# Stock Symbol Watchlist Function
def stock_list():
    symbol_list = list()
    while True:
        symbol = input("Please enter a stock symbol, press [ENTER] once all entries completed: ").upper()
        if symbol == "":
            break
        else:
            symbol_list.append(symbol)
    return sorted(set(symbol_list))
    print(f"Watch list: {sorted(set(symbol_list))}")

# Punctuation Cleaner
def punct_cleaner(text):
    punc = '",.?!;:'
    for mark in punc:
        text = text.replace(mark, "")
    return text

# Vowel Replacer
def vowel_replacer(text):
    vowels = {"a" : 4, "e" : 3, "i" : 1, "o" : 0, "u" : 8}
    text = text.lower()
    for vowel, number in vowels.items():
        text = text.replace(vowel, str(number))

    return text

# Anagram Checker
def anagram_checker():
    first = input("first word/phrase: ").lower()    
    second = input("second word/phrase: ").lower()
    value1 = 0
    value2 = 0
    for letter in list(first):
        value1 += ord(letter)
    for letter in list(second):
        value2 += ord(letter)
    if value1 == value2:
        print("They are Anagrams!")
    else:
        print("They are NOT Anagrams!")


stock_list()

words = "So long, and thanks for all the fish!"
print(punct_cleaner(words))

print(vowel_replacer(words))

anagram_checker()