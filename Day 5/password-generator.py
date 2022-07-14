# -*- coding: utf-8 -*-
"""
Name: Password Generator
Author: Ashley Emetarom
Version: 1.0 (July 14, 2022)
Purpose: Generates a password to use for web service registration.

"""
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

print("Welcome to the PyPassword Generator!")

# Get the amount of letters, symbols, and numbers the user would like in their password.
num_letters = int(input("How many letters would you like in your password?\n"))

num_symbols = int(input("How many symbols would you like?\n"))

num_numbers = int(input("How many numbers would you like?\n"))

# Generate the letters, numbers, and symbols and include them in the password.
password_list = []
for char in range(0, num_letters):
    letter = random.choice(letters)
    password_list.append(letter)

for char in range (0, num_numbers):
    number = random.choice(numbers)
    password_list.append(number)
    
for char in range (0, num_symbols):
    symbol = random.choice(symbols)
    password_list.append(symbol)
    
# Shuffle the list of characters around and aseemble the final password.
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

# Does the same thing as above for shuffling the characters in the password.
# password = ''.join(random.sample(password, len(password)))

print(f"Here is your password: {password} ")


