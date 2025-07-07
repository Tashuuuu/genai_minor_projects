# Goal: Write a Python script that reads .txt file and:

# Open and read file
with open("poem.txt", "r") as file:
    content = file.read()

# Split text into words
words = [word.lower() for word in content.split()] 

# Use dictionaries to count words
def count_words():  
    data_dict = {}  
    for word in words:  
        data_dict[word] = data_dict.get(word, 0) + 1 
    return data_dict

data = count_words()

# Goal1. Counts how many times the word "you" appears:
you_count = data.get("you", 0)

# Goal2. Finds the most frequent word.
from collections import Counter  
stopwords = {"the", "and", "a", "to", "i"}  # Add more as needed  
filtered_words = [word for word in words if word not in stopwords]  
most_common = Counter(filtered_words).most_common(1)
