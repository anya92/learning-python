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


# sorted - returns a sorted list from the given iterable

print(sorted(nums))  # [1, 2, 3, 4, 5]
print(sorted(nums, reverse=True))  # [5, 4, 3, 2, 1]

cars = [{"year": 2001, "make": "Lexus"}, {"year": 1997, "make": "Infiniti"}, {
    "year": 1987, "make": "Pontiac"}, {"year": 2000, "make": "GMC"}, {"year": 2012, "make": "Subaru"}]

print(sorted(cars, key=lambda car: car["make"]))
# [{'year': 2000, 'make': 'GMC'}, {'year': 1997, 'make': 'Infiniti'}, {'year': 2001, 'make': 'Lexus'}, {'year': 1987, 'make': 'Pontiac'}, {'year': 2012, 'make': 'Subaru'}]

print(sorted(cars, key=lambda car: car["year"], reverse=True))
# [{'year': 2012, 'make': 'Subaru'}, {'year': 2001, 'make': 'Lexus'}, {'year': 2000, 'make': 'GMC'}, {'year': 1997, 'make': 'Infiniti'}, {'year': 1987, 'make': 'Pontiac'}]

# max and min - return the largest and the smallest element in an iterable

print(max(nums))  # 5
print(min(nums))  # 1

print(max(cars, key=lambda car: car['year']))
# {'year': 2012, 'make': 'Subaru'}
print(min(len(car['make']) for car in cars))  # 3 (GMC)

# reversed - returns the reversed iterator of the given sequence

print(reversed('Python'))  # <reversed object at 0x004D0F70>

print('Python'[::-1])  # 'nohtyP' or
print(''.join(list(reversed('Python'))))

for char in reversed('Python'):
    print(char)  # 'n' 'o' 'h' 't' 'y' 'P'

# abs - returns the absolute value of the given number

print(abs(-10))  # 10
print(abs(10))  # 10

# sum - adds the items of an iterable and returns the sum

print(sum([4, 1, 6]))  # 11
print(sum((2, 5, 3)))  # 10
print(sum({4, 7, 3}))  # 14

# round - returns the floating point number rounded off to the given ndigits digits after the decimal point

print(round(3.1415))  # 3
print(round(3.1415, 2))  # 3.14

# zip - take iterables (can be zero or more), makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples

nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]

z = zip(nums1, nums2)
print(z)  # <zip object at 0x004C7210>

print(list(z))  # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(tuple(zip(nums1, nums2)))  # ((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))
print(dict(zip(nums1, nums2)))  # {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
