import json

def add_member(members):
    """Add members that lives in the Estate"""
    
    house_number = input("Enter house number: ")
    name = input("Enter member name: ")
    phone = input("Enter member phone number: ")
    
#--------check whether the house already exist -----
    if house_number in members:
        print("That house number is already registered.")
        return False
    
    members[house_number] = {
        "name": name,
        "phone": phone
        
    }
    
    print(f"Member has been added successfully.")
    return True
    
    
def save_members(members):
    with open("members.json", "w") as file:
        json.dump(members, file, indent =4)
        
    print("Members saved successfully.")
    

def load_members():
    try:
        with open("members.json", "r") as file:
            members = json.load(file)

        return members

    except FileNotFoundError:
        return {}
    
    except json.JSONDecodeError:
        print("Sorry, the member records are corrupted.")
        return {}
    
    
def find_member(members):
    house_number = input("Enter house number to search: ")

    if house_number in members:
        member = members[house_number]

        print("Member found.")
        print(f"House number: {house_number}")
        print(f"Name: {member['name']}")
        print(f"Phone: {member['phone']}")

    else:
        print("No member was found for that house number.")
        

# members = load_members()

# find_member(members)

# print("Current members:", members)

# while True:
#     add_member(members)
    
#     again = input("Add another member? (yes/no): ")
    
#     if again.lower() == "no":
#         break
    
# save_members(members)
    
# print(members)