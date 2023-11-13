# name = "senthur"
# print(type(name))
# print("I\'m so happy to be learning how to code in python")


# # multiline strings
# multiLine = """
# hello 
# all 
# how
# are
#  you
#  !
# """
# print(multiLine)


# # use of f-string
# name = ""
# age = ""
# gender = ""
# sillystory = f"""
# Hi,
# my name is {name},
# am {age} years old,
# {gender}
# """
# print(sillystory)

# # cake
# cake = f"""
#     (@) 
#    ( @ )    
#   (  @  )    
#  (   @   )    
#    ( @ )    
#    ( @ )    
# """

# for char in cake:
#     if char == " ":
#         print(" ", end="")
#     elif char == "@":
#         print("@", end="")
#     else:
#         print("\n", end="")



# senthur = {
#     "dress_color": "black",
#     "shoe_color" : "white",
#     "belt_color" : "grey"
# }

# selva = {
#     "dress_": "red",
#     "shoe_" : "green",
#     "belt_" : "blue"
# }

# merged = {}
# merged.update(senthur)
# merged.update(selva)
# print(merged)

# persons = senthur.copy()
# persons.update(selva)
# print(persons)


# # it says 2 power 10
# num = 2**10
# print(num)


# Lab experment
# beakers = 20
# tubes = 30
# rubber_gloves = 10
# safety_glasses = 4

# no_of_frinends = 3

# enough_safety_glasses = no_of_frinends*1 >= 3
# enough_tubes = no_of_frinends*10 >= 30
# enough_gloves = no_of_frinends*2 >= 6
# enough_beakers = no_of_frinends*6 >=18

# gloves_glasses = enough_safety_glasses and enough_gloves
# tubes_beakers = enough_tubes or enough_beakers
# gloves_glassesORgloves_glasses = enough_safety_glasses and enough_gloves or enough_tubes or enough_beakers
# all = enough_gloves and enough_beakers and enough_safety_glasses and enough_tubes

# final = f"""

# Each girl has enough safety glasses: {enough_safety_glasses}
# Each girl has enough rubber gloves: {enough_gloves}
# Each girl has enough tubes: {enough_tubes}
# Each girl has enough beakers: {enough_beakers}
# -
# There are enough gloves and safety glasses for each girl: {gloves_glasses}
# There are enough tubes and or enough beakers for each girl: {tubes_beakers}
# Each girl has enough safety glasses and beakers or enough tubes and beakers: {gloves_glassesORgloves_glasses}
# Each girl has enough gloves, safety glasses, tubes, and beakers: {all}

# '''
# """
# print(final)




# name = "Hello"
# print(len(name))


# def empty_string():
#   print("Empty string")


# name = "senthur"
# empty = ""
# food = "pizza"


# i = int(input("Enter number:\n"))

# if len(food) == 0:
#   empty_string()
# elif i < len(food):
#   print(food[i])
# else:
#   print("Invalid")

# strings = {
# "string1" : "HelloWorld",
# "string2" : 'WOWWOWWWW',
# "string3" : ""
# }
# user_input = input("Enter your word to reverse : \n")
# i = 1
# def user_reverse(user):
#   if len(user_input) == 0:
#    print("Emppty string")
#   elif len(user_input) >= 1:
#    user_reversed = user_input[::-1]
#    print(f"Your reversed string : {user_reversed}")
# user_reverse(user_input)


# if len(strings) == 0:
#   print("Empty string")
# elif len(strings) >i:
#   reversed_string = strings["string1"][::-1]
#   reversed_string1 = strings["string2"][::-1]
#   print(f"Reversed string1 :{reversed_string}  \nReversed string2 : {reversed_string1} ")


# reversed_word = strings[::-1]
# print(reversed_word)


# string = "hello"
# if len(string) < 3:
#   print("empty")
# else:
#   new_string = string[:1] + string[len(string)-3:]
#   print(new_string)


# objects = {
# 'obj1' : "hello",
# 'obj2' : 34324,
# 'obj3' : "hee345",
# 'obj4' : ""
# }
# condi = {}
# for key in objects:
#   condi[key]  = str(objects[key]).isdecimal()
# print(condi)


# calculate numeric fuctions in lists
# numbers = [10, 5, 8, 24, 2, 11, 15, 7, 12]

# total_sum = sum(numbers)
# print(f"sum of numbers in list: {total_sum}")

# max_num = max(numbers)
# print(f"Max number in list : {max_num}")

# min_num = min(numbers)
# print(f"minimum number in list : {min_num}")

# average = sum(numbers)/ len(numbers)
# print(f'Averaage : {average}')

# user_input = int(input("Enter the number: \n"))

# if user_input == numbers:
#   print(f"{user_input} found in list")
# else:
#   print(f"{user_input} not found....")




# Books shelf

books = {
  'book1':{'author':'james','year':'1965'},
  'book2':{'author':'bonf','year':'1878'},
  'book3':{'author':'camerronsteve','year':'1987'},
  'book4':{'author':'alfred','year':'1834'}
}

specific_author = "book2"
if specific_author in books:
  print("found")
else:
  print("not found")

test_specific = "booky"
if test_specific in books:
  print(f"{test_specific}  found in store")
else:
  print(f'{test_specific} not found')

earlisest = min(books, keys=lambda book: books[book]["year"])
print(earlisest)
