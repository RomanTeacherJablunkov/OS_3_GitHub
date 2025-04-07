class Uver:
    def __init__(self, castka, urokova_sazba, doba_splaceni_mesice):
        self.castka = castka
        self.urokova_sazba = urokova_sazba / 100 / 12
        self.doba_splaceni_mesice = doba_splaceni_mesice

    def mesicni_splatka(self):
        citatel = self.castka * self.urokova_sazba * (1 + self.urokova_sazba) ** self.doba_splaceni_mesice
        jmenovatel = (1 + self.urokova_sazba) ** self.doba_splaceni_mesice - 1
        return citatel / jmenovatel

    def celkova_zaplacena_castka(self):
        return self.mesicni_splatka() * self.doba_splaceni_mesice

    def celkove_uroky(self):
        return self.celkova_zaplacena_castka() - self.castka

    def splatkovy_kalendar(self):
        zustatek = self.castka
        mesicni_splatka = self.mesicni_splatka()
        print("\nSplátkový kalendář:")
        for mesic in range(1, self.doba_splaceni_mesice + 1):
            splatka_urok = zustatek * self.urokova_sazba
            splatka_jistina = mesicni_splatka - splatka_urok
            zustatek -= splatka_jistina
            print(f"Měsíc {mesic}: Jistina: {splatka_jistina:.2f} Kč, Úrok: {splatka_urok:.2f} Kč, Zůstatek: {zustatek:.2f} Kč")


class KalkulackaUveru:
    def __init__(self):
        self.uver = None

    def vstupy_uzivatele(self):
        castka = float(input("Zadejte výši úvěru (v Kč): "))
        urokova_sazba = float(input("Zadejte roční úrokovou sazbu (v %): "))
        doba = input("Zadejte dobu splácení (měsíce nebo roky): ")
        doba_splaceni_mesice = int(float(doba.split()[0]) * 12) if "rok" in doba.lower() else int(doba.split()[0])
        self.uver = Uver(castka, urokova_sazba, doba_splaceni_mesice)

    def zobraz_vysledky(self):
        mesicni_splatka = self.uver.mesicni_splatka()
        celkova_castka = self.uver.celkova_zaplacena_castka()
        celkove_uroky = self.uver.celkove_uroky()
        print("\nVýsledky:")
        print(f"• Měsíční splátka: {mesicni_splatka:.2f} Kč")
        print(f"• Celkově zaplacená částka: {celkova_castka:.2f} Kč")
        print(f"• Celkově zaplacené úroky: {celkove_uroky:.2f} Kč")
        if input("\nChcete zobrazit splátkový kalendář? (ano/ne): ").lower() == "ano":
            self.uver.splatkovy_kalendar()


kalkulacka = KalkulackaUveru()
kalkulacka.vstupy_uzivatele()
kalkulacka.zobraz_vysledky()
