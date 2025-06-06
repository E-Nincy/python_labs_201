# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

# 10 numbers in one line separated by comas
numbers = list(map(int, input("Enter a 10 numbers separated by commas: ").split(',')))

# Print 2nd, 4th, 6th, 8th, 10th numbers
print(numbers[1], numbers[3], numbers[5], numbers[7], numbers[9], sep=",")

# Print the 9th, 7th, 5th, 3rd, 1st number
print(numbers[8], numbers[6], numbers[4], numbers[2], numbers[0], sep=",")
