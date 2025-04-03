class Vehicle:                                          #Vytvoření třídy Vehicle pro dědění
    def __init__(self, speed):                          #Konstruktor třídy
        self.speed = speed                  

    def max_speed(self):                                #Metoda speed jenž se bude dědit
        return self.speed                               #Vráci hodnotu speed

class Car(Vehicle):                                     #Třída Auto, která dědí z třídy Vehicle
    def max_speed(self):                                #Metoda maximalní rychlosti
        return f"Car max speed: {self.speed} km/h"      

class Bike(Vehicle):                                    #Třída Bike, která dědí z třídy Vehicle
    def max_speed(self):                                #Metoda maximalní vrátí maximální rychlost automobiluychlosti
        return f"Bike max speed: {self.speed} km/h"     #Vrátí maximální rychlost automobilu

car = Car(180)                                          #Nastavení maximální rychlosti auta
bike = Bike(60)                                         #Nastavení maximální rychlosti kola

print(car.max_speed())                                  #Vypíše hodnotu přiřazenoou pro Car
print(bike.max_speed())                                 #Vypíše hodnotu přiřazenoou pro Bike