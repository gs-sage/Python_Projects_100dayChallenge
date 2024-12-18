# creating a calcultor program

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculation():
  # creating a dictionary that will use the math functions as values

  operation_dictionary = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide,}

  while True:
    # created inputs
    first_number = float(input("What is the first number? "))

    # creating another while loop that is always true 
    # so this keeps running till user chooses to continue with
    # previous calculation
    while True:
      second_number = float(input("What is the second number? "))
      
      # printing the operators      
      for operator in operation_dictionary:
        print(operator)
      
      operation = input("Enter an operation : ")
      
      total_calculation = operation_dictionary[operation](first_number, second_number)
      
      print(f"{first_number} {operation} {second_number} = {total_calculation}")
      
      user_input = input("Type 'y' to continue with {total_calculation}. Type 'n' to start new calculation. : ").lower()
      
      if user_input == "y":
        first_number = total_calculation
      
      else:
        break # if user chooses 'n' then this breaks it out of the inner while loop and goes back to the first one

# we could have also made this function to take dictionary as input 
# if we wanted to have the dictionary outside
calculation()






