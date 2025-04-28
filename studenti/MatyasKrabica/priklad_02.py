class Zamestnanec:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def info(self):
        print(f"Jméno: {self.jmeno}")

class Manazer(Zamestnanec):
    def __init__(self, jmeno, oddeleni):
        super().__init__(jmeno)     
        self.oddeleni = oddeleni
    def info(self):
        super().info()
        print(f"Řidí oddělení: {self.oddeleni}")

manazer = Manazer("Petr", "Vyvoj")
manazer.info()

