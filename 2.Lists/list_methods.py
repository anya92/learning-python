data = [12, 5, 7]

# append - adds an item to the end of the list

data.append(21)
print(data)  # [12, 5, 7, 21]

# extend - adds the elements of the list to tthe end of the current list

data.extend([9, 24, 31])
print(data)  # [12, 5, 7, 21, 9, 24, 31]

# insert - adds an item at the specified position

data.insert(0, -1)
print(data)  # [-1, 12, 5, 7, 21, 9, 24, 31]

# clear - removes all the items of the list

data.clear()
print(data)  # []

# pop - removes the item at the specified position, returns removed value

data = [1, 2, 11, 1, 3, 4]

data.pop()  # if no index is specified, removes the last item (4)
data.pop(1)  # 2
print(data)  # [1, 11, 1, 3]

# remove - removes the item with the specified value

data.remove(1)
print(data)  # [11, 1, 3]

# index - returns the index of the first item with the specified value
# can specify start and end - index(value, start, end)

print(data.index(1))  # 1

print([5, 1, 3, 4, 3, 2, 5, 3].index(3, 3, 5))  # 4

# count - returns the number of items with the specified value

print([1, 5, 1, 3, 2].count(1))  # 2

# reverse - reverses the order of the list

data.reverse()
print(data)  # [3, 1, 11]

# sort - sorts the list

data.sort()
print(data)  # [1, 3, 11]

# join - a String method - returns a string in which the elements of list have been joined by str separator

print(', '.join(["Hello", "world"]))  # "Hello, world"

# slice - makes a new list using slices of the other list
# old_list[start:end:step]

# start
# [0:] == [:]
print([1, 2, 3, 4][:])  # [1, 2, 3, 4]

new_data = data[:]  # copy of the data list
new_data == data  # True
new_data is data  # False

print([1, 2, 3, 4][2:])  # [3, 4]
print([1, 2, 3, 4][-1:])  # [4]

# end
print([1, 2, 3, 4][:2])  # [1, 2]
print([1, 2, 3, 4][:-1])  # [1, 2, 3]

print([1, 2, 3, 4][1:3])  # [2, 3]

# step
print([1, 2, 3, 4, 5, 6, 7][0::2])  # [1, 3, 5, 7]
print([1, 2, 3, 4, 5, 6, 7][::-1])  # [7, 6, 5, 4, 3, 2, 1]
print([1, 2, 3, 4, 5, 6, 7][2::-1])  # [3, 2, 1]


# swapping values in lists

names = ['Bob', 'Tom', 'Jerry']
names[0], names[2] = names[2], names[0]

print(names)  # ['Jerry', 'Tom', 'Bob']
