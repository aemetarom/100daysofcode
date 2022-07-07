# -*- coding: utf-8 -*-
"""
Name: Treasure Island
Author: Ashley Emetarom
Version: 1.0 (July 7, 2022)
Purpose: A simple choose your own adventure game where you have to make
decisions on where to go to find the treasure.

Variables
string choice1 - First decision for the adventure (go left or right)
string choice2 - Second decision for the adventure (wait or swim)
string choice3 - Third decision for the adventure (red, yellow, or blue)

"""
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\". ")
choice1 = choice1.lower()

if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ")
    choice2 = choice2.lower()
    if choice2 == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        choice3 = input("You arive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? ")
        choice3 = choice3.lower()
        if choice3 == "red":
            print("You walk into a room engulfed in flames. Game over.")
        elif choice3 == "blue":
            print("You walk into a room full of beasts. Game over.")
        elif choice3 == "yellow":
            print("Congratulations, you found the treasure!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
else:
    print("You fell into a hole. Game Over.")