# vytvoření třídy Vehicle
class Vehicle:
    # Konstruktor třídy, nastaví rychlost vozidla při vytvoření objektu
    def __init__(self, speed):
        self.speed = speed  # Atribut který ukládá maximální rychlost vozidla

    # Metoda pro získání rychlosti vozidla
    def max_speed(self):
        return self.speed  # Vrací hodnotu rychlosti

#Vytvoření třídy Car ktera je dědíčná z třídy Vehicle
class Car(Vehicle):
    # Přepisuje metodu max_speed, aby vrácela informaci pro auto
    def max_speed(self):
        return f"Car max speed: {self.speed} km/h"  # Vytiskne rychlost auta

# Vytvoření třída Bike která je dědíčná z třídy Vehicle
class Bike(Vehicle):
    # Přepisuje metodu max_speed, aby vrácela informaci pro kolo
    def max_speed(self):
        return f"Bike max speed: {self.speed} km/h"  # Vytiskne rychlost kola

# Vytvoření objektu car s rychlostí 180 km
car = Car(180)

# Vytvoření objektu bike s rychlostí 60 km
bike = Bike(60)

# Zavolání metody max_speed pro auto a výpiše výsledek
print(car.max_speed())  # Vytiskne: Car max speed: 180 km/h

# Zavolání metody max_speed pro kolo a výpiše výsledek
print(bike.max_speed())  # Vytiskne: Bike max speed: 60 km/h