balance = 1000

def check_balance():
    print(f"Your current balance is {balance} rupee")

def deposit_money():
    global balance
    deposit = int(input("Enter the amount you want to deposit: "))
    if deposit > 0:
        balance = balance + deposit
        print(f"rupee {deposit} deposited successfully!")
        print(f"Your updated balance is rupee {balance}")
    else:
        print("Please enter a valid deposit amount!")

def withdraw_money():
    global balance
    withdraw = int(input("Enter the amount you want to withdraw: "))
    if withdraw <= 0:
        print("Please enter a valid withdrawal amount!")
    elif withdraw > balance:
        print("Insufficient balance!")
    else:
        balance = balance - withdraw
        print(f"Your updated balance is rupee {balance}")

while True:
    print("WELCOME TO SIMPLE ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter which option you want to choose (1/2/3/4): ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("You entered an invalid choice!")