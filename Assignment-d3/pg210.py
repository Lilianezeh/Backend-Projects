# -------------6-7. People ------------------
person1 = {
    "first_name": "John",
    "last_name": "Okafor",
    "age": 25,
    "city": "Enugu"
}

person2 = {
    "first_name": "Amara",
    "last_name": "Chukwu",
    "age": 30,
    "city": "Lagos"
}

person3 = {
    "first_name": "Emeka",
    "last_name": "Nwosu",
    "age": 22,
    "city": "Abuja"
}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()


# -------------6-8. Pets ------------------
pet1 = {
    "animal_type": "dog",
    "owner": "Lilian"
}

pet2 = {
    "animal_type": "cat",
    "owner": "John"
}

pet3 = {
    "animal_type": "parrot",
    "owner": "Mary"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()


# -------------6-9. Favorite Places ------------------
favorite_places = {
    "Lilian": ["Paris", "Enugu", "Cape Town"],
    "John": ["Lagos", "Dubai"],
    "Mary": ["Abuja", "London", "Tokyo"]
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"  {place}")


# -------------6-10. Favorite Numbers ------------------
favorite_numbers = {
    "Lilian": [7, 13],
    "John": [10, 21, 3],
    "Mary": [3],
    "David": [21, 9],
    "Sarah": [5, 12, 8]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")


# -------------6-11. Cities ------------------
cities = {
    "enugu": {
        "country": "Nigeria",
        "population": 3300000,
        "fact": "Known as the Coal City for its former coal mining industry."
    },
    "paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Home to the Eiffel Tower, built in 1889."
    },
    "tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "The most populous metropolitan area in the world."
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    for key, value in info.items():
        print(f"  {key.title()}: {value}")