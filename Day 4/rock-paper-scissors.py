# -*- coding: utf-8 -*-
"""
Name: Rock Paper Scissors
Author: Ashley Emetarom
Version: 1.0 (July 8, 2022)
Purpose: A simple rock paper scissors game played against the computer.

Variables
string rock - ASCII art for rock
string paper - ASCII art for paper
string scissors - ASCII art for scissors
bool game_over - Toggle for the game loop.
list (string) choices - collection of possible choices for player and cpu
num choice - player's selection between rock paper and scissors
string player_choice - list item from player's choice
num random_select - random number for cpu's choice
string cpu_choice - list item from cpu's choice

"""
import random

## ASCII art for the game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_over = False
choices = ["rock", "paper", "scissors"]
while game_over == False:
    # Player's selection.
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

    player_choice = choices[choice]

    if player_choice == "rock":
        print(rock)
    elif player_choice == "paper":
        print(paper)
    elif player_choice == "scissors":
        print(scissors)
    else:
        print("Invalid entry.")

    print(f"You chose {player_choice}.")

    # CPU's selection via random number generation.
    random_select = random.randint(0, len(choices) - 1)

    cpu_choice = choices[random_select]
    if cpu_choice == "rock":
        print(rock)
    elif cpu_choice == "paper":
        print(paper)
    else:
        print(scissors)

    print(f"CPU chose {cpu_choice}.")

    # Determine who wins.
    if player_choice == cpu_choice:
        print("It's a draw!")
    
    # Losing conditions for the player.
    elif (player_choice == "rock" and cpu_choice == "paper") or (player_choice == "paper" and cpu_choice == "scissors") or (player_choice == "scissors" and cpu_choice == "rock"):
        print("You lose.")
# If none of the conditions are met, victory!
    else:
        print("You win!")
    # Play again or end the game loop.
    play_again = input("\nWould you like to play again? Y or N: ")
    if play_again.lower() == "n":
     game_over = True
     print("Thanks for playing!")
     

