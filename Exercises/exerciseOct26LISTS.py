# # Dice simulator game
# import random
# while True:
#   user_input = int(input("enter:  "))
#   if user_input == 1:
#     rand = int(random.randrange(1,6))
#     print(rand)
#   else:
#     break


# # random passwrod generator
# import random
# user_input = int(input("enter length:  "))
# lett = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
# res = "".join(random.sample(lett, user_input))                                                        # join is used to combine all letters
# print(res)

# # number guessing
# import random
# random_number = random.randint(0,3)
# for all in range(0,20):
#    user_input = int (input ("Guess number :  "))
#    result = "WIN!!" if user_input == random_number else "LOST"  "\nenter valid input" if user_input > random_number else ""
#    print(f"random number is {random_number} and result {result}")


# # palindrome
# while True:
#    user_input = input("enter:  ")
#    palindrome_letter = user_input[::-1]
#    print(palindrome_letter) 
#    if user_input == user_input[::-1]:
#       print("its a palindrome")
#       break
#    else:
#       print("try again")
#       continue


# # speedtest
# import speedtest
# st = speedtest.Speedtest()
# input_user = int (input("enter option: "))
# if input_user == 1:
#     print(st.download())
# elif input_user == 2:
#     print(st.upload())
# elif input_user == 3:
#     server_name = []
#     st.get_servers(server_name)
#     print(st.results.ping)
# else:
#     print("invalid")

# lines = [
#  'grape banana mango',
#  'nut orange peach',
#  'apple nut banana apple mango',
# ]
# one_list = "".join(lines)                                                                                 
# print(one_list)
# fruits = one_list.split()                                                      # it splits each elements inside list
# print(fruits)
# unique = []                                                                    # empty list to store items not in lines
# for all_fruits in fruits:
#     if all_fruits not in unique:
#         unique.append(all_fruits)                                              # here we appending fruits that are not in unique
#         print(sorted(unique))


# dna = 'ACCGXXCXXGTTACTGGGCXTTGT'                                       
# sequence = dna.split('X')                                                        # it splits whenever 'X' is there i.e.ACCGX, X, CX, X etc
# sequence.sort(key=len, reverse=True)                                             # sorts the list based on len
# print(sequence)
# newseq = []                                                                       
# for all in sequence:
#     if len(all) > 0:
#         newseq.append(all)
# print(sequence)
# print(newseq)

## IGNORE
# lines = [
#  'abc def ghi',
#  'hello world',]
# deep = lines[0][8].split()
# print(deep)
# empty = []
# for all in lines:
#     empty.extend(all.split())
#     print(empty)



# # Open and Read file
# import os                                                                      # to intereact with OS
# script_folder = os.path.dirname(os.path.abspath(__file__))                     # finds folder of file
# found = os.path.join(script_folder, "sample.txt")                              # finds file inside the script folder
# print(found)          
# with open (found, "r") as file:                                               # reads the file "r"
#     ans  = file.read()                                              
#     print(ans)


# import sys
# import os
# script_DIR = os.path.dirname(os.path.abspath(__file__))
# found_file = os.path.join(script_DIR, "sample.txt")
# def main(file_path):
#     with open(file_path, "r") as file:
#         lines = file.readlines()                                                # read lines and display as list
#         strip = [s.strip("\n") for s in lines]                                  # converts list to string
#         print(strip)
#         print(len(lines))
#         for all in lines:
#             print(all, end="")
# if __name__ == "__main__":
#     main(found_file)


# # password generator
# import random
# user = int(input("enter:"))
# random_number = "abclasdifjabasld892374*%%#$%*"
# result = "-".join(random.sample(random_number,user))
# print(result)


# import os
# directory = os.path.dirname(os.path.abspath(__file__))
# found = os.path.join(directory, "sample.txt")
# try:
#     with open (found, "r") as file:
#         fon = file.read()
#         print(fon)
# except Exception as err:
#     print("therer is san error")
#     print(err)
#     print(type(err), __name__)
# print("still running")