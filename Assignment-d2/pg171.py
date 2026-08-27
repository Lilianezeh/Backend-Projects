# ----------- 5-3 Alien Colors #1 -----------
# Version that passes the if test
alien_color = "green"

if alien_color == "green":
    print("The player just earned 5 points!")



# Version that fails the if test (no output)
alien_color = "red"

if alien_color == "green":
    print("The player just earned 5 points!")


# ----------- 5-4 Alien Colors #2 -----------
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")



alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")



# ----------- 5-5 Alien Colors #3 -----------
alien_color = 'green'   # try also 'yellow' and 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")


# ----------- stages of life ----------------

age = 8   # change this value to test different stages

if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

# ----------- 5-7 Favorite Fruit -----------

favorite_fruits = ["mango", "banana", "pineapple"]

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "pineapple" in favorite_fruits:
    print("You really like pineapples!")

if "apple" in favorite_fruits:
    print("You really like apples!")

if "grape" in favorite_fruits:
    print("You really like grapes!")



