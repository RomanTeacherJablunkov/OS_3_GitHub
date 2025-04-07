class Vehicle: #Třída Vehicle
    def __init__(self, speed): #Konstruktor s atributama jako je speed
        self.speed = speed
    #Metoda vrací maximalní rychlost
    def max_speed(self):
        return self.speed
#Třída Car co dědí od Vehicle
class Car(Vehicle): 
    def __init__(self, speed):
        super().__init__(speed) #Volá konstruktor třídy Vehicle
    def max_speed(self): #Vypisuje maximalní rychlhost z instance resp. z Vehicle
        return f"Car max speed: {self.speed} km/h" #Vraci hodnotu
#Třída pro kolo co dědí z Vehicle
class Bike(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)#Vola konstruktor třídy Vehicle
    def max_speed(self): #Vraci max speed kola
        return f"Bike max speed: {self.speed} km/h"
#Instance pro Car max. speed 180
car = Car(180)
bike = Bike(60) #Instance pro Bike max. speed 60
#Vypiše max speed
print(car.max_speed())
print(bike.max_speed())