t = (3, 4, 1, 12, 5, 3, 1, 4, 1)

# count - returns the number of times a specified value occurs in a tuple

print(t.count(1))  # 3
print(t.count(0))  # 0

# index - searches the tuple for a specified value and returns the position of where it was found

print(t.index(1))  # 2
print(t.index(3, 2))  # 5
