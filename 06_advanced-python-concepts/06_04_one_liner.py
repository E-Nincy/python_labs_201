# Use a one-liner list comprehension to express the following functionality:
#
# letters = []
# for letter in 'suchalongword':
#     letters.append(letter)
# print(letters)

letters = [char for char in "suchalongword"]
print(letters)