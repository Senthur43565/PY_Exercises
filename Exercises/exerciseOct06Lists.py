# Create a list called fruits containing the following fruits: 'apple', 'banana', 'cherry', 'date', 'fig'.

# Check if 'banana' is in the list. Print whether it is or not.

# Select and print the third fruit in the list.

# Find the position of 'cherry' in the list and print it.

# Create a new list called more_fruits containing the following fruits: 'grape', 'kiwi', 'lemon'.

# Extend the fruits list by adding the fruits from the more_fruits list.

# Append 'orange' to the fruits list.

# Insert 'pear' at the beginning of the fruits list.

# Remove 'date' from the fruits list.

# Sort the fruits list in alphabetical order.

# Sort the fruits list in reverse alphabetical order.

# Print the final sorted fruits list.
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']

check = 'banana' in fruits
if check is True:
    print("Available")
else:
    print("not available")

select = fruits[2]
print(f"third fruit in list is {select}")

find = fruits.index('cherry')
print(f"position of cherry is  {find}")

more_fruits = ['grape', 'kiwi', 'lemon']

extend_list = fruits.extend(more_fruits)
print(f"Both lists linked together:  \n {fruits}\n")
print("")

append_orange = fruits.append("orange")
print(f"updated list : {fruits}")
print("")


insert_pear = fruits.insert(0, "pear")
print(f"updated list: {fruits}")
print("")


remove_date = fruits.remove("date")
print(f"date removed from list: {fruits}")
print("")

sort = fruits.sort()
print(f"sorted list : {fruits}")
print("")

reverse = fruits.reverse()
print(f"reversed order od list: {fruits}")
print("")

print(f"final sorder list: \n\n{fruits}")
