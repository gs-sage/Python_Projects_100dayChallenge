# Same as calculator one but using recursion instead

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculation():
  print(art.logo)
  # adding the operator signs to a dictionary
  operator_dictionary = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide,}
  total_calc = 0
  # creating a loop so it runs basically forever
  # but if the user chooses no then it clears the previous and starts over
  # also need to have a variable that will store previous calculations if
  # user chooses yes
  first_number = float(input("What is the first number? "))
  while True:
    second_number = float(input("What is the second number? "))
    for key in operator_dictionary:
      print(key)
    
    operation = input("Enter an operation : ")
    
    if operation in operator_dictionary:
      total_calc = operator_dictionary[operation](first_number, second_number)
      print(f"{first_number} {operation} {second_number} = {total_calc}.")
    
    user_input = input(f"Type 'y' to continue with {total_calc}. Type 'n' to start new calculation. : ").lower()
    
    if user_input == "y":
      # removing this here so that the errors with looping are gone
      # second_number = float(input("What is the second number? "))
      first_number = total_calc
    
    elif user_input == "n":
      print(art.logo)
      calculation() # called the function in itself. Using recursion concept


calculation()
















