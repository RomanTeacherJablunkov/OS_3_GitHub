class Animal:  # Třída Animal
    def __init__(self, name):  # Konstruktor
        self.name = name

    # Vrací zvuk
    def make_sound(self):
        return "Some generic animal sound"


class Dog(Animal):  # Třída, která dědí z Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Volá konstruktor třídy Animal
        self.breed = breed  # Ukládá rasu psa
    #Metoda pro zvuk
    def make_sound(self): 
        return "Woof!"  # Vrací zvuk psa


class Cat(Animal):  # Třída, která dědí z Animal
    def __init__(self, name):
        super().__init__(name)  # Volá konstruktor třídy Animal
    #Metoda pro zvuk
    def make_sound(self): 
        return "Meow!"  # Vrací zvuk kočky


my_dog = Dog("Buddy", "Golden Retriever")  # Vytvoření instance psa
my_cat = Cat("Whiskers")  # Vytvoření instance kočky

print(my_dog.make_sound())  # Výpis zvuku psa
print(my_cat.make_sound())  # Výpis zvuku kočky
