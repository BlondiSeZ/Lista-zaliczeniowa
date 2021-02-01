print("'koniec' konczy operacje")
while True:
    x = input("Wybierz rodzaj wynagrodzenia: netto, brutto:")
    if x == 'koniec':
        break
    if x in ('netto' ,'brutto'):
        if x == 'netto':
            b = float(input("wielkość wynagrodzenia: "))
            a = b * 1.389
            a = round(a, 2)
            emerytalne = float(a) * 0.0976
            rentowe = float(a) * 0.065
            wypadkowe = float(a) * 0.0167
            fp = float(a) * 0.0245
            FGSP = float(a) * 0.001
            print("Brutto:", a)
            print("Emerytalne", emerytalne)
            print("Rentowe: ", float(rentowe))
            print("Wypadkowe: ", float(wypadkowe))
            print("FP: ", float(fp))
            print("FGSP: ", float(FGSP))

        if x == 'brutto':
            a = float(input("wielkość wynagrodzenia: "))
            x = a * 0.72
            x = round(x, 2)
            emerytalne = float(a) * 0.0976
            rentowe = float(a) * 0.065
            wypadkowe = float(a) * 0.0167
            fp = float(a) * 0.0245
            FGSP = float(a) * 0.001
            print("Netto:", a)
            print("Emerytalne", emerytalne)
            print("Rentowe: ", float(rentowe))
            print("Wypadkowe: ", float(wypadkowe))
            print("FP: ", float(fp))
            print("FGSP: ", float(FGSP))
    else:
        print("Nieprawidłowy znak operacji!")