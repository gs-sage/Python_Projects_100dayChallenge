# program based on the card roulette used to pay bills in restaurant
# the program uses the random module and its function to iterate through a list and generate a random name
# that person will be responsible to pay the bill

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


print("First way to do this using python random.choice function")
print(random.choice(friends))

print("Second way of doing it, using what I have learned till now.")

random_num_range = random.randint(0,4) # using this range since the list goes from index 0 to 4

if random_num_range == 0:
    print("Alice")

elif random_num_range == 1:
    print("Bob")

elif random_num_range == 2:
    print("Charlie")

elif random_num_range == 3:
    print("David")

else:
    print("Emanuel")


print("Third way of doing it.")

# using the same random number generator in option 2
# just using the value from that as a index number for the list in this case for list friends.

print(friends[random_num_range])
