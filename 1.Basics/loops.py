# for loop

"""
for item in iterable_object:
  do sth with item
"""

# iterable_object - collection of items, e.g. a list of numbers, a string of characters, a range

for char in "hello":
  print(char)

for x in range(1, 10): # 1 - 9
  print(x ** 2)

range(10) # 0 - 9
range(2, 10, 2) # 2 4 6 8

# while loop

i = 1
while i < 6:
  print(i)
  i += 1

password = input("What's the secret password? ")

while password != 'orange':
  print("wrong")
  password = input("What's the secret password? ")
print("correct")

# the break statement

while True:
  message = input("Type exit to exit: ")
  if message == 'exit':
    break  # stop the loop even if the while condition is true

i = 0
while i < 11:
  i += 1
  if i % 2 == 0:
    continue  # stop the current iteration, and continue with the next
  print(i)
