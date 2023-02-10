"""
Name: Hangman
Version: 1.0
Author: @aemetarom
Purpose: A simple but classic word game.
Variables:
list str word_list - list of words for random selection (imported from hangman_words)
str chosen_word - randomly chosen word to be guessed
int word_length - length of the chosen word
bool end_of_game - used to determine if the game is over
int lives - amount of lives/guesses remaining
str logo - title logo (imported from hangman_art)
list str display - string list used for displaying current state of the game
str guess - a guessed letter from the user
list str stages - art of different stages of the game (imported form hangman_art)
"""
from os import system 
import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Debug - Show answer.
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range (word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()
    system("cls") # Only works on NT systems.

    if guess in display:
        print(f"You've already guessed {guess}.")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
        
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])