# Goal: Write a Python script that reads .txt file and:
# 1. Counts how many times the word "you" appears.
# 2. Finds the most frequent word (excluding common words like "the", "and").

# Open and read file
with open("poem.txt", "r") as file:
    content = file.read()
    print(content)

# Split text into words
words = content.split()

# Use dictionaries to count words
def count_words():
    data_dict = {}
    for word in words:
        if word in data_dict:
            data_dict[word] += 1
        else:
            data_dict[word] = 1
    return data_dict

count_words()
