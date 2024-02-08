''' Problem Set 7
1. Write a script that transforms each word into pig Latin and prints the result. 

Pig Latin Rules:

If a word starts with a consonant and a vowel, put the first letter of the word at the end of the word and add "ay." ...
If a word starts with two consonants move the two consonants to the end of the word and add "ay." ...
If a word starts with a vowel add the word "way" at the end of the word.
For example Darkness = arkness Day, break = eak bray, at = at way

2. Compute the average length of each word in the original text 
3. Programmatically find the longest word in the original text '''

# Pig Latin Script

text = '''Darkness at the break of noon  
Shadows even the silver spoon  
The handmade blade, the child's balloon  
Eclipses both the sun and moon'''

text_split = text.replace(',', '').replace("'",'').split()

total = 0
max_length = 0
long_word = []
vowels = 'aeiouAEIOU'

for word in text_split:
    total += len(word)
    if len(word) >= max_length:
        max_length = len(word)
        long_word.append(word)
    if word[0] not in vowels and word[1] in vowels:
        word =  word[1:] + ' ' + word[:1] + 'ay'
        print(word)
    elif word[0] and word[1] not in vowels:
        word =  word[1:] + ' ' + word[:1] + 'ay'
        print(word)
    elif word[0] in vowels:
        word = word + ' way'
        print(word)
    else:
        print("error")


average_length = total / len(text_split)

print(f"The average length of words is {average_length:.2f} characters long.")
print(f"The longest word(s) is/are {long_word} at {max_length} characters long.")