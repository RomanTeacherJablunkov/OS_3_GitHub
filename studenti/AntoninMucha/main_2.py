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
        return "Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Meow!"

my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers")

print(my_dog.make_sound())
print(my_cat.make_sound())  


class Logger(object): #Single ton třída
    def __new__(cls, *args, **kwargs): #Metoda new, která zajistí že vždy bude existovat jen jedna instance teto třídy
        if not hasattr(cls, "_logger"):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger
        