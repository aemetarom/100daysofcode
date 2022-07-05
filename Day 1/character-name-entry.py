# -*- coding: utf-8 -*-
"""
Name: character-name-entry.py
Author: Ashley Emetarom
Version: 1.0 (July 5, 2022)
Summary: Prompts the user for a first and last name to use for a game
character.

Variables

string firstName - Character's first name
string lastName - Character's last name
string fullName - Character's first and last name combined.

"""

print("Welcome to the Character Creator! \n")

firstName = input("Please enter your character's first name: ")
lastName = input("Please enter your character's last name: ")
fullName = firstName + " " + lastName

print("Your character's name is", fullName)

