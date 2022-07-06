# -*- coding: utf-8 -*-
"""
Name: character-counter.py
Author: Ashley Emetarom
Version: 1.0
Purpose: Prompts user for their name and returns the amount of characters in
the name.

Variables

num num_chars = the amount of chars in the user's name

"""

num_chars = len(input("What is your name? "))

print("Your name has " + str(num_chars) + " characters.")