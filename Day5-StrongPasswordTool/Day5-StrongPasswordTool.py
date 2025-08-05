import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = []

print("Welcome to the Strong Password Tool! 🔐")
print("What would you like to do?\n1. Generate a secure password\n2. Check strength of your own password")
choice = input("Enter 1 or 2: ")

#option 1: generate password
if choice == "1":
    user_letters = int(input("How many letters?: "))
    user_numbers = int(input("How many numbers?: "))
    user_symbols = int(input("How many symbols?: "))

    for char in range(0, user_letters):
        password_list.append(random.choice(letters))
        
    for char in range(0, user_numbers):
        password_list.append(random.choice(numbers))

    for char in range(0, user_symbols):
        password_list.append(random.choice(symbols))
   
    random.shuffle(password_list)
    password = "".join(password_list)
    print("Generating your password...")
    print(f"✅ Your generated password is:{password}")
    # Evaluate generated password
    if len(password) >= 12:
        print(f"This is a strong password! 👍\n- Password is long enough\n- Contains {len(password)} characters")
    else:
        print("- Password could be longer (12+ characters recommended)")
    
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if has_letter and has_number and has_symbol:
        print("- Password includes letters, numbers, and symbols ✅")
    else:
        print("- Password could be stronger. Mix letters, numbers & symbols.")

#option2 : evaluate password
elif choice == "2":
    user_password = input("Enter your password: ")
    print("Evaluating password...")
    
    has_letter = any(char.isalpha() for char in user_password)
    has_number = any(char.isdigit() for char in user_password)
    has_symbol = any(not char.isalnum() for char in user_password)

    length_user_password = len(user_password)
    

    if length_user_password >= 12 and has_letter and has_number and has_symbol:
        print("✅ Your password is strong!")
        print(f"- {length_user_password} characters")
        print("- Includes letters, numbers, and symbols")
    else:
        print("⚠️ Your password is weak!")
        if length_user_password < 12:
            print(f"- Only {length_user_password} characters. Make it longer.")
        if not has_letter:
            print("- No letters found")
        if not has_number:
            print("- No numbers found")
        if not has_symbol:
            print("- No symbols found")
        print("- Try using a mix of all three.")

else:
    print("❌ Invalid choice. Please restart and select 1 or 2.")
