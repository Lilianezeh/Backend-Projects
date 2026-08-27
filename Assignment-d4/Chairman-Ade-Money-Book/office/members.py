import json

def add_member(members):
    """Add members that lives in the Estate"""
    
    house_number = input("Enter house number: ").strip()
    
    if house_number == "":
        print("House number cannot be empty.")
        return False
    
    name = input("Enter member name: ").strip()
    
    if name == "":
        print("Member name cannot be empty.")
        return False
    
    phone = input("Enter member phone number: ").strip()
    
    if phone == "":
        print("Phone number cannot be empty.")
        return False
    
    if not phone.isdigit():
        print("Phone number must contain only digits.")
        return False
    
    if len(phone) != 11:
        print("Phone number must be 11 digits.")
        return False
    
#--------check whether the house already exist -----
    if house_number in members:
        print("That house number is already registered.")
        return False
    
    members[house_number] = {
        "name": name,
        "phone": phone   
    }
    
    save_new_member(house_number, name, phone)
    
    print("Member has been added successfully.")
    return True
    
    
def save_members(members):
    try:
        with open("data/members.json", "w") as file:
            json.dump(members, file, indent=4)

        print("Members saved successfully.")
        return True

    except OSError:
        print("Unable to save member records.")
        return False
    

def load_members():
    try:
        with open("data/members.json", "r") as file:
            members = json.load(file)

        return members

    except FileNotFoundError:
        return {}

    except json.JSONDecodeError:
        print("Sorry, the member records are corrupted.")
        return {}
    
    
def find_member(members):
    """Find a member using their house number"""
    
    house_number = input("Enter house number to search: ").strip()
    
    if house_number == "":
        print("House number cannot be empty")
        return

    if house_number in members:
        member = members[house_number]

        print("\nMember found.")
        print(f"House number: {house_number}")
        print(f"Name: {member['name']}")
        print(f"Phone: {member['phone']}")

    else:
        print("No member was found for that house number.")
        

def save_new_member(house_number, name, phone):
    """Save a newly registered member to a text file."""
    
    with open("new_member.txt", "a") as file:
        file.write(
            f"House Number: {house_number}\n"
            f"Name: {name}\n"
            f"Phone: {phone}\n"
            f"------------------------\n"
        )
        
    print("New member record saved successfully.")