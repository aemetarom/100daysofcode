""" 
Name: Caesar Cipher
Version: 1.0
Author: @aemetarom
Purpose: Encodes and decodes messages given by the user by shifting letters by a given value.
Variables:
list str alphabet - the list of letters in the english alphabet
bool keep_running - controls whether to prompt user for another message to encode or decode
str direction - user-entered choice to encode or decode
str text - text to be modified
int shift - number of times to shift from a given letter
str yes_no - input from user on whether or not they want to keep running the program
Functions:
caesar - performs encnryption or decryption depending on the direction specified and returns the encrypted or decrypted result
"""

# Modules
import art


# Functions
def caesar (start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

keep_running = True
while keep_running == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    yes_no = input("Would you like to try it again? Type'yes' or 'no'\n").lower()
    if yes_no == "no":
        keep_running = False
        print("\nGoodbye.")

