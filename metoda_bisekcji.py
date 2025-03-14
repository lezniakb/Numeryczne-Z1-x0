def metodaBisekcji(funkcja, poczatek, koniec, dokladnosc=0, maksIteracji=0):
    if funkcja(poczatek) * funkcja(koniec) >= 0:
        print("Funkcja nie zmienia znaku na końcach przedziału\nMetoda bisekcji nie zostaje uwzględniona.")
        return None, 0
    iteracja = 0
    maksIteracjiDokladnosc = 200
    a = poczatek
    b = koniec

    czySpelniony = False
    while czySpelniony == False:
        iteracja += 1
        fa = funkcja(a)
        fb = funkcja(b)

        # wyznaczamy punkt środkowy
        x0 = (a + b) / float(2)
        f0 = funkcja(x0)

        if dokladnosc != 0:
            modulFunkcji = abs(f0)
            if modulFunkcji < dokladnosc:
                return x0, iteracja
            elif iteracja >= maksIteracjiDokladnosc:
                print("Błąd: przekroczono limit iteracji (zapobiegnięcie nieskończonej pętli")
                return None, iteracja
        elif maksIteracji != 0 and iteracja >= maksIteracji:
            return x0, iteracja

        # warunki konieczne do metody bisekcji
        if f0 * fb < 0:
            a = x0
        elif f0 * fa < 0:
            b = x0

    return x0, iteracja

    # # jezeli wprowadzilismy dokladnosc, to wykonuje sie ten blok
    # if dokladnosc != 0:
    #     # znajdujemy modul z obliczonej polowy funkcji
    #     modulPolowyFunkcji = abs(funkcja(x0))
    #     sprawdzenie = modulPolowyFunkcji > dokladnosc
    #     # dopoki modul z polowy funkcji jest wciaz wiekszy niz zadana dokladnosc to wykonuj
    #     while sprawdzenie == True:
    #         iteracja += 1
    #         x0 = (a + b) / float(2)
    #         if funkcja(a) * funkcja(x0) < 0:
    #             b = x0
    #         else:
    #             a = x0
    #         modulPolowyFunkcji = abs(funkcja(x0))
    #         # dopoki w sprawdzeniu modul kolejnej polowy funkcji jest wiekszy od zadanej dokladnosci to powtorz
    #         sprawdzenie = modulPolowyFunkcji > dokladnosc
    #
    # # jezeli wprowadzilismy maksymalna ilosc iteracji, to wykonuje sie ten blok
    # elif maksIteracji != 0:
    #     sprawdzenie = iteracja < maksIteracji
    #     # dopoki iteracji jest mniej niz podanej maksymalnej liczby to wykonuj
    #     while sprawdzenie == True:
    #         iteracja += 1
    #         x0 = (a + b) / float(2)
    #         if funkcja(a) * funkcja(x0) < 0:
    #             b = x0
    #         else:
    #             a = x0
    #         sprawdzenie = iteracja < maksIteracji
    # return x0, iteracja
