# # right aligned pyramid
# # for i in range(10):
# #   x = "*"
# #   x = i * x
# #   print(f"{x:<10}")

# # # left aligned pyramid
# # for j in range (10):
# #   x = "$"
# #   u = j * x
# #   print(f"{u:<10}")

# # for l in range (10):
# #   x = "@"
# #   x = l * x
# #   print(f"{x: ^30}")

# # for k in range(10):
# #   x = "%"
# #   x = x*(10-k)
# #   print(f"{x : ^30}")


# for i in range(20):
#   z = ("*" * i) + str("*")
#   x = "%" * i
#   y = "%" * i
#   print(f'{z:^20} {y: >20} {x:<50}')
# # for i in range(10):
# #     x = "*" * i
# #     y = "$" * i
# #     z = "@" * i
# #     w = "%" * (10 - i)
# #     print(f"{x:<10} {y:<10} {z:^30} {w:^30}")

# import copy
# numbers = [21, 45, 5, 87, 112, 65, 976]
users = ['dave','senthur']

# print('dave' in users)
# print(users[0])
# print(users[-1])
# print(numbers[1:5])
# users.append('selva')
# print(users)
# users.insert(0, 'santhanam')
# print(users)
# users.pop(0)
# print(users)
# index = users.index('dave')
# print(index)
# rever = numbers[::-1]
# print(rever)
# numbers.sort()
# print(numbers)


# from functools import reduce

# numbers1 = [2,43,67,112,8,343]

# def add(x,y):
#   return x + y

# sum = reduce(add, numbers)
# print(sum)

# numbers.extend(numbers1)
# print(numbers)
# import copy

# list1 = [[23, 45, 45, 34], [23, 45, 2, 78, 12]]
# copied_list = copy.deepcopy(list1)
# copied_list[0][1] = 20
# print(copied_list)

# conc = "         ***poda dai**".join(users)
# print(conc)
# user1 = len(users)
# print(user1)


# print(sorted(users, reverse = True))

