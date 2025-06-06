# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

from collections import Counter

# Get input from user
user_input = input("Enter a string: ")

# Split words
words = user_input.split()

# Count the frequency of each word
word_counts = Counter(words)

# FInd the most common word
if word_counts:
    most_common_word, count = word_counts.most_common(1)[0]
    print(f"The most common word is: '{most_common_word}' (appeared {count} times)")
else:
    print("No words entered.")