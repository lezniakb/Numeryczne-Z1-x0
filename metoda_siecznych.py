def metodaSiecznych(funkcja, poczatek, koniec, dokladnosc=None, maksIteracji=None):
    iteracja = 0
    x0 = poczatek
    x1 = koniec
    bladDzielenia = False
    if dokladnosc != None:
        modulFunkcji = abs(funkcja(x1))
        warunek = modulFunkcji >= dokladnosc
        while warunek and (bladDzielenia == False):
            iteracja += 1
            mianownik = funkcja(x1) - funkcja(x0)
            if mianownik == 0:
                print("Błąd: dzielenie przez zero w metodzie siecznych!")
                bladDzielenia = True
            else:
                x2 = x1 - funkcja(x1) * (x1 - x0) / mianownik
                x0 = x1
                x1 = x2
            modulFunkcji = abs(funkcja(x1))
            warunek = modulFunkcji >= dokladnosc and (bladDzielenia is False)
    elif maksIteracji is not None:
        warunek = iteracja < maksIteracji
        while warunek and (bladDzielenia == False):
            iteracja += 1
            mianownik = funkcja(x1) - funkcja(x0)
            if mianownik == 0:
                print("Błąd: dzielenie przez zero w metodzie siecznych!")
                bladDzielenia = True
            else:
                x2 = x1 - funkcja(x1) * (x1 - x0) / mianownik
                x0 = x1
                x1 = x2
            warunek = iteracja < maksIteracji and (bladDzielenia is False)
    if bladDzielenia:
        return None, iteracja
    return x1, iteracja