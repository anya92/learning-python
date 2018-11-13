# Inheritance - a process of using details from a new class without modifying existing class


class Animal:

    def make_sound(self, sound):
        print(f"This animal says {sound}.")


class Dog(Animal):
    pass


buddy = Dog()

buddy.make_sound("woof")  # This animal says woof.

print(isinstance(buddy, Dog))  # True
print(isinstance(buddy, Animal))  # True

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
