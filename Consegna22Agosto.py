selezione = ""
while selezione != 0:
    selezione = int(input("\nScegli una figura di cui calcolare il perimetro.\nDigita:\n1 per un quadrato;\n2 per un cerchio;\n3 per un rettangolo;\n0 per uscire.\n"))

    if selezione == 1:
        lato_q = int(input("Inserisci la lunghezza del lato: "))
        perim_q = lato_q * 4
        print(f"\nIl perimetro di un quadrato con un lato di {lato_q} è uguale a {perim_q}.")

    elif selezione == 2:
        raggio = int(input("Inserisci la lunghezza del raggio: "))
        circonferenza = 2*3.14*raggio
        print(f"\nLa circonferenza di un cerchio con raggio di {raggio} è uguale a {circonferenza}.")

    elif selezione == 3:
        base = int(input("Inserisci la base: "))
        altezza = int(input("Inserisci l'altezza: "))
        perim_r = (base+altezza)*2
        print(f"\nIl perimetro di un rettangolo con base di {base} e altezza di {altezza} è uguale a {perim_r}.")

    elif selezione == 0:
        break