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
import matplotlib.pyplot as plt
from operator import itemgetter

# Read the data file into a variable.
f = open("data/desolation_row.txt", "r")
text = f.read()
f.close()

# Clean and Tokenize contents into words.
for character in text:
    if character in  '".,!?':
        text = text.replace(character, '')
    if character  == "-":
        text = text.replace(character, ' ')
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
unique_words = list()
frequency = list()
for item in sorted(words.items(), key = itemgetter(1), reverse= True):
    if item[1] > 2:
        unique_words.append(item[0])
        frequency.append(item[1])
        print(f"{item[0]:<20}{item[1]:>15}")

plt.bar(unique_words[:5], frequency[:5])
plt.winter()
plt.show();
# Output number of words in text file
words_total = len(text_split)
print(f"Number of words in text: {words_total}")

# output number of unique words in text file
unique = len(words)
print(f"Number of unique words in text: {unique}")
# OR USE A SET!!!!

# Proportion of unique words in text
proportion = unique/words_total
print(f"The proportion of unique words in the text is: {proportion:.2f} ")