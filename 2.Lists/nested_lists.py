nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# accessing items

print(nested_list[0])  # [1, 2, 3]
print(nested_list[-1])  # [7, 8, 9]
print(nested_list[1][1])  # 5


# looping through a nested list

for i in nested_list:
    for j in i:
        print(j)

# nested list comprehensions

print([[num for num in range(1, 4)]
       for val in range(3)])  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

print([['X' if x % 2 == 0 else 'O' for x in range(3)] for val in range(3)])
# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

print([[a, b, c] for a in range(1, 4)
       for b in range(1, 4) for c in range(1, 4)])
