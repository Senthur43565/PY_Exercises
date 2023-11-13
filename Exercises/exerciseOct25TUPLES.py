# from __future__ import print_function
# import sys
# def name():
#   print("what is your name")
#   inputs = input("your name:")
#   print(f"your name is {inputs}")
# name()


# import sys
# def main():
#   version = sys.version_info.major
#   print(version)
#   if sys.version_info[6] > 3:
#     name = input("your name")
#   else:
#     name = input("your details")
# main()


# check whether the given input can be converted to number or not

# def main():
#   value1 = input("Enter value to check")
#   decimal =  print(value1.isdecimal())
#   numeric = print(value1.isnumeric())
#   print(decimal )
#   # if value1 == numeric:
#   #   print("it cannot be converted")
#   # else:
#   #   print("YES!!!")
# main()

# # convert str to int
# val = "23"
# print(type(val))
# inte = int  (val)
# print(type(inte))


# # convert float to int
# val = 4.565
# print(type(val))
# val2 = int(val)
# print(type(val2))

# # calculatearea of triangle using try catch
# a = input("value of a")
# b = input("value of b")

# try:
#     a = int(a)
#     b = int(b)
#     print(0.5 * a + b)
# except:
#     print(f"somethind invalid")


# # calculator
# try:
#     a = int(input("enter value 1:"))
#     b = int(input("enter value 2:"))
#     operand = input("enter operation: + , - , *")
#     if operand == "+":
#         result = a + b
#     if operand == "-":
#         result = a - b
#     if operand == "*":
#         result = a * b
# except ValueError:
#     print("invalid value")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")


# # eval function - this function works like human

# a = int(input("enter 1:"))
# b = int(input("enter 2:"))
# oper = input("enter operation")
# answer = str(a) + oper + str(b)
# comman = eval(answer)
# print(comman)

# import random
# random.seed(10)
# a = random.random()
# print(a)
# print(random.random())


# import random
# letters = "123456"
# print(random.choice(letters))
# print(random.choices(letters, k = 5))


# import random
# fruits = ["Apple", "Banana", "Peach", "Orange", "Durian",
# "Papaya"]
# three_fruit = random.choices(fruits, k = 3)
# print(three_fruit)
# user_input = int(input("enter guess:  "))
# numbers = random.randrange(1)
# if user_input == numbers:
#     print("WIN!!!")
#     print(f"your guess {user_input} and computer guess {numbers}")
# else:
#     print("LOST")
#     print(f"your guess {user_input} and computer guess {numbers}")


# x = 2
# y = x==2
# if y:
#     print("true")


# values = [None, 0, "", False, [], (), {}, "0", True]
# for x in values:
#     if x:
#         print("found value", x)
#     else:
#         print("INVALID", x)


# # which number is bigger
# a = int(input("enter :  "))
# b = int(input("enter :  "))
# res = f"{a} is greateer than {b}" if a > b else f"{b} is greater than {a}"
# print(res)


# conpare strings using ASCII or length\
# a = str(input("enter :  ")).lower()
# b = str(input("enter :  ")).lower()
# compare = input("ASCII or len:   ").lower()
# if compare == "ascii":
#     if a > b:
#         print(f"a is greater")
#     elif b > a:
#         print(f"b is greater")
#     else:
#         print("both same")
# elif compare == "len":
#     if len(a) > len(b):
#         print(f"a has length")
#     elif len(b) > len(a):
#         print(f"b has length")
#     else:
#         print("both same")

# long_string = """
# hai 
# hello
# welcome
# """
# print(long_string)

# a = "hello"
# print("-"*len(a))
# chara = a[1:]
# print(chara * 2)


# good one
# import time

# text = "Hello, World!"
# for char in text:
#     print( "\r"+ char, end="")
#     time.sleep(1)  # Sleep for 1 second (adjust as needed to control speed)
# print(text)

# a = "senthurselva"
# b = a[:7] + "SANTHANA" + a[7:]
# print(b)


# text = "The black cat climbed the green tree."
# print(text.index("c"))
# print(text.rindex("c", 8, 13)) # 10


# input = "hai hello how are you"
# try:
#     ans = input.rindex("z", 2, 20)
#     print(f"your input : {input} \n and searched letter {ans}")
# except ValueError:
#     print("invalid")

# # finding in string and use of find in if else
# ani = input("find word :  ")
# inp = "hai hello how are you"
# ans = inp.rfind("ll", 0, 10)
# print(ans)
# try:
#  if "how" in inp:
#     ind = inp.index(ani)
#     print(ind)
# except ValueError:
#   print("invalid")


# use of CHR
# for all in range(16, 32):
#     print(all ,chr(all))                              # finds ASCII index for numbers between 16 to 32 

# # to find string and where
# import time
# input1 = " a b c d e f c h k l k l"
# user_input = input("enter: ")
# ans = f"your input {user_input}, found in index {input1.index(user_input)} and it was repeated {input1.count(user_input)} times" if user_input in input1 else "not found"
# for all in input1:
#     print("\r" + all, end="")
#     time.sleep(.5)    
# print(ans)

# # to find ASCII and index of user_input and print ASCII code of each character
# input1= "hai how are you"
# user_input = input("guess:  \n")
# try:
#     if user_input in input1:
#         ans = ord(user_input)                                                 
#         ind = input1.rindex(user_input, 4, 8)
#         print(ans, ind)
# except ValueError:
#     print("invalid")
# for all_let in input1:
#     print(f"index of {all_let} is {ord(all_let)}")


# # Exercise- to find ASCII of number
# user_input = int(input("enter number: "))          
# ans = chr(user_input)                                                        #finds ASCII number for input
# print(ans)

# # to eliminate duplicate len
# while True:
#  inpu = input("enter:  ")
#  length = len(inpu)
#  ans = f"you have entered {inpu}" if length == 5 else "enter valid input"    #it gives invalid if len is not as recommended
#  print(ans)
#  break


# # PASSWORD GENERATOR
# import random
# password = "abcdefghijkl329487234#$#&(*&_)"
# user_input = int(input("enter length of password: "))
# if user_input < 5 or user_input > 10:
#     print("Enter length between 5 to 10")
# else:
#     for all in password:
#         random_char = ''.join(random.sample(password, user_input))
#     print(random_char)

#guess number
# import random
# comp = random.randrange(1, 20)
# while True:
#     user = int(input(f"guess number: \n or X to exit"))
#     if comp < user:
#         print(f"BIG {comp}")
#     elif comp > user:
#         print(f"SMALL {comp}")
#     else:
#         print("WON!!")
#         break



# # display using string concatination .format, name
# name = "senthur"
# age = 27.9
# print("{} was born {} years ago ".format(name, age))
# print("{hello} was born {hwy} years ago".format(hello = name, hwy = age))

# # formatted printing
# data = [
#  ["Foo Bar", 42],
#  ["Bjorg", 12345],
#  ["Roza", 7],
#  ["Long Name Joe", 3],
#  ["Joe", 12345677889],
#  ]
# for all in data:
#     print("{} {}".format(all[0], all[1]))
# print("-" * 16)
# for all in data:
#     print("{:>14}|{:1}".format(all[0], all[1]))


# from copy import deepcopy
# planets = ['Mercury', 'Venus', 'Earth', 'Mars',
# 'Jupiter', 'Saturn']
# print(planets[:3]) #selects first three elements
# print(planets[1:3]) #selects first 3 and selects first 1 from that 3
# planets[1::3] = ["senthur", "selva"] #to print inbetween mercury and venus, mars and jupiter
# print(planets)
# galaxy = planets[:] #copy of list
# print(galaxy.append("heybro")) #adds an element to end of list
# print(galaxy)
# univ = deepcopy(galaxy) 
# print(univ)
# print(":".join(univ))  #to join list with variables   
# print(planets)
# print(type(planets))
# print(planets[0])
# print(planets[:1])
# print(planets[1:])
# print(planets[:2])
# print(planets[1:3])
# print(planets[3:5])
# print(planets.append(7))
# print(planets)
# planets.extend(["hello"])
# print(planets)
# planets.insert(0,"INDIA")
# print(planets)
# planets.remove("Mercury")
# print(planets)
# planets.pop(3)
# print(planets)
# planets.reverse()
# print(planets)
# print(planets[::3])


# # exercise for list of people
# people = ["santhana", "senthur", "selvan", "pavi", "dhaswin"]
# user_input = input("Enter name to add to list:\n")
# added_list = people.append(user_input)
# while True:
#     user_inp = input("Enter type of application: n | x | s ")
#     if user_inp == "n":
#         remove = people.remove("santhana")
#         print(people)
#     elif user_inp == "s":
#         print(f"current number of users in list: {len(people)}")
#     elif user_inp == "x":
#         remove1 = people.remove("santhana")
#         print(f"{remove1} left from queue")
#     else:
#         print("valid option")



# animals = ['chicken', 'cow', 'snail', 'elephant']
# animals.sort()
# print(animals)
# animals.sort(reverse = True)                                                              # sorts in reverse order
# print(animals)
# animals.sort(key= len, reverse= False)                                                    # sorts by comparing length of string 
# print(animals)



# # TUPLES
# from operator import itemgetter
# students = [
#     ('senthur', 'A',24),
#     ('selva', 'A', 2),
#     ('santhana', 'B', 1)
# ]
# students.sort()
# print(students)
# sorte = sorted(students, key=itemgetter(2))                                              # sort by the third element of each tuple , means, it sorts based on 1, 2, 24 in our case
# print(sorte)


# # sorted characters
# string = "sdlfkdbvasldkd"
# sort = sorted(string)
# jo = "".join(sort)                                                                        # joins list of element into single element
# count = string.count('d')                                                                 # counts number of repetition of 'd'
# print(jo)
# print(count)


# # EXERCISE
# colors = ['blue', 'yellow', 'black', 'purple']
# for all in range(len(colors)):                                    
#     print(f"{all + 1 }. {colors[all]}")                                        
# select = input("enter ")
# if not select.isdecimal():                                                     
#         exit(f"number must be between 1 and {len(colors)}")
# if int(select) < 1 or int(select)  > len(colors):
#         exit("invalid")
# col = int(select) - 1
# print(colors[col])