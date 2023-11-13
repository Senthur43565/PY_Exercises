# RECURSION  function calls itself twice until certain condition is met.
# def add_one(num):
#     if (num >= 9):
#         return num + 1
#     else:
#         total = num + 1
#         return add_one(total)
# result = add_one(1)
# print(result) 
 
# def hallo(hey):
#   if hey <= 20:
#     print(hey)
#     hallo(hey + 1)
# hallo(-1)




def towers_of_hanoi(n, x, y, z):
    if n == 1:
        print(f"Move disc 1 from {x} to {z}")
        return towers_of_hanoi(n - 1, x, z, y)
    print(f"Move disc {n} from {x} to {z}")
    towers_of_hanoi(n - 1, y, x, z)

# Example usage for 3 discs:
towers_of_hanoi(3, 'A', 'B', 'C')


# LAMBDA 

# CLOSURE

# GENERATOR