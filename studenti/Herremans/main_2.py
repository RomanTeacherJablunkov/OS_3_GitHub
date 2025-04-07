class Uver:
    def __init__(self, castka, rocni_urokova_sazba, doba_splaceni_mesice):
        self.castka = castka
        self.rocni_urokova_sazba = rocni_urokova_sazba
        self.doba_splaceni_mesice = doba_splaceni_mesice

    def mesicni_splatka(self):
        mesicni_urokova_sazba = self.rocni_urokova_sazba / 100 / 12
        return (self.castka * mesicni_urokova_sazba * (1 + mesicni_urokova_sazba) ** self.doba_splaceni_mesice) / ((1 + mesicni_urokova_sazba) ** self.doba_splaceni_mesice - 1)

    def celkova_zaplacena_castka(self):
        return self.mesicni_splatka() * self.doba_splaceni_mesice

    def celkove_uroky(self):
        return self.celkova_zaplacena_castka() - self.castka


class KalkulackaUveru:
    def __init__(self):
        self.uver = None

    def ziskej_vstup(self):
        castka = float(input("Zadejte výši úvěru (v Kč): "))
        rocni_urokova_sazba = float(input("Zadejte roční úrokovou sazbu (v %): "))
        volba_doby = input("Zadejte dobu splácení (měsíce/roky): ").strip().lower()
        if volba_doby == "měsíce":
            doba_splaceni_mesice = int(input("Zadejte délku splácení v měsících: "))
        else:
            doba_splaceni_roky = int(input("Zadejte délku splácení v letech: "))
            doba_splaceni_mesice = doba_splaceni_roky * 12
        self.uver = Uver(castka, rocni_urokova_sazba, doba_splaceni_mesice)

    def zobraz_vysledky(self):
        if self.uver is not None:
            print("\nVýsledky:")
            print(f"Měsíční splátka: {self.uver.mesicni_splatka():.2f} Kč")
            print(f"Celkově zaplacená částka: {self.uver.celkova_zaplacena_castka():.2f} Kč")
            print(f"Celkově zaplacené úroky: {self.uver.celkove_uroky():.2f} Kč")
        else:
            print("Úvěr nebyl zadán.")

kalkulacka = KalkulackaUveru()
kalkulacka.ziskej_vstup()
kalkulacka.zobraz_vysledky()
