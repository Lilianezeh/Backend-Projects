#Exercise 1 -Declare and Print Variables

instructor = "Alex"
students = 30
course = "Python"

print(f"The instructor is {instructor}, there are {students} students in the {course} class!")

#Exercise 2 — Swap Two Variables Without a Third Variable

students_morning = 15 
students_evening = 25

print(f"Before Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")
students_morning, students_evening = students_evening, students_morning
print(f"After Swap: Evening Batch = {students_evening}, Morning Batch {students_morning}")

#Exercise 3 — Assign Multiple Variables in One Line

python_students = 25
java_students = 18
ai_students = 12

print(f" Python = {python_students}, Java = {java_students}, AI = {ai_students}")

#Exercise 4 — Check the Type of a Variable

age = 21
course_rating = 4.9
course_name = "Python programming"

print(f"{age} is of type {type(age)}")
print(f"{course_rating} is of type {type(course_rating)}")
print(f"{course_name} is of type {type(course_name)}")

#Exercise 5 — Concatenating Strings

instructor = "Alex"
academy = "Lkhibra Academy"
slogan = "Learning Python is fun!"

print("The instructor at " + academy + " says: \"" + slogan + "\"")

#Part B — Data Types & Conversions

#Exercise 6 — Convert String to Integer and Vice Versa
str_num = "100"
int_num = int(str_num)

int_value = 42
str_value = str(int_value)

print(f"Integer_value: {int_num}, Type: {type(int_num)}")
print(f"String value: {str_value}, Type: {type(str_value)}")

#Exercise 7 — Convert Float to Integer and Vice Versa

float_num = 9.75
int_num = int(float_num)

int_value = 50
float_value = float(int_value)

print(f"Float to Int: {int_num}, Type: {type(int_num)}")
print(f"Int to Float:{float_value}, Type: {type(float_value)}")

#Exercise 8 — Convert a Boolean to an Integer
true_value = int(True)
false_value = int(False)

print(f"True as an integer: {true_value}")
print(f"False as an integer: {false_value}")

#Exercise 9 — Convert List to a String and Back
words = ["Python", "is", "amazing"]

sentence = ", ".join(words)

words_again = sentence.split(", ")

print(f"List to String: {sentence}")
print(f"String to List: {words_again}")

#Exercise 10 — Convert Dictionary Keys and Values to Lists
course = {
    "name": "Lkhibra Academy",
    "age": 5,
    "language": "Python"
}

keys = list(course.keys())
values = list(course.values())

print(f"Keys: {keys}")
print(f"Values: {values}")

#Part C — Operators & Expressions

#Exercise 11 — Perform Arithmetic Operations

a, b = 10, 5
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Modulus: {a % b}")

#Exercise 12 — Use Comparison Operators
x, y = 10, 5
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} == 10: {x == 10}")
print(f"{x} != {y}: {x != y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

#Exercise 13 — Use Logical Operators
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"Not True: {not True}")

#Exercise 14 — Use Assignment Operators
value = 10
print(f"Initial Value: {value}")
value += 5
print(f"After += : {value}")
value -= 3
print(f"After -= : {value}")
value *= 2
print(f"After *= : {value}")
value /= 3
print(f"After /= : {value}")
value %= 8
print(f"After %= : {value}")

#Exercise 15 — Use Bitwise Operators
p, q = 5, 3
print(f"{p} & {q} = {p & q}")
print(f"{p} | {q} = {p | q}")
print(f"{p} ^ {q} = {p ^ q}")
print(f"{p} << 1 = {p << 1}")
print(f"{p} >> 1 = {p >> 1}")

#Part D — Conditionals

#Exercise 16 — Check if a Number is Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

#Exercise 17 — Find the Largest Number
nums = input("Enter three numbers (separated by spaces): ").split()
n1, n2, n3 = int(nums[0]), int(nums[1]), int(nums[2])
if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3
print(f"The largest number is {largest}.")


#Exercise 18 — Check if a Year is a Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Exercise 19 — Grade Classifier
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score} -> Grade: {grade}")


#Part E — String Operations & Formatting

#Exercise 20 — Extract the Domain from an Email
email = "lilianezichi@gmail.com"
domain = email.split("@")[1]
print(f"Domain: {domain}")

#Exercise 21 — Count the Occurrences of a Word in a Review
review = "The quality of food is great, I had a quality time with friends, The quality of their service is great"
word_to_count = "quality"
count = review.lower().split().count(word_to_count)
print(f"The word '{word_to_count}' appears {count} times.")

#Exercise 22 — Format an Invoice
CARD_WIDTH = 20
items = [("Laptop", 1200.99), ("Mouse", 25.50)]
print(f"{'Item': <12}Price")
print("-" * 19)
for item_name, price in items:
    print(f"{item_name:<12}${price:.2f}")


#Exercise 23 — Reverse Words in a Sentence
sentence = "Lkhibra Academy is great"
reversed_sentence = " ".join(sentence.split()[::-1])
print(reversed_sentence)


#Exercise 24 — Extract Hashtags from a Social Media Post
post =  "Loving #Python and #Coding at #LkhibraAcademy"
hashtags = [word for word in post.split() if word.startswith("#")]
print(f"Hashtags: {hashtags}")


#Exercise 25 — Validate a Password Strength
password = "Blessing@1512"
has_min_length = len(password) >= 8
has_number = any(char.isdigit() for char in password)
special_characters = "!@#$%^&*()_-+=[]{};:,.<>?/"
has_special_char = any(char in special_characters for char in password)

if has_min_length and has_number and has_special_char:
    print(f"'{password}' is a strong password.")
else:
    print(f"'{password}' is a weak password.")


#Exercise 26 — Remove Extra Spaces from a String
messy_text = " Hello   World  !  "
clean_text = " ".join(messy_text.split())
print(clean_text)


#Exercise 27 — Convert a String to Title Case
initial_text = "lkhibra academy python training"
title_case_text = initial_text.title()
print(title_case_text)


#Exercise 28 — Replace Words in a Text
original_text = "I love Python programming"
updated_text = original_text.replace("Python", "Java")
print(updated_text)


#Exercise 29 — Check How a String Starts or Ends
filename = input("Enter a filename: ")
if filename.startswith("report") and filename.endswith(".pdf"):
    print("This is a valid report PDF file.")
else:
    print("This is not a valid report PDF file.")


#Mini Project — Palindrome Checker
original_input = input("Enter a word or phrase: ")
cleaned_text = original_input.replace(" ", "").lower()
 
if cleaned_text == cleaned_text[::-1]:
    print(f"{original_input} is a palindrome!")
else:
    print(f"{original_input} is not a palindrome.")
