f = open('lorem_ipsum.txt')

print(f)  # <_io.TextIOWrapper name='lorem_ipsum.txt' mode='r' encoding='cp1250'>

print(f.read())  # 'Lorem ipsum (...)'

print(f.read())  # ''
# Python reads files using a cursor
# After a file is read, the cursor is at the end

f.seek(0)  # moves cursor to the beginning
print(f.read())  # 'Lorem ipsum (...)'

f.seek(0)
print(f.readline())  # 'Lorem ipsum (...) aliqua.'

print(f.readline())  # 'Ut enim (...) consequat.'

print(f.readlines())
# ['Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n']

print(f.closed)  # False

f.close()

print(f.closed)  # True

# print(f.read())  # ValueError: I/O operation on closed file.


# with blocks

with open('lorem_ipsum.txt') as file:
    data = file.read()

print(file.closed)  # True

print(data)  # 'Lorem ipsum (...)'
