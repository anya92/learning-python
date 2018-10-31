# Set comprehension

s = {x ** 2 for x in range(10)}
print(s)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

c = {char.upper() for char in 'hello world' if char.isalpha()}
print(c)  # {'R', 'O', 'H', 'L', 'E', 'D', 'W'}
