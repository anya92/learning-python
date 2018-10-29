# clear - removes all the elements from the dictionary

user = {'name': 'user1234', 'email': 'user@email.com'}
print(user)  # {'name': 'user1234', 'email': 'user@email.com'}
user.clear()
print(user)  # {}

# copy - makes a copy of a dictionary

a = {'b': 0, 'c': 1}
b = a.copy()

print(b)  # {'b': 0, 'c': 1}
print(b == a)  # True
print(b is a)  # False

# fromkeys - returns a dictionary with the specified keys and values

print({}.fromkeys("a", "b"))  # {'a': 'b'}
print(dict.fromkeys(["email"], None))  # {'email': None}

new_user = {}.fromkeys(["name", "email", "city", "image"], 'unknown')

print(new_user)
# {'name': 'unknown', 'email': 'unknown', 'city': 'unknown', 'image': 'unknown'}

# get - returns the value of the specified key

print(new_user["name"])  # 'unknown
print(new_user.get('name'))  # 'unknown

# print(new_user["phone"]) # KeyError
print(new_user.get('phone'))  # None

# pop - removes the element with the specified key

print(new_user.pop('image'))  # 'unknown'
print(new_user)  # {'name': 'unknown', 'email': 'unknown', 'city': 'unknown'}

# popitem - removes the last inserted key-value pair

print(new_user.popitem())  # ('city', 'unknown')
print(new_user)  # {'name': 'unknown', 'email': 'unknown'}

# update - updates the dictionary with the specified key-value pairs

new_user_2 = {'id': 1, 'name': 'Ben'}
new_user_2.update(new_user)
print(new_user_2)  # {'id': 1, 'name': 'unknown', 'email': 'unknown'}
