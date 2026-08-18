# ----------- 3-4 Guest List -----------

guest_list = ["mum", "vincent", "emmanuel", "stanley"]

mum = guest_list[0]
message1 = f"Hi {mum.title()}, I'm inviting you to dinner today."
print(message1)

vincent = guest_list[1]
message2 = f"Hi {vincent.title()}, I'm inviting you to dinner today."
print(message2)

emmanuel = guest_list[2]
message3 = f"Hi {emmanuel.title()}, I'm inviting you to dinner today."
print(message3)

stanley = guest_list[3]
message4 = f"Hi {stanley.title()}, I'm inviting you to dinner today."
print(message4)


# ----------- 3-5 Changing Guest List -----------

guest_list = ["mum", "vincent", "emmanuel", "stanley"]

print(f"{guest_list[0].title()} can't make it to dinner.")

guest_list[0] = "rapheal"

rapheal = guest_list[0]
message1 = f"Hi {rapheal.title()}, I'm inviting you to dinner today."
print(message1)

vincent = guest_list[1]
message2 = f"Hi {vincent.title()}, I'm inviting you to dinner today."
print(message2)

emmanuel = guest_list[2]
message3 = f"Hi {emmanuel.title()}, I'm inviting you to dinner today."
print(message3)

stanley = guest_list[3]
message4 = f"Hi {stanley.title()}, I'm inviting you to dinner today."
print(message4)


# ----------- 3-6 More Guests -----------

guest_list = ["rapheal", "vincent", "emmanuel", "stanley"]

print("I found a bigger dinner table, so I can invite more guests.")

guest_list.insert(0, "naomi")
guest_list.insert(3, "precious")
guest_list.append("victor")

naomi = guest_list[0]
message1 = f"Hi {naomi.title()}, I'm inviting you to dinner today."
print(message1)

rapheal = guest_list[1]
message2 = f"Hi {rapheal.title()}, I'm inviting you to dinner today."
print(message2)

vincent = guest_list[2]
message3 = f"Hi {vincent.title()}, I'm inviting you to dinner today."
print(message3)

precious = guest_list[3]
message4 = f"Hi {precious.title()}, I'm inviting you to dinner today."
print(message4)

emmanuel = guest_list[4]
message5 = f"Hi {emmanuel.title()}, I'm inviting you to dinner today."
print(message5)

stanley = guest_list[5]
message6 = f"Hi {stanley.title()}, I'm inviting you to dinner today."
print(message6)

victor = guest_list[6]
message7 = f"Hi {victor.title()}, I'm inviting you to dinner today."
print(message7)


# ----------- 3-7 Shrinking Guest List -----------

guest_list = [
    "naomi",
    "rapheal",
    "vincent",
    "precious",
    "emmanuel",
    "stanley",
    "victor"
]

print("I can invite only two people for dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner.")

popped_guest = guest_list.pop()
print(f"Sorry {popped_guest.title()}, I can't invite you to dinner.")

print(f"Hi {guest_list[0].title()}, you're still invited to dinner.")
print(f"Hi {guest_list[1].title()}, you're still invited to dinner.")

del guest_list[0]
del guest_list[0]

print(guest_list)