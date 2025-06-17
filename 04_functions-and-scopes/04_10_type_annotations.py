# Add type annotations to the three functions shown below.
 
def multiply(num1, num2):  # Type: (int,  int) <- int
    return num1 * num2

def greet(greeting, name):      # Type: (str, str) <- str
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args):       #  Typ: (*str) <- list
    [print(f"* {item}") for item in args]
    return args
