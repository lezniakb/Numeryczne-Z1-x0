def metodaBisekcji(funkcja, poczatek, koniec, dokladnosc=0, maksIteracji=0):
    if funkcja(poczatek) * funkcja(koniec) >= 0:
        print("Funkcja nie zmienia znaku na końcach przedziału\nMetoda bisekcji nie zostaje uwzględniona.")
        return None, 0
    iteracja = 0
    maksIteracjiDokladnosc = 200
    a = poczatek
    b = koniec

    while True:
        iteracja += 1
        fa = funkcja(a)
        fb = funkcja(b)

        # wyznaczamy punkt środkowy
        x0 = (a + b) / 2.0
        f0 = funkcja(x0)

        if dokladnosc != 0:
            modulFunkcji = abs(f0)
            if modulFunkcji < dokladnosc:
                return x0, iteracja
            elif iteracja >= maksIteracjiDokladnosc:
                print("Przekroczono maksymalną ilość iteracji dla warunku |f(x)| < epsilon")
                return None, iteracja
        elif maksIteracji != 0 and iteracja >= maksIteracji:
            return x0, iteracja

        # warunki konieczne do metody bisekcji
        if f0 * fb < 0:
            a = x0
        elif f0 * fa < 0:
            b = x0