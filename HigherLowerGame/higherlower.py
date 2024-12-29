import game_data
import art
import random

# need to generate two random data
def random_personality_generator(data):
    new_data = random.choice(data)
    return new_data

# create a function that takes the random generator as input and uses
# its return value to compare each time
# I could create an empty dictionary or list that takes the random value each time
# then it takes the item name and prints or whatever we need to do
def add_data(empty_list, data):
    for i in range(2):
        random_value = random_personality_generator(data)
        empty_list.append(random_value)

    print(empty_list) # to confirm it is adding those data to the list

    # if empty_list[0]["follower_count"] > empty_list[1]["follower_count"]:
    #     print(empty_list[0]["follower_count"])
    # else:
    #     print(empty_list[1]["follower_count"])

# created a personality printer function that takes a list and prints the output data
# created this as a separate function instead of keeping it inside the main logic function
def personality_printer(takes_list):
    item_one = takes_list[0]
    item_two = takes_list[1]
    print(f'Compare A : {item_one["name"]}, {item_one["description"]}, from {item_one["country"]}')
    print(art.vs)
    print(f'Against B : {item_two["name"]}, {item_two["description"]}, from {item_two["country"]}')

    if item_one["follower_count"] > item_two["follower_count"]:
        guess = "A"
    else:
        guess = "B"
    return guess

def higherlower():
    print(art.logo)
    gamedata = game_data.data
    new_list = []
    game_continue = True
    score = 0

    add_data(new_list, gamedata)
    guess = personality_printer(new_list)

    # we compare then remove the right one and old second one becomes first
    # the loop will add another one to the list, and we keep going till
    # user fails
    # first_item = new_list[0]
    # second_item = new_list[1]

    # compare the follower count of the two data
    # ask for user input again and repeat till user guesses incorrect
    while game_continue:

        # if first_item["follower_count"] > second_item["follower_count"]:
        #     guess = "A"
        # else:
        #     guess = "B"

        # ask user for input
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # check if user input is correct

        if user_guess == guess:
            print("right")
            # if correct take the less follower value as new input A
            new_list.pop(0)

            # generate a new random data
            new_list.append(random_personality_generator(gamedata))
            guess = personality_printer(new_list)
            print(new_list)
            score += 1
            print(f"Your current score is {score}.")
            print(guess) # for testing purposes I printed it here
        else:
            print("wrong")
            print(f"Sorry that was wrong. Your final score is {score}.")
            game_continue = False


higherlower()



