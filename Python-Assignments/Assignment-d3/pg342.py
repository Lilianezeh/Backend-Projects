# -------------10-6. Addition ------------------
first_number = input("Enter a number: ")
second_number = input("Enter another number: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("Sorry, please enter valid numbers only.")
else:
    result = first_number + second_number
    print(f"The sum of {first_number} and {second_number} is {result}.")
    
    
# -------------10-7. Addition Calculator ------------------
print("Enter 'q' at any time to quit.\n")

while True:
    first_number = input("\nEnter a number: ")
    if first_number == 'q':
        break

    second_number = input("Enter another number: ")
    if second_number == 'q':
        break

    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("Sorry, please enter valid numbers only.")
        continue
    else:
        result = first_number + second_number
        print(f"The sum of {first_number} and {second_number} is {result}.")
        
        
# -------------10-8. Cats and Dogs ------------------
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} could not be found.")
    else:
        print(f"\nContents of {filename}:")
        print(contents)
        
        
# -------------10-9. Silent Cats and Dogs ------------------
filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nContents of {filename}:")
        print(contents)
        
        
 # -------------10-10. Common Words ------------------
filename = "alice_in_wonderland.txt"

try:
    with open(filename, encoding="utf-8") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} could not be found.")
else:
    lower_contents = contents.lower()
    the_count = lower_contents.count('the')
    the_space_count = lower_contents.count('the ')

    print(f"'the' appears approximately {the_count} times.")
    print(f"'the ' (with trailing space) appears approximately {the_space_count} times.")