users = ['senthur', 'selva', 'santa']
data = ['senthur', '25']

# to find whether "name" in list or not
print("selva" in users[0])

# to select particular "name"
print(users[0])

# to find position of "name" in List
print(users.index("selva"))

print(users[1:])


print(users.append("hello"))

users.extend(data)

users.insert(0, 'bobby')

users.remove('bobby')

data.clear()
print(data)


users.sort()
print(users)

nums = [34, 4, 3, 2, 78]
nums.sort(reverse=True)

print(nums)
