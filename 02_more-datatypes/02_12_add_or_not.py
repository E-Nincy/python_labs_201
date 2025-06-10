# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

user_numbers = set()
score = 0

print("🎮 Welcome to the Memory Game!")
print("Enter numbers. Try not no repeat!")
print("You lose if you repeat a number 5 times.")
print("You win if you enter more than 10 uniques number.\n")

while True:
    user_input = input("Enter  number: ")
    
    # Check if input is a valid integer
    try:
        number = int(user_input)
    except ValueError:
        print("That's not a valid number. Try again.\n")
        continue

    if number in user_numbers:
        score -= 1
        print(f"Duplicate! You lose a point. Current score: {score}\n")
    else:
        user_numbers.add(number)
        print(f"Added! Total uniques numbers: {len(user_numbers)}\n")

    if score <= -5:
        print(f"Game Over! You lost. Too many duplicates.")
        break
    elif len(user_numbers) > 10:
        print("COngratulations! You win! Great memory.")
        break