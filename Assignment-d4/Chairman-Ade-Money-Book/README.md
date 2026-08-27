# Chairman Ade Money Book

A simple estate management system built with Python for recording estate members, tracking monthly payments, checking payment status, and keeping an estate diary.

---

## Description

**Chairman Ade Money Book** is a beginner-friendly Python project that helps an estate chairman or secretary manage residents and their monthly payments.

The application allows users to:

* Register estate members.
* Record monthly payments for each house.
* Prevent duplicate payments for the same house in the same month.
* View payment history for any house.
* Check whether a house has paid for a specific month.
* Keep a diary of estate meetings and activities.
* Save all records permanently using JSON files.
* Create backup copies of important records.

This project demonstrates the use of Python functions, modules, dictionaries, lists, loops, conditionals, exception handling, file handling, and JSON.

---

## Features

* Add new estate members.
* Validate member details (house number, name, and phone number).
* Find a member using a house number.
* Record monthly estate payments.
* Prevent duplicate payments for the same month.
* Display all payment records.
* View payment history for a particular house.
* Check payment status for a selected month.
* Add diary entries with the current date and time.
* Display all estate diary entries.
* Save and load records using JSON files.
* Create backup copies of data files.

---

## Project Structure

```text
Chairman-Ade-Money-Book/
│
├── main.py                 # Main application menu
├── README.md               # Project documentation
├── new_member.txt          # Log of newly registered members
│
├── office/
│   ├── __init__.py         # Makes office a Python package
│   ├── members.py          # Member management functions
│   ├── payment.py          # Payment management functions
│   └── diary.py            # Estate diary functions
│
├── data/
│   ├── members.json        # Stores member records
│   ├── payment.json        # Stores payment records
│   └── diary.json          # Stores diary entries
│
└── backups/
    ├── members_backup.json # Backup of member records
    ├── payment_backup.json # Backup of payment records
    └── diary_backup.json   # Backup of diary entries
```

---

## Technologies Used

* Python 3
* JSON
* Git
* GitHub
* Python Standard Library (`json`, `datetime`, `shutil`)

---

## How to Run the Project

### 1. Clone or download the project.

### 2. Open the project folder in your terminal.

### 3. Run the application.

```bash
py main.py
```

### 4. Use the menu.

```text
==== CHAIRMAN ADE MONEY BOOK ====

1. Add member
2. Record payment
3. Display all payments
4. View house payment history
5. Check payment status
6. Find member
7. Add diary entry
8. Display diary
9. Exit
```

Enter the number corresponding to the action you want to perform.

---

## How the Application Works

### Member Management

* Register new estate members.
* Prevent duplicate house numbers.
* Validate phone numbers before saving.
* Search for members by house number.

### Payment Management

* Record payments for registered members.
* Save payments by month.
* Prevent duplicate payments for the same house and month.
* Display payment history for a house.
* Check whether payment has been made for a particular month.

### Estate Diary

* Record important estate meetings and activities.
* Automatically save the current date and time for each entry.
* Display all diary entries.

---

## Data Storage

All application data is stored in the **`data`** folder.

| File           | Purpose                           |
| -------------- | --------------------------------- |
| `members.json` | Stores registered estate members. |
| `payment.json` | Stores payment records.           |
| `diary.json`   | Stores estate diary entries.      |

The records remain available even after the application is closed.

---

## Backup

The application creates backup copies of important records in the **`backups`** folder.

Backup files include:

* `members_backup.json`
* `payment_backup.json`
* `diary_backup.json`

These backups help preserve records in case the original data files are accidentally modified or lost.

---

## Input Validation

The application performs basic validation to improve data quality.

Examples include:

* House number cannot be empty.
* Member name cannot be empty.
* Phone number must contain only digits.
* Phone number must be exactly **11 digits**.
* Payment amount must be a valid number greater than zero.
* A house cannot pay twice for the same month.
* Diary entries cannot be empty.

---

## Python Concepts Demonstrated

This project was built using beginner-friendly Python concepts, including:

* Functions
* Modules and imports
* Lists
* Dictionaries
* Loops (`for`, `while`)
* Conditional statements (`if`, `elif`, `else`)
* Exception handling (`try` / `except`)
* File handling
* JSON serialization (`json.dump()` and `json.load()`)
* Date and time using `datetime`

---

