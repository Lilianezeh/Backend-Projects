# -------------6-4. Glossary 2 ------------------
glossary = {
    "variable": "A name used to store a value in a program.",
    "function": "A reusable block of code that performs a specific task.",
    "list": "A collection of items stored in a single variable.",
    "dictionary": "A collection of key-value pairs.",
    "loop": "A way of repeating a block of code.",
    "string": "A sequence of characters enclosed in quotation marks.",
    "integer": "A whole number without a decimal point.",
    "conditional": "A statement that allows a program to make decisions.",
    "parameter": "A value that is passed into a function.",
    "boolean": "A value that can be either True or False."
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n{meaning}\n")
    
    

# -------------6-5. Rivers ------------------
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "niger": "nigeria"
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()

# Print the name of each river
for river in rivers.keys():
    print(river.title())

print()

# Print the name of each country
for country in rivers.values():
    print(country.title())
    
    
# -------------6-6. Polling ------------------
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}

people_to_poll = [
    "jen",
    "sarah",
    "mike",
    "david",
    "phil",
    "lilian"
]

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, please take our favorite languages poll.")