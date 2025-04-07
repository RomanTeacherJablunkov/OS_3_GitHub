class Vehicle: #Třída určující vozidlo
    def __init__(self, speed): #Def určující jeho rychlost
        self.speed = speed

    def max_speed(self):  #Metoda vracející maximální rychlost vozidla
        return self.speed

class Car(Vehicle): #Třída pro auto jako typu vozidla
    def max_speed(self): #Vrací maximální rychlost auta
        return f"Car max speed: {self.speed} km/h"

class Bike(Vehicle): #Třída pro motorku jako typu vozidla
    def max_speed(self): #Vrací maximální rychlost motorky
        return f"Bike max speed: {self.speed} km/h"

car = Car(180) #Nastavená rychlost auta
bike = Bike(60) #Nastavená rychlost motorky

print(car.max_speed()) #Vytisknutí textu pro aut
print(bike.max_speed()) #Vytisknutí textu pro motorku