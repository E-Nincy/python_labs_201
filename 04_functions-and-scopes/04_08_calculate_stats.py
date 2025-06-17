# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numbers):
  # define the function here
  return{
    "min" : min(numbers),
    "max" : max(numbers),
    "sum" : sum(numbers),
    "mean" : sum(numbers) / len(numbers)
  }

# call the function below here
example_list = [1, 2, 3, 4, 5, 6, 7]
result = stats(example_list)
print(result) 