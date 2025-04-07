class Animal:#Třída Animal
    def __init__(self, name):#Konstruktor
        self.name = name
    #Vrácí zvuk
    def make_sound(self):
        return "Some generic animal sound"

class Dog(Animal):#Třída Dog děděná z Animal
    def __init__(self, name, breed):
        super().__init__(self, name)#Volá konstruktor třídy Animal
        self.breed = breed #Ukládá rása psa

    def make_sound(self):
        return "Woof!" #Vrácí zvuk psa

class Cat(Animal):#Třída Cat děděná z Animal
    def __init__(self, name):
        super().__init__(name)#Volá konstruktor třídy Animal
    def make_sound():
        return "Meow!"#Vrácí zvuk kočky

my_dog = Dog("Buddy", "Golden Retriever")#Vytvoření instance psa
my_cat = Cat("Whiskers")#Vytvoření instance psa

print(my_dog.make_sound())#Vypíše zvuk psa
print(my_cat.make_sound())#Vypíše zvuk kočky