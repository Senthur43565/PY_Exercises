# # changing order inside dictionar or list
# from collections import OrderedDict
# d = OrderedDict()
# d['name'] = 'selva'
# d['age'] = '27'
# d['gender'] = 'male'
# print(d)
# d.move_to_end('name')
# print(d)

# # count number of char:
# text = """
#  This is a very long text.
#  OK, maybe it is not that long after all.
#  """
# empty_list = {}
# for all_char in text:
#     if text.isalnum:
#      if all_char == '\n':
#       continue
#     if all_char not in empty_list:
#             empty_list[all_char] = 1
#     else:
#             empty_list[all_char] +=1
# print(empty_list)
# for all_key in sorted(empty_list.keys()):
#    print("{}-{}".format(all_key, empty_list[all_key]))


# text = """
#  This is a very long text.
#  OK, maybe it is not that long after all.
#  """
# char_count = {}
# for char in text:
#     if char.isalnum():  # This will exclude spaces and special characters
#         if char in char_count:
#             char_count[char] += 1 #char_count[T] = char_count[T] + 1
#         else:
#             char_count[char] = 1

# # Filter characters that are repeated more than once
# repeated_chars = {char: count for char, count in char_count.items() if count > 1}

# print(repeated_chars)


# #  COUNT WORDS IN LIST:

# words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula',
# 'Sloth', 'Rhino', 'Sloth']
# empty_list = {}
# for all_words in words:
#     if all_words in empty_list:
#         empty_list[all_words] += 1
#     else:
#         empty_list[all_words] = 1
# for all in  empty_list:
#     print("{}--{}".format(all, empty_list[all]))


# # DEFAULT DICT
# from collections import defaultdict
# counter = defaultdict(int)
# word = 'eggplant'
# # if word not in counter:
# #     counter[word] = 0
# counter[word] += 1
# print(counter)



# # SETS 
# # Set Creation:-  Imagine a collectiom of dict marbles and iceCream. we cannot add the same type of items into dict, means, if red marble already in dict we cannot dd another red.
# marbles = {'red', 'green', 'blue', 'yellow', 'green'}
# iceCream = {'strawberry', 'mango', 'chocolate'}
# marbles.update(iceCream)
# print(marbles)


# # SET Operation:-  
# toys = {'van', 'jeep','cycle', 'car'}
# toys2 = {'van', 'car', 'lorry'}
# both_toys = toys.union(toys2)                                          # combines all toys together and removes duplicate as default
# print(both_toys)
# common_toys = toys.intersection(toys2)                                 # finds the toys both dict have
# print(common_toys)
# different_toy = toys.difference(toys2)                                 # finds differece in first list compared to second list 
# print(different_toy)
# unique_toy = toys.symmetric_difference(toys2)                          # displays items that are not repeated
# print(unique_toy)
# toys2.update(toys)                                                     # .update adds multiple items or another dictset into current dictset
# toys2.add('bus')                                                       # .add both adds single item to dictset
# print(toys2)




# # Checking for Membership: checking whether inserted item found in Dict

# fruits = {'apple', 'banana', 'orange'}
# checking_fruit = 'apple' in fruits
# print(checking_fruit)

# # Set comprehension: we want a box of even number in range 1 to 10

# even_numbers = {x for  x in range(1,11) if x % 2 == 0 }
# print(even_numbers)


# # FUNCTIONS

# PARAMETER OPERATIONS

# def main(x, y, z):
#     print("{}{}{}".format(x,y,z))
# main(
# # named-parameters
#     x = 'selva',                                                            # if we passing parameters as named, variable name should be same. 
#     y = 'A',
#     z = 2
# )

# def main(a, b=2, c=5):                                                        # parameters with default must come at the end, not at beginning
#     print("{}-{}-{}-".format(a, b, c))
# main(1, 5, 0)

# def main(*numbers):                                                          # * asterick will return value as TUPLE and it accepts any number of parameters also called arbitrary arguments
#     print(numbers)
#     total = 0
#     for s in numbers:
#         total += s
#     return total
# print(main(1, 2, 3))

# def main(**kw):                                                               # ** returns values as DICTIONARY
#     print(kw)
# main(a = 2, b = 8)
# def main(name, **kw):
#     print("{}-{}".format(name, kw))
# main(name = 'selva', a = 2, b = 6)


# #  ALL PARAMETER OPERATIONS in single function
# def main(a , b=6, *things, **numbers):
#     print("{}-{}-{}-{}".format(a, b, things, numbers))
# main(a=2, b=12, things=(4, 5), numbers={'a': 23})

def f(name):
 """
 The documentation
 should have more than one lines.
 """
 print(name)


f("hello")
print(f.__doc__)






# # SENDING EMAIL using smtplib
# import smtplib
# from email.message import EmailMessage

# def send_email(to, subject, content, sender_email, sender_password):
#     # Create an EmailMessage object
#     message = EmailMessage()
#     message.set_content(content)
#     message['Subject'] = subject
#     message['From'] = sender_email
#     message['To'] = to

#     # Connect to the SMTP server and send the email
#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.login(sender_email, sender_password)
#         server.send_message(message)

# # Call the send_email function with the email details
# send_email(
#     to='szabgab@gmail.com',
#     subject='self message',
#     content='Has some content too',
#     sender_email='gabor@szabgab.com',
#     sender_password='your_password'
# )







