# # calculator
# print('Welcome......')
# number1=float(input('enter first number:\n'))
# number2=float(input('enter second number:\n'))
# operation=input('enter operation (+,-,*,/):\n')

# if operation=='+':
#   result=number1+number2
# elif operation=='-':
#   result=number1-number2
# elif operation=='*':
#   result=number1*number2
# elif operation=='/':
#   result=number1/number2
# else:
#   result='Invalid operation'
# print(result)

# # finding ODD EVEN
# input = int(input('enter number:\n'))
# if input/2 == 0:
#     print('even')
# else:
#     print('odd')


# #vowels and consonants

# input=input('Enter a word:')
# vowels=0
# consonants=0
# for letter in input:
#   if letter.isalpha():
#     if letter.lower() in "aeiou":
#       vowels+=1
#     else:
#       consonants+=1
# print("Vowels:", vowels)
# print("Consonants:", consonants)


# Guess random number
import random
while True:
    userinput = int(input('Enter number 1 to 5:\n'))
    computerinput = random.randint(1, 5)
    attempts = 0
    attempts += 1
    if attempts == 5:
        break
    if userinput == computerinput:
        result = 'WIN'
    elif userinput >= computerinput:
        result = "TOO HIGH"
    elif userinput <= computerinput:
        result = 'TOO LOW'
    else:
        result = "INVALID ENTRY"

    print('you entered:\n'+str(userinput) +
          '\ncomputer choice:\n'+str(computerinput))
    print(result+'\nAttempts:'+str(attempts))
