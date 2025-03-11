def metodaBisekcji(funkcja, poczatek, koniec, dokladnosc=None, maksIteracji=None):
    if funkcja(poczatek) * funkcja(koniec) >= 0:
        print("Błąd: funkcja nie zmienia znaku na końcach przedziału!")
        return None, 0
    iteracja = 0
    # wyznaczamy punkt środkowy
    polowa = (poczatek + koniec) / float(2)

    # jezeli wprowadzilismy dokladnosc, to wykonuje sie ten blok
    if dokladnosc != None:
        # znajdujemy modul z obliczonej polowy funkcji
        modulPolowyFunkcji = abs(funkcja(polowa))
        sprawdzenie = modulPolowyFunkcji > dokladnosc
        # dopoki modul z polowy funkcji jest wciaz wiekszy niz zadana dokladnosc to wykonuj
        while sprawdzenie == True:
            iteracja += 1
            polowa = (poczatek + koniec) / float(2)
            if funkcja(poczatek) * funkcja(polowa) < 0:
                koniec = polowa
            else:
                poczatek = polowa
            modulPolowyFunkcji = abs(funkcja(polowa))
            # dopoki w sprawdzeniu modul kolejnej polowy funkcji jest wiekszy od zadanej dokladnosci to powtorz
            sprawdzenie = modulPolowyFunkcji > dokladnosc

    # jezeli wprowadzilismy maksymalna ilosc iteracji, to wykonuje sie ten blok
    elif maksIteracji != None:
        sprawdzenie = iteracja < maksIteracji
        # dopoki iteracji jest mniej niz podanej maksymalnej liczby to wykonuj
        while sprawdzenie == True:
            iteracja += 1
            polowa = (poczatek + koniec) / float(2)
            if funkcja(poczatek) * funkcja(polowa) < 0:
                koniec = polowa
            else:
                poczatek = polowa
            sprawdzenie = iteracja < maksIteracji
    return polowa, iteracja
