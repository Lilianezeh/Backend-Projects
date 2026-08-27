import shutil

from office.members import (
    add_member,
    save_members,
    load_members,
    find_member
)

from office.payment import (
    record_payment,
    save_payments,
    load_payments,
    display_payments,
    view_house_payments,
    check_payment_status
)

from office.diary import (
    add_diary_entry,
    display_diary,
    save_diary,
    load_diary
)

def backup_data():
    """Create backups of the application data files."""

    try:
        shutil.copy(
            "data/members.json",
            "backups/members_backup.json"
        )

        shutil.copy(
            "data/payment.json",
            "backups/payment_backup.json"
        )

        shutil.copy(
            "data/diary.json",
            "backups/diary_backup.json"
        )

        print("Data backup created successfully.")
        return True

    except OSError:
        print("Unable to create data backup.")
        return False


members = load_members()
payments = load_payments()
diary = load_diary()

backup_data()


def show_menu():
    """Displays the main menu"""

    print("\n ==== CHAIRMAN ADE MONEY BOOK ====")
    print("1. Add member")
    print("2. Record payment")
    print("3. Display all payments")
    print("4. View house payment history")
    print("5. Check payment status")
    print("6. Find member")
    print("7. Add diary entry")
    print("8. Display diary")
    print("9. Exit")

    choice = input("Enter your choice: ").strip()

    return choice

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
        diary_added = add_diary_entry(diary)

        if diary_added:
            save_diary(diary)

    elif choice == "8":
        display_diary(diary)

    elif choice == "9":
        print("Chairman Ade Money Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 9.")