class Vehicle: #Třída pro vehicle
    def __init__(self, speed): #Konstruktor s atributami speed
        self.speed = speed
    #Vrácení max_speed
    def max_speed(self):
        return self.speed
#Třída car zděděná od Vehicle
class Car(Vehicle):
    def max_speed(self):#Volá konstruktor třídy Vehicle
        return f"Car max speed: {self.speed} km/h" #Vypisuje maximální rychlost auta
#Třída Bike zděděná od Vehicle
class Bike(Vehicle):
    def max_speed(self):#Volá konstruktor třídy Vehicle
        return f"Bike max speed: {self.speed} km/h"#Vypisuje maximální rychlost kola

car = Car(180)#Instance pro car max. speed 180
bike = Bike(60)#Instance pro bike max. speed 60

print(car.max_speed())#Vypíše max speed car
print(bike.max_speed())#Vypíše max speed bike