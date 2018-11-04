# map - applies a function to all the items in an input list

nums = [1, 2, 3, 4, 5]

doubles = list(map(lambda x: x * 2, nums))

print(doubles)  # [2, 4, 6, 8, 10]

# filter - creates a list of elements for which a function returns true

odds = list(filter(lambda x: x % 2 != 0, nums))

print(odds)  # [1, 3, 5]

# map and filter combined

doubled_evens = list(map(lambda x: x * 2,
                         filter(lambda x: x % 2 == 0, nums)))

print(doubled_evens)  # [4, 8]

# using list comprehension

print([num * 2 for num in nums if num % 2 == 0])  # [4, 8]

# all - returns True when all elements in the given iterable are true

print(all([x % 2 == 0 for x in [2, 4, 6]]))  # True
print(all([x % 2 == 0 for x in [2, 4, 6, 7]]))  # False

print(all([1, True, 'a']))  # True
print(all([1, False, 'a']))  # False

# any - returns True if any element of an iterable is True

print(any([x % 2 == 0 for x in [1, 3, 6, 7]]))  # True
print(any([x % 2 == 0 for x in [1, 3, 5, 7]]))  # False

print(any([0, False, 'a']))  # True
print(any([0, False, '']))  # False

# with generator expressions - a high performance, memory efficient generalization of list comprehensions

names = ['Morgan', 'Michael', 'Matt', 'Mark']

print(all(name[0] == 'M' for name in names))  # True

# instead of list comprehension: print(all([name[0] == 'M' for name in names]))


# sorted
