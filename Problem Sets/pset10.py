''' PSET 10
1. Read the data file into a variable. It may be easiest to initially store the data as a string
2. Clean and "tokenize" the contents into words, i.e. remove punctuation, transform data into lower case
3. Use a dict to store words and counts
4. Produce well-formatted output of each word and its associated count, sorted by most frquent word first
5. Output also the total number of words in the text file
6. Output the number of unique words in the text
7. Calculate the proportion of unique words in the text
'''

# LIbraries
import os
from operator import itemgetter

# Read the data file into a variable.
f = open("data/desolation_row.txt", "r")
text = f.read()
f.close()

# Clean and Tokenize contents into words.
for character in text:
    if character in  "'.,!?":
        text = text.replace(character, '')
    if character  == "-":
        text = text.replace(character, ' ')
    if character == '"':
        text = text.replace(character, '')
    else: 
        pass
text_split = text.lower().split()

# Use a dict to store words and counts
words = {}
for word in text_split:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

# Output of each word and its associated count, sorted by most frquent word first
for word in sorted(words.items(), key = itemgetter(1), reverse= True):
    print(f"{word[0]:<20}{word[1]:>15}")

# Output number of words in text file
words_total = len(text_split)
print(f"Number of words in text: {words_total}")

# output number of unique words in text file
unique = len(words)
print(f"Number of unique words in text: {unique}")

# Proportion of unique words in text
proportion = unique/words_total
print(f"The proportion of unique words in the text is: {proportion:.2f} ")