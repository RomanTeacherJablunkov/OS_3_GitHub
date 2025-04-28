#zadáme program pro vstupní proměnné
sířka= float (input("zadej šířku hřiště v metrech:" ))
délka= float (input("zadej šířku hřiště v metrech:" ))
pocet_kol= float (input("zadej počet kol, které jsi uběhl :" ))
delka_kroku = float(input("zadej délku kroku v běhu (v metrech): "))
#počítání s proměnnými
obvod_hriste = 2* (sírka+délka)
pocet_kroků_kolo = obvod_hřiště / délka_kroků
pocet_kroků_celkem = pocet_kol * obvod_hřiště / délka_kroku
#výstupy pro náš program
print ("obvod hřiště je : ", obvod_hřiště "metru")
print(f"uděláš příbližně (round{pocet_kroku_kolo) za jedno kolo.")
print ("to znamená, že celkem uděláš {round(pocet_kroku_celkem)} kroků za {pocet_kol}")