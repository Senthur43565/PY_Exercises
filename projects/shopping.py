# # SHOPPING AVAILABLE COMBINATION OF ITEMS WITH COLORS
# import time
# import random
# import itertools                                                                                                                                    # USED TO FIND ALL AVAILABLE COMBINATION FROM LISTS

# colors = ["red", "blue", "pink"]
# toys = ["car", "ball", "doll"]

# random_colors = random.choice(colors)                                                                                                               # chooses random colors
# random_toys = random.choice(toys)                                                                                                                   # chooses random toys
# random_product = random_colors + "-" + random_toys                                                                                                  #combines random colot and toy

# print("Random color is: {}\nRandom toy is: {}\nRandom_product final: {}\n".format(random_colors, random_toys, random_product))                      

# user_choice = input("If the random product is not OK for you,\nPress 'O' to accept or press ENTER to choose your color: ").upper()  

# if user_choice == 'O':
#     print("Thank you for choosing our product. Stay in touch with us.")
# else:
#     print("Please hold on for 3 seconds.")
#     time.sleep(3)

# if user_choice != 'O':
#     user_input_colors = input("Enter the color you would like: ")
#     if user_input_colors in colors:
#         print(f"You chose: {user_input_colors}")
#     else:
#         print(f"Color '{user_input_colors}' not found in the available colors.")

#     user_input_toys = input("Enter the toy you would like: ")
#     if user_input_toys in toys:
#         print(f"You chose: {user_input_toys}")
#     else:
#         print(f"Toy '{user_input_toys}' not found in the available toys.")

#     final_user_product = user_input_colors + "-" + user_input_toys
#     print("You chose: {}".format(final_user_product))

# iterated_random = list(itertools.product(colors, toys))                                                                                           # iterates through colors and toys, print all posiible combinations of colors and toys
# available_combinations = ['-'.join(all_product) for all_product in iterated_random]                                                               # finds random combination from iterated random

# if final_user_product in available_combinations:
#     print("You chose: {}".format(final_user_product))
# else:
#     print("The combination you chose is not found in available combinations.")











import random
import itertools
user_name_list = []
user_one = input("Enter your name:  ")
user_name_list.append(user_one)
user_two = input("Enter your name:  ")
user_name_list.append(user_two)
user_three = input("Enter your name:  ")
user_name_list.append(user_three)
user_four = input("Enter your name:  ")
user_name_list.append(user_four)
user_five = input("Enter your name:  ")
user_name_list.append(user_five)
print(user_name_list)
colors = ['red', 'green', 'yellow', 'gold', 'black']
user_color_list = []


for user in user_name_list:
    random_colors = random.choice(colors)
    user_color_list.append((user, random_colors))
print(user_color_list)
zipped = zip(user_color_list)
for all in zipped:
    print(all)
