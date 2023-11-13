# # WIFI tracker
# import subprocess
# data = subprocess.check_output(
#     ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split("\n")                                       
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(
#         ['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
#     results = [b.split(':')[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print("{:<30} | {:<}".format(results[0]))
#     except IndexError:
#         print("{:<30} | {:<}".format(i, ""))

# # OPEN FILE EXCEPTION HANDLING
# import os 
# script = os.path.dirname(os.path.abspath(__file__))
# found = os.path.join(script, "sample.py")
# print(found)

# try:
#     with open (found, "r") as file:
#         res = file.read()
#         print(res)
# except ValueError as err:
#     print("invalid")
#     print(err)
#     print(type(err))



# # DICTIONARY
# user = {}
# user['name'] = "selva"                                                                      # append a key and value to dictionary
# user['age'] = '27'
# print(user)
# sub = user['name']                                                                          # displays value of selected key and stores it in variable "sub"
# print(sub)
# user1 = {
#  'fname': 'Foo',
#  'lname': 'Bar',
 
#  }
# user1.update(user)                                                                         # adds dict to another dict
# print(user1)
# print(user1.keys())
# for all in user1.keys():                                                                   # looping through dictionary
#     print(f"{all}    -         {user1[all]}")
# for all1 , uid in user1.items():                                                           # loop using .items
#     print("{}===>{}".format(all1, uid))

# for t in user1.items():
#     print(t)
#     print("{}{}". format(t[0], t[1]))
# print(user1.values())                                                                      # shows values of dictionary  
# print(user1)
# print(user1.get('email'))                                                                  # get() displays none if searched key not in dict

# for k in ["name", "email"]:
#     if k in user1:
#         print("{} ---> {}".format(k, user1[k]))                                            # find key or value in dict
#     else:
#         print("{} not found in dict".format(k))
# print("name" in user1)                                                                     # check key in dict
# print("selva" in user1.values())                                                           # check value in dict or not                
# del user1["name"]                                                                          # remove key from dict
# print(user1)
# pop = user1.pop("fname")                                                                   # .pop take out value or key and return it in pop
# print(pop)











# # LIST of DICTIONARY

# people = [
#     {
#     'name' : 'Foo Bar',
#     'email' : 'foo@example.com'
#     },
#     {
#     'name' : 'Qux Bar',
#     'email' : 'qux@example.com',
#     'address' : 'Borg, Country',
#     'children' : ['Alpha','Beta']
#     }
#  ]
# users = people[0]['name']                                                                  # can access dict inside a dict 
# child = people[1]['children'][0]
# print(child)
# pl = (1, 2)                                                                                # can use tuple as key in dict
# people[0][pl] = 'senthur'                                                                  # adds new key to dict1 inside people
# print(people)
# print(list(map(lambda p:p['name'], people)))                                               # lambda takes a particular key to be selected, map will find values inside key and list will put them together
# print(list)




# # SHARED DICTIONARY

# people = [{
#     "name" : "selva",
#     "section" : "sec-A"
# },
# {
#     "name" : "senthur",
#     "section" : "sec_B"
# }, 
# {
#     "name" : "santha",
#     "section" : "sec_C"
# },
# ]
# by_name = {}
# by_section = {}
# for all in people:
#     by_name[ all['name'] ] = all                                                            # shared list will arrange all items inside particular dict in a given empty_dict
#     by_section[all["section"]] = all
# print(by_name)
# print(by_section)
# print(by_name[0])



# # IMMUTABLE COLLECTION : TUPLE AS DICTIONARY KEYS

# dict1 = {}
# dict1['animal'] = ('lion', 'tiger')
# dict1['fruits'] = ('apple', 'orange')
# print(dict1)
# for all in dict1.keys():
#     print(all)
#     print(all.__class__)                                                         # all.__class__ is same as type(all)
#     print(dict1[all])



# # SORT DICTIONARY BY VALUE

# scores = {
#  'Foo' : 10,
#  'Bar' : 88,
#  'Miu' : 34,
#  }
# print(scores)
# sorted_score = sorted(scores)                                                      # by default keys will get sorted
# print(sorted_score)
# print(sorted(scores.values()))                                                     # sort the values, but we cannot get the keys back!
# sorted_names = sorted(scores, key=lambda a:scores[a])   
# for all in sorted_names:
#     print("{:<5}{}".format(all, scores[all]))



# # SORT DICTIONARY KEYS BY VALUES
# scores = {
#  "Jane" : 30,
#  "Joe" : 20,
#  "George" : 30,
#  "Hellena" : 90,
#  }
# for name in scores.keys():
#     print("{:<20}--{}".format(name, scores[name]))
# print("")
# for all in sorted(scores.keys()):
#     print("{:<15} - {}".format(all, scores[all]))
# lamb = sorted(scores, key=lambda a : scores[a])
# print(lamb)


# def color_of_items():
#     coloures_Tot = zip(colors, toys)
#     print(coloures_Tot)
#     for all in coloures_Tot:
#         OP_color = all[0] + all [1]
#         print(OP_color.split())
#     print(OP_color)  

# print("Welcoeme to colour choosing part of shopping")
# color_of_items()