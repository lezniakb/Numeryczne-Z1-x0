def metodaSiecznych(funkcja, poczatek, koniec, dokladnosc=0, maksIteracji=0):
    iteracja = 0
    maksIteracjiDokladnosc = 200
    x1 = poczatek
    x2 = koniec

    while True:
        iteracja += 1
        mianownik = funkcja(x2) - funkcja(x1)
        if mianownik == 0:
            print("Błąd: dzielenie przez zero w metodzie siecznych!")
            return None, iteracja
        else:
            x3 = x2 - funkcja(x2) * (x2 - x1) / mianownik
            x1 = x2
            x2 = x3

        if dokladnosc != 0:
            modulFunkcji = abs(funkcja(x2))
            if modulFunkcji < dokladnosc:
                break
            elif iteracja >= maksIteracjiDokladnosc:
                print("Błąd: przekroczono maksymalną ilość iteracji dla warunku |f(xi)| < epsilon")
                return None, iteracja
        elif maksIteracji != 0 and iteracja >= maksIteracji:
            break

    return x2, iteracja

    #
    # bladDzielenia = False
    # if dokladnosc != 0:
    #     modulFunkcji = abs(funkcja(x2))
    #     warunek = modulFunkcji >= dokladnosc
    #     while warunek and (bladDzielenia == False):
    #         iteracja += 1
    #         mianownik = funkcja(x2) - funkcja(x1)
    #         if mianownik == 0:
    #             print("Błąd: dzielenie przez zero w metodzie siecznych!")
    #             bladDzielenia = True
    #         else:
    #             x3 = x2 - funkcja(x2) * (x2 - x1) / mianownik
    #             x1 = x2
    #             x2 = x3
    #         modulFunkcji = abs(funkcja(x2))
    #         warunek = modulFunkcji >= dokladnosc and (bladDzielenia is False)
    #         # Próba napisania warunku końca przy braku miejsc zerowych
    #         # if iteracja >= 200:
    #         #     print("Osiągnięto limit iteracji, funkcja nie ma miejsc zerowych")
    #         #     warunek = False
    # elif maksIteracji != 0:
    #     warunek = iteracja < maksIteracji
    #     while warunek and (bladDzielenia == False):
    #         iteracja += 1
    #         mianownik = funkcja(x2) - funkcja(x1)
    #         if mianownik == 0:
    #             print("Błąd: dzielenie przez zero w metodzie siecznych!")
    #             bladDzielenia = True
    #         else:
    #             x3 = x2 - funkcja(x2) * (x2 - x1) / mianownik
    #             x1 = x2
    #             x2 = x3
    #         warunek = iteracja < maksIteracji and (bladDzielenia is False)
    # if bladDzielenia:
    #     return None, iteracja
    # return x2, iteracja