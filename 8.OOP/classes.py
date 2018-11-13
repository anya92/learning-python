# Object Oriented Programming - solving a programming problems by creating objects

# a class - a blueprint for the object
# an object - an instantiation of a class

# methods - functions defined inside the body of a class


class Person:  # creating a class
    count = 0  # class attribute

    @classmethod
    def how_many_people(cls):
        return f"There are {cls.count} people."

    @classmethod
    def from_string(cls, data_string):
        first, last, age = data_string.split(',')
        return cls(first, last, int(age))

    # __init__() - a function which is always executed when the class is being initiated
    # parameter self - a reference to the class itself

    def __init__(self, first, last, age):
        # print("A new user has been created.")
        self.first = first
        self.last = last
        self.age = age
        Person.count += 1

    def __repr__(self):
        return f"{self.first} {self.last}, {self.age}"

    def full_name(self):  # instance method
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def birthday(self):
        self.age += 1  # modifying properties


print(Person.count)  # 0

person1 = Person('Jerry', 'Gergich', 70)  # creating an object
person2 = Person('Tom', 'Haverford', 33)

print(Person.count)  # 2

print(type(person1))  # <class '__main__.Person'>

print(person2.first, person2.last, person2.age)  # 'Tom Haverford 33'

print(person1.full_name())  # 'Jerry Gergich'
print(person2.initials())  # 'T.H.'

person2.birthday()
print(person2.age)  # 34

print(Person.how_many_people())  # 'There are 2 people.'

person3 = Person.from_string("Ron,Swanson,56")
print(person3.full_name())  # Ron Swanson

print(person3)  # Ron Swanson, 56
