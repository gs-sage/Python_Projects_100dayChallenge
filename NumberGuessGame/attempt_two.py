# working and adding onto attempt one this is attempt two to make this code more modular
# making more functions that handle specific parts of the logic
import random

# creating a function that returns the amount of lives
# user has based on difficulty level
def difficulty_level(user_input):
  if user_input == "easy":
    return 10
  else:
    return 5

# creating a function that validates the user input to be either easy or hard
def validate_input(user_level_choice):
  return user_level_choice == "easy" or user_level_choice == "hard" 

# creating a function that provides user winning case 
# and if the guess is higher or lower than the computer guess
def guess_checker(user_input, computer_input):
  if user_input == computer_input:
    print(f"You got it right. The answer is {user_input}.")
    return True
  elif user_input > computer_input:
    print("Too high. Guess again.")
    return False
  elif user_input < computer_input:
    print("Too low. Guess again.")
    return False


# creating the main logic function for the game
def guess_game():
  print("Welcome to the Guessing Game.")
  print("I am thinking a number between 1 and a 100.")
  
  # creating variables to store computer guess
  computer_guess = random.randint(1,100)
  
  #asking the user for the difficulty level
  level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()

  while not validate_input(level):
    print("Enter a valid choice.")
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
  
  # now using level as a argument for the difficulty level function and 
  # assigning it to a variable so we can use it
  lives = difficulty_level(level)
  
  # creating another variable that will work with lives to run a loop
  game_not_complete = True

  while game_not_complete and lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    
    # taking user input and then using if statements so all conditions work
    user_guess = int(input("Make a guess: "))

    # using the function guess checker here with user_guess and computer guess as argument
    # since this function return true or false it will help to determine if the user guessed
    # right or wrong

    if guess_checker(user_guess, computer_guess):
      game_not_complete = False
    else:
      lives -= 1
      
    if lives == 0:
      print("Your are out of lives. Game Over.")
      print(f"The correct answer was {computer_guess}.")
      game_not_complete = False

# finally calling the main function to run the game
guess_game()

    
    







