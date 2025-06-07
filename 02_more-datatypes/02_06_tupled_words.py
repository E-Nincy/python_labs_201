# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

# Take a string from the user
user_input = input("Enter a string; ")

# split the string into words
words = user_input.split()

# Create a list of tuples, one tuple per word
result_list = [tuple(word) for word in words]

print(result_list)