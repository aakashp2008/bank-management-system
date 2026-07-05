balance = 0

while True:
    print("\n=== Bank Management System ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: ₹", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print("₹", amount, "deposited successfully.")
        else:
            print("Please enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount <= balance:
            balance -= amount
            print("₹", amount, "withdrawn successfully.")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
