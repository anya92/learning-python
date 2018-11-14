# Inheritance - a process of using details from a new class without modifying existing class


class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}."

    def make_sound(self, sound):
        print(f"This animal says {sound}.")


class Dog(Animal):

    def __init__(self, name, species, breed):
        # self.name = name
        # self.species = species
        # Animal.__init__(self, name, species)
        super().__init__(name, species="Dog")
        self.breed = breed


buddy = Dog("Buddy", "Dog", "Pug")

print(buddy)  # 'Buddy is a Dog.'
buddy.make_sound("woof")  # 'This animal says woof.'

print(isinstance(buddy, Dog))  # True
print(isinstance(buddy, Animal))  # True

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
