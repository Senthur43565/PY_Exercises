# line01="*************"
# line02="*           *"
# line03="*  WELCOME! *"
# print('')
# print('')
# print(line01)
# print(line02)
# print(line03)
# print(line02)
# print(line01)


import math
number = 42
print("")
print('got it!') if number != 42 else print('not today')


# if number!=42:
#   print('got it')
# else:
#   print('not today')


# first="senthur"
# second="selva"
# print(type(first)==str)
# print(isinstance(first,str))


# dosa=str("onion")
# print(type(dosa))
# print(type(dosa)==str)
# print(isinstance(dosa,str))

# fullname=first+second
# print(fullname)
# fullname+="  GENIUS!"
# print(fullname)


# casting a number to string
# DOB=str(1995)
# DOb=1995
# print(type(DOB))
# print(type(DOb))
# print(isinstance(DOB,int))
# print(DOB)


# string methods
first = 'Senthur'
second = 'selva'
print(first)
print(first.lower())
print(first.upper())
print(len(first))
first += "                     "
first = "                " + first
print(len(first))
print(first)
print(len(first.rstrip()))

name = 'senthurSelva'.upper()
print(name.center(30, '*'))
print("idle".ljust(15, '-') + 'Rs.5'.center(5)+'1 qty'.rjust(8, '-'))


# string index values
print(name[2])
print(name[-2])
print(name[1:-1])
print(type(name) == str)
print(name.startswith("s"))


avg1 = 78.1
avg = float(90.6)
print(type(avg))
print(isinstance(avg, float))
print(avg1)


# built-in datatype

print(round(avg, 1))

print(math.pi)
print(math.sqrt(60.4))
print(math.ceil(avg))
print(math.floor(avg))


# casting string ro a number
zipcode = '641029'
zip = int(zipcode)
print(type(zip))
