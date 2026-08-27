# -------------------8-9. Messages--------------------------
def show_messages(messages):
    """Prints each message in the list."""

    for message in messages:
        print(message)


messages = [
    "Hello, how are you?",
    "Python is fun to learn.",
    "Keep practicing your coding.",
    "You are doing great!"
]

show_messages(messages)


# -------------------8-10. Sending Messages--------------------------
def send_messages(messages, sent_messages):
    """Prints each message and moves it to sent_messages."""

    while messages:
        current_message = messages.pop()

        print(current_message)

        sent_messages.append(current_message)


messages = [
    "Hello, how are you?",
    "Python is fun to learn.",
    "Keep practicing your coding.",
    "You are doing great!"
]

sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)


# -------------------8-11. Archived Messages--------------------------
def send_messages(messages, sent_messages):
    """Prints each message and moves it to sent_messages."""

    while messages:
        current_message = messages.pop()

        print(current_message)

        sent_messages.append(current_message)


messages = [
    "Hello, how are you?",
    "Python is fun to learn.",
    "Keep practicing your coding.",
    "You are doing great!"
]

sent_messages = []

send_messages(messages.copy(), sent_messages)

print("\nOriginal messages:")
print(messages)

print("\nSent messages:")
print(sent_messages)

