# ----------- 5-1 Conditional Tests -----------

car = "subaru"

print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")


name = "Lilian"

print("\nIs name == 'Lilian'? I predict True.")
print(name == "Lilian")

print("\nIs name == 'lilian'? I predict False.")
print(name == "lilian")


age = 25

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age == 30? I predict False.")
print(age == 30)


country = "Nigeria"

print("\nIs country != 'Ghana'? I predict True.")
print(country != "Ghana")

print("\nIs country != 'Nigeria'? I predict False.")
print(country != "Nigeria")


number = 10

print("\nIs number > 5? I predict True.")
print(number > 5)

print("\nIs number < 5? I predict False.")
print(number < 5)


# ----------- 5-2 More Conditional Tests -----------

# --------------------------------
# String equality
# --------------------------------

name = "Lilian"

print("String equality:")
print(name == "Lilian")
print(name == "John")


# --------------------------------
# String inequality
# --------------------------------

print("\nString inequality:")
print(name != "John")
print(name != "Lilian")


# --------------------------------
# lower() method
# --------------------------------

country = "Nigeria"

print("\nUsing lower():")
print(country.lower() == "nigeria")
print(country.lower() == "ghana")


# --------------------------------
# Numerical equality and inequality
# --------------------------------

age = 25

print("\nNumerical equality:")
print(age == 25)
print(age == 30)

print("\nNumerical inequality:")
print(age != 30)
print(age != 25)


# --------------------------------
# Greater than and less than
# --------------------------------

score = 75

print("\nGreater than:")
print(score > 50)
print(score > 90)

print("\nLess than:")
print(score < 90)
print(score < 50)


# --------------------------------
# Greater than or equal to
# --------------------------------

print("\nGreater than or equal to:")
print(score >= 75)
print(score >= 80)


# --------------------------------
# Less than or equal to
# --------------------------------

print("\nLess than or equal to:")
print(score <= 75)
print(score <= 50)


# --------------------------------
# Using and
# --------------------------------

age = 25

print("\nUsing and:")
print(age > 18 and age < 30)
print(age > 30 and age < 40)


# --------------------------------
# Using or
# --------------------------------

print("\nUsing or:")
print(age == 25 or age == 30)
print(age == 18 or age == 20)


# --------------------------------
# Item in a list
# --------------------------------

fruits = ["apple", "banana", "orange"]

print("\nTesting if an item is in a list:")
print("apple" in fruits)
print("mango" in fruits)


# --------------------------------
# Item not in a list
# --------------------------------

print("\nTesting if an item is not in a list:")
print("mango" not in fruits)
print("banana" not in fruits)