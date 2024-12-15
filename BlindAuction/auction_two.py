# creating another auction python program but this time just 
# using the while loop and no for loop

# creating another auction python program but this time just
# using the while loop and no for loop

bid_dictionary = {}
ask_user = "yes"
current_highest_bid = 0
winner = ""  # declaring the empty string to be used by the key value

while ask_user == "yes":
    user_input = input("What is your name? ")
    user_bid = int(input("What is your bid? "))
    # once we have the inputs we want to add them to the dictionary
    # to do this we will also need to create an empty dictionary at the top
    bid_dictionary[user_input] = user_bid

    print(bid_dictionary)  # this is just for testing

    # we also want the program to repeat asking the inputs
    # till there are people who want to bid
    # we will need a variable that will be used for this

    ask_user = input("Are there other bidders? Type 'yes' or 'no'. \n").lower()  # converting it to lowercase

    # now we have the primary logic for the program done
    # this will take user input, add it to dictionary and
    # also ask if they want to continue
    # now we need to add a loop to this so it repeats till the condition is true
    # now we go to the top and add a while loop

    # now we have a loop that will run till condition is true

    # now we need a logic that will go through the dictionary
    # and find out the highest bidder

    if bid_dictionary[user_input] > current_highest_bid:
        current_highest_bid = bid_dictionary[user_input]
        winner = user_input

# now we print the highest bidder
# print(f"The winner is {bid_dictionary[key]} with a bid of ${current_highest_bid}.") # tested this and found the code doesn't print the user name but the value
# since the key is not a global variable we can't use it in a proper way
# we will need another global variable that will take the value of key
# we will define a global empty string variable and assign it the value of key
# printing it again using the winner variable
print(f"The winner is {winner} with a bid of ${current_highest_bid}.")



