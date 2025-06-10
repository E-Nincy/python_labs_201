# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here

from resources import randlist

# Sort the list
sorted_list = sorted(randlist)

# Add 0 at the end if is a odd number
if len(sorted_list) % 2 != 0:
    sorted_list.append(0)

# Store the numbers in two
paired_list = []
for i in range(0, len(sorted_list), 2):
    pair = (sorted_list[i], sorted_list[i+1])
    paired_list.append(pair)

# Print each tupla
for pair in paired_list:
    print(pair)