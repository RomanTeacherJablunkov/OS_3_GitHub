class Vehicle: #Vytvoření třídy Vehicle
    def __init__(self, speed): #Inicializace atribut / Konstruktok INIT
        self.speed = speed #Uložení atributy 'speed'
#Enter
def max_speed(self): #Metoda pro vrácení 'maximální rychlosti'
        return self.speed #Vrátí hodnotu maximální rychlost
#Enter
class Car(Vehicle): #Třída 'Car', která se dědí ze třídy 'Vehicle'
    def max_speed(self): #Metoda pro vrácení 'maximální rychlosti'
        return f"Car max speed: {self.speed} km/h" #Vrátí maximální rychlost třídy 'Car' v km/h
#Enter
class Bike(Vehicle): #Třída 'Bike' která se dědí ze třídy 'Vehicle'
    def max_speed(self): #Metoda pro vrácení 'maximální rychlosti'
        return f"Bike max speed: {self.speed} km/h" #Vrátí maximální rychlost třídy 'Bike' v km/h
#Enter
car = Car(180) #Definuje max. rychlost pro 'Car' pomocí instance
bike = Bike(60) #Definuje max. rychlost pro 'Bike' pomocí instance
#Enter
print(car.max_speed()) #Vytiskne maximální rychlost třídy 'Car'
print(bike.max_speed()) #Vytiskne maximální rychlost třídy 'Bike'