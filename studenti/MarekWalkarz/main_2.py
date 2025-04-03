class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return f"{self.name} Woof! {self.breed} "

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} Meow!"

my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers")
print(my_dog.make_sound())
print(my_cat.make_sound())