# -*- coding: utf-8 -*-
"""
Name: Treasure Island
Author: Ashley Emetarom
Version: 2.0 (July 7, 2022)
Purpose: An improved version of Treasure Island that adds personalization, battles,
and variable treasure.

Variables

string first_name - Character's first name'
string last_name - Character's last name'
num party_size - Size of the party for treasure to be split between

"""
import random

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

print("Welcome to Treasure Island 2.0!")
# Set initial variables. 
gameOver = False
first_name = input("Please enter your character's first name: ")
last_name = input("Please enter your character's last name: ")
party_size = int(input("How many people (including yourself) are coming along on this adventure? "))



print(f"\nHere begins the adventure of the brave treasure hunter, {first_name} {last_name}...")

if party_size > 1:
    print(f"...and their merry band of {party_size - 1}!\n\n")
# Begin game loop.

while gameOver == False:
    player_health = random.randrange(20,40)
    #First dialog options.
    choice1 = ""
    while choice1 != "explore" and choice1 != "leave":   
        choice1 = input("You wake up near the opening to a dark, damp cave. Type \"explore\" to venture into the cave, or type \"leave\" to get out. ")
        choice1 = choice1.lower()
        if choice1 == "explore": # First battle encounter. 
            print("\nYou encounter a creepy skeleton!")
            battle_choice = ""
            battle_choice = input("\nDo you want to \"fight\" or \"run\"? ")
            battle_choice = battle_choice.lower()
            if battle_choice != "run":
                if battle_choice == "fight": #Start battle sequence.
                    battle_mode = True
                    skeleton_health = 30
                    turn = random.randrange(1,100) #Who gets first attack?
                    while player_health > 0 and skeleton_health > 0:
                        if turn % 2 ==  0:
                            player_damage = random.randrange(5,15)
                            skeleton_health -= player_damage
                        else: 
                            monster_damage = random.randrange(5,15)
                            player_health -= monster_damage
                   
                        turn += 1
                    if player_health <= 0:
                       #Oops, the player died. Game over.
                        print("\nYou have been defeated. And so your story ends...")
                        gameOver = True
                        
                    elif skeleton_health <= 0:  #Monster dies.             
                        print("You defeated the skeleton! Yay!")
                        choice1 = "leave"
                else:
                    print("\nInvalid option. You lose a turn.")
                    turn += 1
            elif battle_choice == "run":
                print("\nYou run away to fight another day!")
                choice1 = "leave"
        if choice1 == "leave":
                print("\nYou decide that the cave may be too dangerous to explore, so you leave the cave and venture out to a sandy beach. There is another island not too far from where you are.") 
        elif gameOver == False:
            print("\nInvalid option.\n")
# Second dialogue options.
    choice2 = ""
    while choice2 != "swim" and choice2 !="boat" and gameOver == False:
        choice2 =input("\nAlthough you believe it is within swimming distance, you're also considering making a makeshift boat to ensure that you make it over safely. Type \"swim\" to attempt to swim over to the island, or \"boat\" to build a boat.")
        choice2 = choice2.lower()
        if choice2 == "swim":
               # Placeholder for potentially difficult random encounter.
               print("Random hard encounter.")
               print("\nYou managed to defeat the monster and swim the rest of the way.")
        elif choice2 == "boat":
              # Placeholder for easier random encounter, if any.
            print("\nYou decide to make a boat using pieces of wood strewn about the beach and the tools that you brought with you. After working for sometime, you finally build a boat and paddle your way over to the other island.")
        else:
            print("\nInvalid option.")
    # Third dialogue options.
    choice3 = ""
    while choice3 !="red" and choice3 !="yellow" and choice3 != "blue" and gameOver == False:
           choice3 = input("\nUpon landing on the island, you find a small, seemingly abandoned house. You enter the house to investigate, and find a prismatic key and three colored doors. Which door do you want to unlock? Type \"red\", \"yellow\", or \"blue\". ")
           choice3 = choice3.lower()
           if choice3 == "red":
               # TODO: Something a bit more descriptive. May kill, may not.
               print("You take environmental damage. The key breaks. Game over.")
           elif choice3 == "blue":
               # TODO: Actually hard encounter. Player unlikely to win.
               print("Random hard encounter. Room full of beasts. The key breaks. Game over.")
           elif choice3 == "yellow":
               # TODO: Have the treasure chest contain a random amount of gold to be split amongst the party.
                print("Congratulations! You have found the treasure! You win!")
           else:
                print("You pick an invalid option and eventually the key breaks on its own. Game over.")
           gameOver = True
    
    if gameOver == True: # Give the option to start a new game.
        replay = input("\nWould you like to play again? Y or N? ")
        replay = replay.lower()
        if replay == "y" or replay =="yes":
            gameOver = False
        else:
            print("Thanks for playing!")

