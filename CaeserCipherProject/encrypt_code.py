# created the encrypt part of the code

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# creating an encrypt function that takes two parameters
def encrypt(original_text, shift_amount):
  # creating an empty string that will store new values created in line 32 
  new_word = ""
  
  for letter in original_text:
    print(alphabet.index(letter)) # this prints each letter the user inputs and provides its index number using the list alphabet. this can be commented out, i left it for myself to understand the logic

    # we need to create new word based on the shift amount determined by user
    # so we need to add the shift amount to the index number of each letter of the word user inputs
    # so if for example if the user types hi with shift amount of 1 what we are doing is taking the index value of h and i 
    # which will be 7 and 8 since we have them in the list alphabet
    # and then we add 1 to the index value of each letter so they becom 8 and 9. So the encrypted word becomes ij

    current_word = alphabet.index(letter) # this is the current word index values

    # this will be the new encrypted word index value since current_word 
    # will be a number since we are using the index() function to get the position of the letters from the list
    encrypted_word_index_value = current_word + shift_amount # this is not the word, this just has the index values of the new word

    # now we add those values to an string. We take the new index values and take it from the alphabet list.
    # we also need to add the empty string for this variable outside the loop 
    # or it will cause issues
    new_word = new_word + alphabet[encrypted_word_index_value]

  # now we print the new word
  print(new_word)

# now we call the function
encrypt(original_text=text, shift_amount=shift)


    
    
