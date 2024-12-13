# now creating a single function that does both encryption and decryption 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# in this we will create a fully functional ceaser program based on the previous two files that we made
# We now know the logic behind both and will create a single function that does both encryption and decryption
# we will also take symbols and numbers as input and will keep them as it is

# we start by creating the function called caeser
# this will take all 3 parameters defined at top 

def caeser(original_text, shift_amount, encode_decode):
  new_word = ""
  for letter in original_text:    
    if letter in alphabet and encode_decode == "encode":
      current_word = alphabet.index(letter)
      encrypted_word_index_value = (current_word + shift_amount) % len(alphabet)
      new_word = new_word + alphabet[encrypted_word_index_value]
    elif letter in alphabet and encode_decode == "decode":
      current_word = alphabet.index(letter)
      encrypted_word_index_value = (current_word - shift_amount) % len(alphabet)
      new_word = new_word + alphabet[encrypted_word_index_value]
    else: # this is basically if letter not in alphabet condition then we add the letter to the string
      new_word = new_word + letter
  print(f"Here is your {encode_decode}d word : {new_word}.")

# now our function is complete 
# we will call it in a loop so that it runs as long as the user wants
# we will declare a variable to have a condition for our while loop

restart = "yes"

while restart != "no":
  caeser(original_text=text, shift_amount=shift, encode_decode=direction)
  go_again = input("Type yes to go again. Type no to end. : ").lower()

  restart = input("Type yes to go again. Type no to end. : ").lower()
  

  

      




