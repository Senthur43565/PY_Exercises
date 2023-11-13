import sys
import random
playerChoice = input("enter nymber between 1 to 3\n")
player = int(playerChoice)
if player < 1 | player > 3:
    sys.exit('enter valid option')

computerChoice = random.choice("3")
computer = int(computerChoice)
print('')
print('You chose' + playerChoice)
print('Comp chose'+computerChoice)
print('')


if player == 1 and computer == 3:
    print('😍😍😍YOU WIN')
elif player == 2 and computer == 1:
    print('😍YOU WIN')
elif player == 3 and computer == 2:
    print('😍😍you WIN')
elif player == computer:
    print('TIE')
else:
    print('computer WINS🤦')
