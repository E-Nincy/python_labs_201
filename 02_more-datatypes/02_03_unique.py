# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

my_list = [5, 6, 9, 'Love', 9, 2, 13, 6, 5]

unique_list = [x for x in my_list if my_list.count(x) == 1]
print(unique_list)