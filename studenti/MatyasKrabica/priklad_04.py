class Matematika:
    @staticmethod
    def soucet(a,b):
        print(f"Součet: {a + b}")
    @classmethod
    def info(cls):
        print(f"Toto je třída: {cls.__name__}")
#Voláni
Matematika.info()
Matematika.soucet(7,3)