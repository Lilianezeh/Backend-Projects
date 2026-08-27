# -----------------5-8: Hello Admin---------------------

usernames = ['admin', 'jaden', 'priya', 'kwame', 'sofia']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")


# -----------------5-9: No Users---------------------
usernames = []  

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")



# -----------------5-10: Checking Usernames---------------------
current_users = ['Admin', 'Jaden', 'Priya', 'Kwame', 'Sofia']
new_users = ['jaden', 'Marcus', 'PRIYA', 'Delphine', 'Tobias']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"'{new_user}' is available.")



# -----------------5-11: Ordinal Numbers---------------------

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")