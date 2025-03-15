def metodaSiecznych(funkcja, poczatek, koniec, dokladnosc=0, maksIteracji=0):
    iteracja = 0
    maksIteracjiDokladnosc = 200
    x1 = poczatek
    x2 = koniec

    for petla in range(maksIteracjiDokladnosc):
        iteracja += 1
        mianownik = funkcja(x2) - funkcja(x1)
        # gdy funkcja zejdzie tak blisko 0 ze program uzna ze jest rowna 0
        if mianownik == 0:
            return x2, iteracja
        else:
            x3 = x2 - funkcja(x2) * (x2 - x1) / mianownik
            x1 = x2
            x2 = x3

        if dokladnosc != 0:
            modulFunkcji = abs(funkcja(x2))
            if modulFunkcji < dokladnosc:
                return x2, iteracja
            elif iteracja >= maksIteracjiDokladnosc:
                return None, iteracja
        elif maksIteracji != 0 and iteracja >= maksIteracji:
            return x2, iteracja

    return x2, iteracja