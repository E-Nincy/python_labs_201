# Convert a string to a tuple and print out the result.
# What do you see?
# Asnwer: I see a tuple of characters, = ('c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's')

# What happens if you try to iterate over your tuple of characters?
# Answer: I will get a letter per line

# Do you notice any difference to iterating over the string?
# Answer: No visual difference in the output, but there is a difference in data types.


string = "codingnomads"

my_tuple = tuple(string)
print(my_tuple)             # Output: ('c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's')