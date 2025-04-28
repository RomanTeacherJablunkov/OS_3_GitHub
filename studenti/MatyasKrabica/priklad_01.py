#Zadání
#Vytvořit třídu zdravic, která má metodu pozdrav()
#vytvořit třídu SlovakZdravic, CzechZdravic která dědi z Zdravice a přetěžuje metodu pozdrav().

#SK : Ahoj svet!
#CZ: Ahoj světe!


class Zdravic:
    pozdrav = "Pozdrav"
    def pozdrav(self):
        raise NotImplementedError("Tuto metodu musí implementovat do podtřídy")
    
class SlovakZdravic(Zdravic):
    def pozdrav(self):
        print("Ahoj svet!")
class CzechZdravic(Zdravic):
    def pozdrav(self):
        print("Ahoj světe!")

class AnglickyZdravic(Zdravic):
     def pozdrav(self):
          print("Hello World!")

def privitaj(zdravic_object):
        zdravic_object.pozdrav()

slovak = SlovakZdravic()
cech = CzechZdravic()
anglicky = AnglickyZdravic()
for z in (slovak, cech, anglicky):
    privitaj(z)