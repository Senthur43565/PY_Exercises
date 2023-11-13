# get input from user
# check user input
# create a random choice
# compare user and random option
# display result with guesses


import sys
import random
from enum import Enum

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSOR = 3


player_choice = int(input("Enter your choice:\n 1.Rock \n 2.Paper \n 3.scissor\n"))

onOff = False

if player_choice < 1 or player_choice > 3:
  sys.exit("Enter valid choice....")

random_choice = random.choice("123")
computer_choice  = int(random_choice)

print(f"You chose:  "+str(RPS(player_choice)).replace('RPS.','') + f"\nComputer chose:"+ str(RPS(computer_choice)).replace('RPS.',''))

if player_choice == 1 and computer_choice == 3:
  print("You win 😁")
elif player_choice == 2 and computer_choice == 1:
  print("You win 😍")
elif player_choice == 3 and computer_choice == 2:
  print("You win 👌")
elif player_choice == computer_choice:
  print("Tie game")
else:
  print("Computer Wins 😒")



