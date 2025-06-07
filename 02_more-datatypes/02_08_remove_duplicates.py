# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

# Use a different data type
my_list_ = [1, 2, 3, 4, 3, 4, 5]
new_list = list(set(my_list_))
print(new_list)

# Use a loop and a second list
my_list_ = [1, 2, 3, 4, 3, 4, 5]
new_list = []
for item in my_list_:
    if item not in new_list:
        new_list.append(item)
print(new_list)

