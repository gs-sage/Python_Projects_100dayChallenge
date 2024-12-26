import random

# Attempt 1

def guess_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_guess = random.randint(1,100)
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        lives = 10
    else:
        lives = 5
    print(f"You have {lives} attempts remaining to guess the number")

    while lives != 0:
        guess_number = int(input("Make a guess : "))

        if guess_number == computer_guess:
            print(f"You got it. The answer was {guess_number}.")
            break
        elif guess_number > computer_guess:
            print("Too high.")
            print("Guess again.")
        else:
            print("Too low.")
            print("Guess again.")

        if lives == 0:
            print("You have run out of guesses. Game over.")
            print("Run game again to play.")

guess_game()















