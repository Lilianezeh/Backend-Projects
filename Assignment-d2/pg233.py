# -----------------7-8: Deli---------------------
sandwich_orders = ["tuna", "chicken", "veggie", "pastrami", "turkey"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())


# -----------------7-9: No Pastrami---------------------
sandwich_orders = ["tuna", "pastrami", "chicken", "pastrami", "veggie", "pastrami", "turkey"]

print("The deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())


# -----------------7-10: Dream Vacation--------------------
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")

    responses[name] = destination

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, destination in responses.items():
    print(f"{name} would like to visit {destination}.")

