# Method Resolution Order -  the order in which base classes are searched when looking for a method (multiple inheritance)


class A:
    def who_am_I(self):
        print("I am an A")


class B(A):
    def who_am_I(self):
        print("I am a B")
        super().who_am_I()


class C(A):
    def who_am_I(self):
        print("I am a C")


class D(B, C):
    # def who_am_I(self):
    #     print("I am a D")  # 'I am a D'
    pass


d = D()

d.who_am_I()
# 'I am a B'
# 'I am a C'

b = B()
b.who_am_I()
# 'I am a B'
# 'I am an A'

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# help(D)
# class D(B, C)
#  |  Method resolution order:
#  |      D
#  |      B
#  |      C
#  |      A
#  |      builtins.object
#  |
