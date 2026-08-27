import json


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def record_payment(payments, members):
    house_number = input("Enter house number: ").strip()

    if house_number not in members:
        print("No member is registered under the house number.")
        return False

    try:
     amount = float(input("Enter amount paid: ").strip())
    except ValueError:
        print("Please Enter a valid Amount")
        return False
    
    if amount <= 0:
        print("Amount must be greater than zweo.")
        return False
    
    if round(amount, 2) != amount:
        print("Amount cannot have more than 2 decimal places.")
        return False

    month = input("Enter month paid for: ").strip().title()
    
    parts = month.split()
    
    if len(parts) != 2 or parts[0] not in MONTHS or not parts[1].isdigit():
        print("Please enter the month in this format: August 2026.")
        return False
    
    year = int(parts[1])
    
    if year <2020 or year > 2100:
        print("Please enter a valid year.")
        return False
    
    for payment in payments:
        if payment["house_number"] == house_number and payment["month"] == month:
            print(f"House {house_number} has already paid for {month}.")
            return False

    # -------- create a payment dictionary ----------
    payment = {
        "house_number": house_number,
        "amount": amount,
        "month": month
    }

    payments.append(payment)

    print("Payment recorded successfully.")
    return True
    

def save_payments(payments):
    try:
        with open("data/payment.json", "w") as file:
            json.dump(payments, file, indent =4)
        
        print("Payment saved successfully.")
        return True

    except OSError:
        print("Unable to save payment records.")
        return False
    
    
def display_payments(payments):
    """Displays all the payments that have been recorded"""
    
    print("\n---Payment Records---")
    
    if not payments:
        print("No payment records found.")
        return
    
    for payment in payments:
        print(
            f"\nHouse: {payment['house_number']:<12}"
            f"\nAmount: ₦{payment['amount']:<12}"
            f"\nMonth: {payment['month']:<12}"
        )
        
        
def view_house_payments(payments, members):
    """To view the payment history for each house"""
    
    house_number = input("Enter house number: ").strip()
    
    if house_number == "":
        print("House number cannot be empty.")
        return
    
    if house_number not in members:
        print("No member is registered under the house number.")
        return
    
    found = False
    
    for payment in payments:
        if payment["house_number"] == house_number:
            print(
                f"\nHouse: {payment['house_number']:<12}"
                f"\nAmount: ₦{payment['amount']:<12}"
                f"\nMonth: {payment['month']:<12}"
            )
            
            found = True
            
    if not found:
            print(f"\nNo payment records found for house {house_number}.")
            
            
def check_payment_status(payments, members):
    """Checks whether a house has paid for a particular month"""
    
    house_number = input("Enter house number: ").strip()
    
    if house_number == "":
        print("House number cannot be empty.")
        return
    
    
    if house_number not in members:
        print("No member is registered under the house number.")
        return
    
    month = input("Enter month: ").strip().title()
    
    if month == "":
        print("Month cannot be empty.")
        return
    
    for payment in payments:
        if payment["house_number"] == house_number and payment["month"] == month:
            print("\nPayment Status: PAID")
            print(f"Amount Paid: ₦{payment['amount']}")
            return
        
    print("\nPayment Status: NOT PAID")
            

def load_payments():
    try:
        with open("data/payment.json", "r") as file:
            payments = json.load(file)
            
        print("Payment loaded successfully")
        return payments
    
    except FileNotFoundError:
        print("No payment file found. Starting with an empty list.")
        return []
    
    except json.JSONDecodeError:
        print("Sorry, the payment records are corrupted.")
        return []
    