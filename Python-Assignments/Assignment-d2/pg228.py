# -----------------7-4: Pizza Toppings---------------------

prompt = "\nWhat topping would you like on your pizza? "
prompt += "\n(Enter 'quit' when you're done.) "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")



# -----------------7-5: Movie Tickets---------------------

prompt = "\nHow old are you? (Enter 'quit' to end) "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")



# -----------------7-6: Three Exits---------------------
# Version 1 - condition built into the while line itself:

prompt = "\nWhat topping would you like? (Enter 'quit' to stop) "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")


# Version 2 - an active/flag variable controls the loop:
prompt = "\nWhat topping would you like? (Enter 'quit' to stop) "
active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")


# Version 3 - break exits immediately:
prompt = "\nWhat topping would you like? (Enter 'quit' to stop) "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")



# ----------------7-7: Infinity -------------------
while True:
    print("This loop never ends!")