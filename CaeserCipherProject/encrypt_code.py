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

    # now to make sure the code doesn't get index out of range error i.e. we have an list that goes from range 0-25 
    # we are adding shift amount to get new index values based on user input
    # as long as the values are under 25 we won't get error but once they cross 25 we will get index out of bounds error
    # i.e. if the user types ze and wants a shift of 2 then the logic takes the index value of z which will be 25 and adds 2 to it
    # which will be 27 and in our list of alphabet it only goes to 25 so we will get an error
    # to resolve this we will use the modulo operator
    # this operator works since it will take the remainder value and assign it to the variable in this case variable encrypted_word_index_value
    # this works since small numbers divided by index range of alphabet which is 26 counting from 0-25 will give the remainder of the small number
    # i.e. 2/26 will have a remainder of 2 since 26 can't divide 2 and if it is a big number that is 30/26 will give remainder of 4 since 26 goes 1 time into 30
    # so this will resolve the out of bounds error for index
    # all we have to do is to take the variable and just divide it by the length of the alphabet list

    encrypted_word_index_value = encrypted_word_index_value % len(alphabet)

    # now we add those values to an string. We take the new index values and take it from the alphabet list.
    # we also need to add the empty string for this variable outside the loop 
    # or it will cause issues
    new_word = new_word + alphabet[encrypted_word_index_value]

  # now we print the new word
  print(new_word)

# now we call the function
encrypt(original_text=text, shift_amount=shift)


    
    
