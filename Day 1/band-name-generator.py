# -*- coding: utf-8 -*-
"""
Name: band-name-generator.py
Author: Ashley Emetarom
Version: 1.0 (July 5, 2022)
Summary: Prompts the user for the name of the city they grew up in, as well as
their pet's name and combines the two to form a possible band name.

Variables

string city - name of the city the user grew up in
string pet - name of the user's pet
string final - the combination of city and pet to be printed out

"""

print("Welcome to the Band Name Generator.\n")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\nHouston")
final = city + " " + pet
print("Your band name could be", final)
