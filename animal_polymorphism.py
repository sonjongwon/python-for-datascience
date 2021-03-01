class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return "Meow!"


class Dog(Animal):
    def talk(self):
        return "Woof! Woof!"


animals = [Cat('Missy'),
           Cat('Mr.mistoffelees'),
           Dog('Lassie')]

for animal in animals:
    print(animal.name, ":", animal.talk())
