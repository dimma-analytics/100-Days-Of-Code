print("👋 Welcome to Python Budget Tracker!")

user_choice = input("\nDo you want to set a starting balance?(yes/no): ").lower()
balance = 0
total_income = 0
total_expenses = 0
transactions = []

if user_choice == "yes":
    user_balance = float(input("Enter your starting balance(₦): "))
    balance += user_balance
    print(f"Your starting balance is ₦{balance}")
elif user_choice == "no":
    balance += 0
    print(f"Your starting balance is ₦{balance}")
else:
    print("Invalid input!\nPlease select Yes/no")



while True:
    menu = input("\nWhat would you like to do?\n1. Add Income\n2. Add Expense\n3. View Summary\n4. View Transactions\n5. Exit\nEnter your choice: ")
    print(f"\nYou selected option {menu}")
    #option1
    if menu == "1":
        income_source = input("\nWhat is your source of income?: ")
        income_amount = float(input("How much did you receive?(₦): "))
        balance += income_amount
        total_income += income_amount
        transactions.append(f"Income: +₦{income_amount} from {income_source}")
        print(f"\n✅ Income added successfully.\n💰Your current balance is ₦{balance}")
    #option2
    elif menu == "2":
        expense_reason= input("\nWhat did you spend money on?: ")
        expense_amount = float(input("How much did you spend?: "))
        balance -= expense_amount
        total_expenses += expense_amount
        transactions.append(f"Expense: -₦{expense_amount} from {expense_reason}")
        print(f"\n✅ Expense deducted successfully.\n💰Your current balance is ₦{balance}")
    #option3
    elif menu == "3":
        print("\n📊 Budget Summary: ")
        print(f"🟢 Total income: ₦{total_income}")
        print(f"🔴 Total expenses: ₦{total_expenses}")
        print(f"💰 Current balance: {balance}")
    #option4
    elif menu == "4":
        if len(transactions) == 0:
            print("🚫 No transactions recorded yet.")
        for item in transactions:
            print("\nTransaction History: ")
            print(item)
    #option5
    elif menu == "5":
        print("👋 Exiting Budget Tracker. Goodbye!")
        break
    #invalid input
    else:
        print("❌ Invalid Input! Select options 1-5.")

    
    