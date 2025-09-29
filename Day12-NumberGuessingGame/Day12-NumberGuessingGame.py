import random

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ]
random_num = random.choice(number)

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.\nCan you guess the number?")
game_level = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()


def easy_level():
    for attempt in range(10, -1, -1):
        if attempt != 0:
            print(f"You have {attempt} attempts left")
            user_guess = int(input("Make a guess: "))
            if user_guess > random_num:
                print("Too high!")
            elif user_guess < random_num:
                print("Too low!")
            elif user_guess == random_num:
                print("You win!\nYou guessed the number correctly.")
                break
        elif attempt == 0:
            print(f"You have {attempt} attempt left.\n You lose!")
            break


def hard_level():
    for attempt in range(5, -1, -1):
        if attempt != 0:
            print(f"You have {attempt} attempts left")
            user_guess = int(input("Make a guess: "))
            if user_guess > random_num:
                print("Too high!")
            elif user_guess < random_num:
                print("Too low!")
            elif user_guess == random_num:
                print("You win!\nYou guessed the number correctly.")
                break
        elif attempt == 0:
            print(f"You have {attempt} attempt left.\n You lose!")
            break


if game_level == "easy":
    print("You chose easy. You have 10 tries to guess the number.")
    easy_level()
elif game_level == "hard":
    print("You chose hard. You have 5 tries to guess the number.")
    hard_level()
else:
    print("Invalid input!")


