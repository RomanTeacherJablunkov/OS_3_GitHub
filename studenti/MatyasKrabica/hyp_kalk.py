#Třída uvěr
class Uver:
    def __init__(self, urok, rocni_urokova_sazba, mesice):
        self.urok = urok  # Vyse uveru
        self.rocni_urokova_sazba = rocni_urokova_sazba  # Rocni urokova sazba
        self.mesice = mesice  # Doba splaceni v mesicich

    def mesicni_splatka(self):
        r = self.rocni_urokova_sazba / 100 / 12  # Mesicni urokova sazba
        n = self.mesice  # Pocet mesicu

        # Vypocet mesicni splatky podle anuitniho vzorce
        if r == 0:  # Pokud je urokova sazba 0, mesicni splatka je proste castka delena pocetem mesicu
            return self.urok / n
        else:
            return self.urok * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

    def celkove_zaplaceno(self):
        return self.mesicni_splatka() * self.mesice  # Celkove zaplacena castka

    def celkove_uroky(self):
        return self.celkove_zaplaceno() - self.urok  # Celkove zaplacene uroky


class KalkulatorUveru:
    def __init__(self):
        self.uver = None

    def zadat_udaje(self):
        # Vstupy od uzivatele
        urok = float(input("Zadejte vyse uveru (v Kc): "))
        rocni_urokova_sazba = float(input("Zadejte rocni urokovou sazbu (v %): "))
        doba_splaceni = input("Zadejte dobu splaceni (mesic nebo rok): ").strip().lower()

        # Kontrola pro mesice nebo roky
        if "rok" in doba_splaceni:
            roky = int(input("Zadejte dobu splaceni v letech: "))
            mesice = roky * 12
        elif "mesic" in doba_splaceni:
            mesice = int(input("Zadejte dobu splaceni v mesicich: "))
        else:
            print("Neplatny vstup pro dobu splaceni. Zadejte 'mesic' nebo 'rok'.")
            return

        # Vytvoreni instance Uver
        self.uver = Uver(urok, rocni_urokova_sazba, mesice)

    def zobrazit_vysledky(self):
        if not self.uver:
            print("Nejprve musite zadat udaje.")
            return

        # Vypocet a vystup vysledku
        print("\nVysledky:")
        print(f"Mesicni splatka: {self.uver.mesicni_splatka():.2f} Kc")
        print(f"Celkove zaplacena castka: {self.uver.celkove_zaplaceno():.2f} Kc")
        print(f"Celkove zaplacene uroky: {self.uver.celkove_uroky():.2f} Kc")

class AmortizacniPlan:
    def __init__(self, uver):
        self.uver = uver

    def vygenerovat_plan(self):
        # Vytvoreni tabulky splatek
        r = self.uver.rocni_urokova_sazba / 100 / 12
        n = self.uver.mesice
        mesicni_splatka = self.uver.mesicni_splatka()

        zustatek = self.uver.urok
        plan = []

        for mesic in range(1, n + 1):
            urokova_splatka = zustatek * r
            jistinova_splatka = mesicni_splatka - urokova_splatka
            zustatek -= jistinova_splatka

            # Zaokrouhleni vysledku na dve desetinna mista
            plan.append({
                'Mesic': mesic,
                'Splatka': round(mesicni_splatka, 2),
                'Urok': round(urokova_splatka, 2),
                'Jistina': round(jistinova_splatka, 2),
                'Zustatek': round(zustatek, 2)
            })

        return plan

    def vytisknout_plan(self):
        plan = self.vygenerovat_plan()
        print("\nSplatkovy kalendar:")
        print(f"{'Mesic':<8}{'Splatka':<12}{'Urok':<10}{'Jistina':<12}{'Zustatek'}")
        for radek in plan:
            print(f"{radek['Mesic']:<8}{radek['Splatka']:<12}{radek['Urok']:<10}{radek['Jistina']:<12}{radek['Zustatek']}")


# Hlavni program
if __name__ == "__main__":
    kalkulator = KalkulatorUveru()
    kalkulator.zadat_udaje()
    kalkulator.zobrazit_vysledky()

    # Moznost zobrazeni splatkového kalendáře
    zobrazit_plan = input("\nChcete zobrazit splatkovy kalendar? (ano/ne): ").strip().lower()
    if zobrazit_plan == 'ano':
        amortizacni_plan = AmortizacniPlan(kalkulator.uver)
        amortizacni_plan.vytisknout_plan()
