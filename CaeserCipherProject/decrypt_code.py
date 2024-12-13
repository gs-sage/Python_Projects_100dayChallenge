# this will be the same as the encrypt code
# the only logic difference is that we will be subtracting the shift amount
# from the index value of the word

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(original_text, shift_amount):
  decrypted_word = ""
  for letter in original_text:
    current_word = alphabet.index(letter)
    # the difference is here where we subtract the shift amount instead of adding it
    decrypted_word_index_value = current_word - shift_amount
    decrypted_word_index_value = decrypted_word_index_value % len(alphabet)
    decrypted_word = decrypted_word + alphabet[decrypted_word_index_value]
  print(decrypted_word)
