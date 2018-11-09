
class Person:  # creating a class
    count = 0  # class attribute

    @classmethod
    def how_many_people(cls):
        return f"There are {cls.count} people."

    # __init__() - a function which is always executed when the class is being initiated
    # parameter self - a reference to the class itself

    def __init__(self, first, last, age):
        # print("A new user has been created.")
        self.first = first
        self.last = last
        self.age = age
        Person.count += 1

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
