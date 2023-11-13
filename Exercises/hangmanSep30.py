# List of words for the game
# Select a random word from the list
# Initialize variables
# Display the initial message
# Main game loop
      # Display the word with blanks for missing letters

# Ask the player for a letter guess
# Check if the guess is a single letter
# Check if the letter has been guessed before
# Add the guess to the list of guesses
# Check if the guess is in the word
# Check if the player has won
# game over

import time
import random
words = ["santhana","senthur","selvan","are","you"]
randomGuess = random.choice(words)
guesses = ""
maxAttempts = 5

while maxAttempts > 0:
    displayWord = ""
    for letter in randomGuess:
        if letter in guesses:
         displayWord += "_"
    print(displayWord)

    playerGuess = input("Guess a letter" .lower())

    if len(playerGuess) != 1:
        time.sleep(2)
        print("Enter a single letter......")
        continue

    if playerGuess in guesses:
       print("You already guessed this letter....")
       continue

    guesses += playerGuess


    if playerGuess in randomGuess:
       print("good job")
    else:
       print("OOPS! its wrong")
    maxAttempts -= 1

    if all(letter in guesses for letter in randomGuess):
       print("congratulations"+ randomGuess)
       break
if maxAttempts == 0:
   print("game OVER")

      




