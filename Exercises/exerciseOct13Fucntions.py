# differenve between parameters and arguments

# DEFAULT ARGUMENT technique
def sum(x, b):
    # (x, b) are the parameters that never change, they are like placeholders
    print(x + b)
sum(3, 8)
# (3,8) arguments are actual data, when def is called..can change as per our need
#  above code does not return any value, use of def is to return value and later we use it in our program..


# so if we need to return a value do the following code

def minus(a, b):
    return a+b
result = minus(5, 10)
# it returns the value from def and store it in the result
print(result)


def sum(x=1, y=0):
    # can also pass default values to parameters
    return x + y
output1 = sum()
print(output1)

# ARBITRARY ARGUMENT technique
def multiple_items(*args):
    # if we have unknown amount of arguments to be passed into the function, we can use (*anyname)
    # this will return parameters as Tuple..
    print(args)
    print(type(args))
multiple_items('senthur', 'selva', 'how', 'are')



def multi_named_items(**kwargs):
    # this will return parameters as Dictionaries..
    print(kwargs)
    print(type(kwargs))
multi_named_items(first='virat', second='kohli')


