# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """
    Conerts kilometer to miles

    Args:
        km (float): A number representing distance in kilometers.

    Returns:
        float: The equivalent distance in miles.
    """

    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)