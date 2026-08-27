# ----------- 4-13 Buffet -----------

foods = ("rice", "chicken", "fish", "salad", "pasta")

print("The restaurant offers:")

for food in foods:
    print(food)

# Try to change one of the items

foods[0] = "yam"
foods = ("rice", "chicken", "fish", "salad", "pasta")

print("The restaurant offers:")

for food in foods:
    print(food)

# The restaurant changes its menu
foods = ("rice", "beef", "fish", "vegetables", "pasta")

print("\nThe revised menu is:")

for food in foods:
    print(food)