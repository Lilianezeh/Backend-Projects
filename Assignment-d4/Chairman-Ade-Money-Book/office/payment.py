import json
from members import add_member, save_members, load_members, find_member


def record_payment(payments, members):
    house_number = input("Enter house number: ")

    if house_number not in members:
        print("No member is registered under the house number.")
        return False

    try:
     amount = float(input("Enter amount paid: "))
    except ValueError:
        print("Please Enter a valid Amount")
        return False
    
    if amount <= 0:
        print("Amount must be greater than zweo.")
        return False


    
    month = input("Enter month paid for: ").strip().title()
    
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
    with open("payment.json", "w") as file:
        json.dump(payments, file, indent =4)
        
    print("Payment saved successfully.")
    
    
def display_payments(payments):
    """Displays all the payments that have been recorded"""
    print("\n---Payment Records---")
    
    for payment in payments:
        print(
            f"\nHouse: {payment['house_number']:<12}"
            f"\nAmount: ₦{payment['amount']:<12}"
            f"\nMonth: {payment['month']:<12}"
        )
        
        
def view_house_payments(payments, members):
    """To view the payment history for each house"""
    
    house_number = input("Enter house number: ")
    
    if house_number not in members:
        print("No member is registered under the house number.")
        return
    
    for payment in payments:
        if payment["house_number"] == house_number:
            print(
                f"\nHouse: {payment['house_number']:<12}"
                f"\nAmount: ₦{payment['amount']:<12}"
                f"\nMonth: {payment['month']:<12}"
            )
            
            
def check_payment_status(payments, members):
    """Checks whether a house has paid for a particular month"""
    
    house_number = input("Enter house number: ")
    
    if house_number not in members:
        print("No member is registered under the house number.")
        return
    
    month = input("Enter month").strip().title()
    
    for payment in payments:
        if payment["house_number"] == house_number and payment["month"] == month:
            print("\nPayment Status: PAID")
            print(f"Amount Paid: ₦{payment['amount']}")
            return
        
    print("\nPayment Status: NOT PAID")
            

def load_payments():
    try:
        with open("payment.json", "r") as file:
            payments = json.load(file)
            
        print("Payment loaded successfully")
        return payments
    
    except FileNotFoundError:
        print("No payment file found. Starting with an empty list.")
        return []
    
    
def show_menu():
    """Displays the main menu"""

    print("\n ==== CHAIRMAN ADE MONEY BOOK ====")
    print("1. Add member")
    print("2. Record payment")
    print("3. Display all payments")
    print("4. View house payment history")
    print("5. Check payment status")
    print("6. Find member")
    print("7. Exit")

    choice = input("Enter your choice: ")

    return choice

members = load_members()
payments = load_payments()

while True:
    choice = show_menu()

    if choice == "1":
        member_added = add_member(members)
        
        if member_added:
            save_members(members)

    elif choice == "2":
        payment_recorded = record_payment(payments, members)

        if payment_recorded:
            save_payments(payments)

    elif choice == "3":
        display_payments(payments)

    elif choice == "4":
        view_house_payments(payments, members)

    elif choice == "5":
        check_payment_status(payments, members)

    elif choice == "6":
        find_member(members)

    elif choice == "7":
        print("Chairman Ade Money Book.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 7.")


