import math
import matplotlib.pyplot as plt
import numpy as np

# Obliczanie wielomianu metodą Hornera
def obliczWielomianHorner(x, wspolczynniki, dlugosc):
    wynik = wspolczynniki[0]
    i = 1
    while i < dlugosc:
        wynik = wynik * x + wspolczynniki[i]
        i = i + 1
    return wynik

# Funkcja wielomianowa – przykładowo: x^3 - 2x^2 - 5
def funkcjaWielomianowa(x):
    wspolczynniki = [1, -2, 0, -5]  # odpowiada x^3 - 2x^2 + 0*x - 5
    dlugosc = len(wspolczynniki)
    return obliczWielomianHorner(x, wspolczynniki, dlugosc)

# Funkcja trygonometryczna: sin(x) - 0.5
def funkcjaTrygonometryczna(x):
    return math.sin(x) - 0.5

# Funkcja wykładnicza: exp(x) - 3
def funkcjaWykladnicza(x):
    return math.e**(x) - 3

# Funkcja złożona: exp(sin(x)) - 2
def funkcjaZlozona(x):
    return math.e**(math.sin(x)) - 2

# Metoda bisekcji bez użycia break/continue
def metodaBisekcji(funkcja, poczatek, koniec, dokladnosc=None, maksIteracji=None):
    if funkcja(poczatek) * funkcja(koniec) >= 0:
        print("Błąd: funkcja nie zmienia znaku na końcach przedziału!")
        return None, 0
    iteracja = 0
    # Inicjalne wyznaczenie punktu środkowego
    c = (poczatek + koniec) / 2.0

    if dokladnosc is not None:
        warunek = abs(funkcja(c)) >= dokladnosc
        while warunek:
            iteracja = iteracja + 1
            c = (poczatek + koniec) / 2.0
            if funkcja(poczatek) * funkcja(c) < 0:
                koniec = c
            else:
                poczatek = c
            warunek = abs(funkcja(c)) >= dokladnosc
    elif maksIteracji is not None:
        warunek = iteracja < maksIteracji
        while warunek:
            iteracja = iteracja + 1
            c = (poczatek + koniec) / 2.0
            if funkcja(poczatek) * funkcja(c) < 0:
                koniec = c
            else:
                poczatek = c
            warunek = iteracja < maksIteracji
    return c, iteracja

# Metoda siecznych bez użycia break/continue
def metodaSiecznych(funkcja, poczatek, koniec, dokladnosc=None, maksIteracji=None):
    iteracja = 0
    x0 = poczatek
    x1 = koniec
    bladDziel = False
    if dokladnosc is not None:
        warunek = abs(funkcja(x1)) >= dokladnosc
        while warunek and (bladDziel is False):
            iteracja = iteracja + 1
            mianownik = funkcja(x1) - funkcja(x0)
            if mianownik == 0:
                print("Błąd: dzielenie przez zero w metodzie siecznych!")
                bladDziel = True
            else:
                x2 = x1 - funkcja(x1) * (x1 - x0) / mianownik
                x0 = x1
                x1 = x2
            warunek = abs(funkcja(x1)) >= dokladnosc and (bladDziel is False)
    elif maksIteracji is not None:
        warunek = iteracja < maksIteracji
        while warunek and (bladDziel is False):
            iteracja = iteracja + 1
            mianownik = funkcja(x1) - funkcja(x0)
            if mianownik == 0:
                print("Błąd: dzielenie przez zero w metodzie siecznych!")
                bladDziel = True
            else:
                x2 = x1 - funkcja(x1) * (x1 - x0) / mianownik
                x0 = x1
                x1 = x2
            warunek = iteracja < maksIteracji and (bladDziel is False)
    if bladDziel:
        return None, iteracja
    return x1, iteracja

# Funkcja wyznaczająca przedział unimodalny bez break/continue
def znajdzPrzedzialUnimodalny(funkcja, poczatek, koniec, tolerancja, limitIteracji):
    iteracja = 0
    znaleziono = (funkcja(poczatek) * funkcja(koniec) < 0)
    warunek = (not znaleziono) and (iteracja < limitIteracji) and (abs(koniec - poczatek) >= tolerancja)
    while warunek:
        iteracja = iteracja + 1
        srodek = (poczatek + koniec) / 2.0
        if funkcja(poczatek) * funkcja(srodek) < 0:
            koniec = srodek
        elif funkcja(srodek) * funkcja(koniec) < 0:
            poczatek = srodek
        else:
            delta = abs(koniec - poczatek) / 2.0
            poczatek = poczatek - delta
            koniec = koniec + delta
        znaleziono = (funkcja(poczatek) * funkcja(koniec) < 0)
        warunek = (not znaleziono) and (iteracja < limitIteracji) and (abs(koniec - poczatek) >= tolerancja)
    return poczatek, koniec, iteracja

# main
funkcje = {
    1: ("Wielomianowa: x^3 - 2x^2 - 5 (Horner)", funkcjaWielomianowa),
    2: ("Trygonometryczna: sin(x) - 0.5", funkcjaTrygonometryczna),
    3: ("Wykładnicza: exp(x) - 3", funkcjaWykladnicza),
    4: ("Złożona: exp(sin(x)) - 2", funkcjaZlozona)
}
print("Dostępne funkcje:")
for klucz in funkcje:
    print(str(klucz) + ": " + funkcje[klucz][0])
wyborFunkcji = int(input("Podaj numer funkcji: "))
funkcjaWybrana = funkcje.get(wyborFunkcji, funkcje[1])[1]

poczatekPrzedzialu = float(input("Podaj początek przedziału a: "))
koniecPrzedzialu = float(input("Podaj koniec przedziału b: "))

# Sprawdzenie założenia o przeciwnych znakach na końcach przedziału
if funkcjaWybrana(poczatekPrzedzialu) * funkcjaWybrana(koniecPrzedzialu) >= 0:
    print("Funkcja nie zmienia znaku na końcach przedziału.")
    print("Próba wyznaczenia przedziału unimodalnego...")
    poczatekPrzedzialu, koniecPrzedzialu, iterUnimodal = znajdzPrzedzialUnimodalny(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, 1e-6, 50)
    print("Znaleziono przedział: [" + str(poczatekPrzedzialu) + ", " + str(koniecPrzedzialu) + "] po " + str(iterUnimodal) + " iteracjach.")

print("Wybierz kryterium stopu:")
print("1: Osiągnięcie zadanej dokładności |f(x)| < epsilon")
print("2: Wykonanie określonej liczby iteracji")
wyborKryterium = int(input("Podaj numer kryterium: "))
dokladnosc = None
maksIteracji = None
if wyborKryterium == 1:
    dokladnosc = float(input("Podaj epsilon: "))
else:
    maksIteracji = int(input("Podaj liczbę iteracji: "))

# Obliczenia metodą bisekcji
miejsceZeroweBisekcji, iterBisekcji = metodaBisekcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweBisekcji is not None:
    print("\nMetoda bisekcji:")
    print("Miejsce zerowe: " + str(miejsceZeroweBisekcji))
    print("Liczba iteracji: " + str(iterBisekcji))
    print("f(miejsce zerowe) = " + str(funkcjaWybrana(miejsceZeroweBisekcji)))

# Obliczenia metodą siecznych
miejsceZeroweSiecznych, iterSiecznych = metodaSiecznych(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweSiecznych is not None:
    print("\nMetoda siecznych:")
    print("Miejsce zerowe: " + str(miejsceZeroweSiecznych))
    print("Liczba iteracji: " + str(iterSiecznych))
    print("f(miejsce zerowe) = " + str(funkcjaWybrana(miejsceZeroweSiecznych)))

# Przygotowanie danych do wykresu – obliczenie wartości funkcji dla tablicy punktów
iloscPunktow = 400
tablicaX = np.linspace(poczatekPrzedzialu, koniecPrzedzialu, iloscPunktow)
tablicaY = []
i = 0
while i < len(tablicaX):
    tablicaY.append(funkcjaWybrana(tablicaX[i]))
    i = i + 1

# Rysowanie wykresu
plt.figure(figsize=(8, 6))
plt.plot(tablicaX, tablicaY, label="f(x)")
plt.axhline(0, color="black", linewidth=0.5)
if miejsceZeroweBisekcji is not None:
    plt.scatter(miejsceZeroweBisekcji, funkcjaWybrana(miejsceZeroweBisekcji), color="red", zorder=5, label="Bisekcja")
if miejsceZeroweSiecznych is not None:
    plt.scatter(miejsceZeroweSiecznych, funkcjaWybrana(miejsceZeroweSiecznych), color="blue", zorder=5, label="Sieczne")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji")
plt.legend()
plt.grid(True)
plt.show()

