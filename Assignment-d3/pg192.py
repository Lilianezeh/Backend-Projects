# -------------6-1. Person ------------------
person = {
    "first_name": "John",
    "last_name": "Okafor",
    "age": 25,
    "city": "Enugu"
}

for key, value in person.items():
    print(f"{key.replace('_', ' ').title()}: {value}")


# -------------6-2. Favorite Numbers ------------------
favorite_numbers = {
    "Lilian": 7,
    "John": 10,
    "Mary": 3,
    "David": 21,
    "Sarah": 5
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")


# -------------6-3. Glossary ------------------
glossary = {
    "variable": "A name used to store a value in a program.",
    "function": "A reusable block of code that performs a specific task.",
    "list": "A collection of items stored in a single variable.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "A way of repeating a block of code."
}

for term, definition in glossary.items():
    print(f"{term.title()}:\n{definition}\n")