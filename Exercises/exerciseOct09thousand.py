# def main():
#     print("hello")

# if __name__ == "__main__":
#     main()


# print("hello", end="")
# print("world")

# import sys
# def python_space():
#   sys.stdout.write("hello")
#   sys.stdout.write("world")
# python_space()

# check converted to interger
# person1 = input("Enter age")
# print(person1)
# print(person1.isnumeric())
# print(person1.isalpha())
# if person1 == True:
#   print("its a numeber")
# elif person1 == False:
#   print("its a string")
# else:
#   print("invalid")


# # expected answer
# def main():
#   expected = 42
#   user_input = input("Enter \n")
#   user_input = int(user_input)
#   if user_input == expected:
#     print("welcome")
# main()

# # check whether division
# import time
# def main():
#   a = int(input("Enter value of a:\n"))
#   b = int(input("Enter value of b:\n"))
#   if b == 0:
#     print(f"{a} is not divisible by {b}")
#   else:
#     c = a/b
#     time.sleep(2)
#     print(f"division of {a} and {b} is2 {c}")
# main()


# # to check number equality
# def main():
#     a = int(input("Enter a :\n"))
#     b = int(input("Enter b :\n"))
#     if a == b:
#         print(f"the answer is {a} = {b}")
#     else:
#         output = "a is greater than b" if a > b else "b is greater than a"
#         # simplified if-else statement
#         print(output)
# main()

# # calculate area of rectangle
# def main(a,b):
#   area = a * b
#   print(area)
# length = int(input("Enter L :\n"))
# width = int(input("Enter W :\n"))
# output = 'invalid' if length <= 0 or width <= 0 else main(length , width)
# print(output)
# # if length <= 0 or width <=0:
# #   print("Invalid")
# # else:
# #   main(length, width)


# import sys
# def main():
#   print(len(sys.argv))
# main()

# # EVAL method
# def main():
#     a = 3
#     b = 5
#     operation = input("enter operation : \n")
#     output = f"{a}  {operation}  {b}"
#     print(output)
#     result = eval(output)
#     print(result)
# main()

# from __future__ import print_function
# print(2/2)

# import random
# # a = random.random()
# # print(a)
# print(random.random())
# print(1 + int(6 * random.random()))

# import random
# fruits = ["Apple", "Banana", "Peach", "Orange", "Durian",
# "Papaya"]
# select = random.sample(fruits,3)
# print(select)

# hidden = random.randrange(1,21)
# print(hidden)
# use_guess = int(input("Enter guess:\n"))

# if use_guess == hidden:
#   print("hit")
# else:
#   output = 'Guess if greater' if use_guess > hidden else 'Guess is less'
#   print(output)

# money = int(input("enter:\n"))
# def good_money():
#   money > 10000
# def some_money():
#   money > 10000
# while True:
#   has_good = good_money
#   has_some = some_money
#   if has_good or has_some:
#     print("live")
#     break


# a = int(input("Enter a :\n"))
# b = int(input("Enter b :\n"))
# if a == b:
#   print("Equals")
# else:
#   output =  f"a :{a} is greater than b : {b}" if a > b else f"b :{b} is greater than a : {a}"
#   print(output)


# fake message
import random
import pyautogui as pg
import time
time.sleep(1)
animal = ('fuck', 'bullshit', 'idiot', 'you')
games = ('pubg', 'forza', 'COD', 'ClashOf Clans')

for _ in range(5):
    a = random.choice(animal)
    pg.write(f"you are a {a}")
    pg.press("enter")

for _ in games:
    randoms = random.choice(games)
    pg.write(f"you wanna play: {randoms}")
    pg.press("enter")
