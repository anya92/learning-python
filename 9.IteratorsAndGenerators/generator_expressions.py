def nums():
    for num in range(1, 10):
        yield num


g = nums()
print(g)  # <generator object nums at 0x00238F70>

g = (num for num in range(1, 10))  # generator expression
print(g)  # <generator object <genexpr> at 0x00418F70>
