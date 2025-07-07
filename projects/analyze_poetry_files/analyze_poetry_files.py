# Goal: Write a Python script that reads .txt file and:

# Open and read file
with open("poem.txt", "r") as file:
    content = file.read()
    print(content)

# Split text into words
w = content.split()
words = [word.lower() for word in w]

# Use dictionaries to count words
def count_words():
    data_dict = {}
    for word in words:
        if word in data_dict:
            data_dict[word] += 1
        else:
            data_dict[word] = 1
    return data_dict

data = count_words()

# Goal1. Counts how many times the word "you" appears:
data["you"]

# Goal2. Finds the most frequent word.
from collections import Counter
Counter(words).most_common(1)
