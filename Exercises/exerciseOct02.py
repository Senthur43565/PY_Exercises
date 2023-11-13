# import time
# userInput=int(input("Enter number:\n"))
# def funName(userInput):
#   for number in range(1,userInput):
#     if userInput %3 == 0 and userInput % 5 == 0:
#       print("FizzBuzz")
#     elif userInput % 3 == 0:
#       print("Fizz")
#     elif userInput %5 == 0:
#       print("Buzz")
#     else:
#       print(number)
# print("timing")
# time.sleep(5)
# funName(userInput)

import requests
res = requests.get(url=f"http://10.10.11.161/api")
print(res)