# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

# Convert  a string into a tuple
string = "codingnomads"
tuple_version = tuple(string)
print("Tuple:", tuple_version)

# Conver a tuple into a list
list_version = list(tuple_version)
print("list:", list_version)

# Change "c" into a "k"
for i in range(len(list_version)):
    if list_version[i] == 'c':
        list_version[i] = 'k'
        break

print("Modified List:", list_version)

# Convert the list back into a tuple
final_tuple = tuple(list_version)
print("Final Tuple:", final_tuple)
