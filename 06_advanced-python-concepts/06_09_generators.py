# Demonstrate how to create a generator object.
# Print the object to the console to see what you get.
# Then iterate over the generator object and print out each item.

# Generator object
gen = (x for x in range(5))
print(gen)

# Iterate over object
for item in gen:
    print(item)