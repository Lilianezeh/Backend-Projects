# ----------- 4-10 Slices -----------

cubes = [number ** 3 for number in range(1, 11)]

print("The first three items in the list are:")
print(cubes[:3])

print("Three items from the middle of the list are:")
print(cubes[3:6])

print("The last three items in the list are:")
print(cubes[-3:])


# ----------- 4-11 My Pizzas, Your Pizzas -----------

pizzas = ["pepperoni", "chicken", "beef"]

friend_pizzas = pizzas[:]

# Add a new pizza to my list
pizzas.append("vegetable")

# Add a different pizza to my friend's list
friend_pizzas.append("cheese")

# Prove that the lists are separate
print("My pizzas:")
print(pizzas)

print("My friend's pizzas:")
print(friend_pizzas)

# Print my favorite pizzas
print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza)

# Print my friend's favorite pizzas
print("My friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)


# ----------- 4-12 More Loops -----------

my_foods = ["pizza", "falafel", "carrot cake"]

friend_foods = my_foods[:]

print("My favorite foods are:")

for food in my_foods:
    print(food)

print("My friend's favorite foods are:")

for food in friend_foods:
    print(food)