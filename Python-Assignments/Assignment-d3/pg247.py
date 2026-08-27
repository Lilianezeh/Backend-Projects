# ------------8-3: T-Shirt -------------------

def make_shirt(size, message):
    """Prints the size of a shirt and the message on it."""

    print(f"The shirt size is {size} and the message on it is '{message}'.")


# Calling the function using positional arguments
make_shirt("Medium", "I love Python")


# Calling the function using keyword arguments
make_shirt(size="Large", message="Python is awesome")


# -------------8-4: Large Shirts ------------------
def make_shirt(size="Large", message="I love Python"):
    """Prints the shirt size and the message on it."""

    print(f"The shirt size is {size} and the message on it is '{message}'.")


# Large shirt with the default message
make_shirt()


# Medium shirt with the default message
make_shirt(size="Medium")


# Shirt with a different size and different message
make_shirt(size="Small", message="Keep Learning Python")


# -------------------8-5: cities ---------------------
def describe_city(city, country="Iceland"):
    """Prints a sentence describing a city and its country."""

    print(f"{city} is in {country}.")


# City using the default country
describe_city("Reykjavik")


# Another city using the default country
describe_city("Akureyri")


# City with a different country
describe_city("Lagos", "Nigeria")



    



