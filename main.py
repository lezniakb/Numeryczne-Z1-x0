import math
import matplotlib.pyplot as plt
import numpy as np

# Obliczanie wielomianu metodą Hornera
def obliczWielomianHornerem(x, wspolczynniki, dlugosc):
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
    return obliczWielomianHornerem(x, wspolczynniki, dlugosc)

# Funkcja trygonometryczna: sin(x) - 0.5
def funkcjaTrygonometryczna(x):
    return math.sin(x) - 0.5

# Funkcja wykładnicza: exp(x) - 3
def funkcjaWykladnicza(x):
    return math.e**(x) - 3

# Funkcja złożona: exp(sin(x)) - 2
def funkcjaZlozona(x):
    return math.e**(math.sin(x)) - 2

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

def znajdzPrzedzialUnimodalny(funkcja, poczatek, koniec, tolerancja, limitIteracji):
    i = 0
    znaleziono = funkcja(poczatek) * funkcja(koniec) < 0
    odleglosc = abs(koniec - poczatek)
    warunek = (not znaleziono) and (i < limitIteracji) and (odleglosc >= tolerancja)
    while warunek:
        i += 1
        srodek = (poczatek + koniec) / float(2)
        if funkcja(poczatek) * funkcja(srodek) < 0:
            koniec = srodek
        elif funkcja(srodek) * funkcja(koniec) < 0:
            poczatek = srodek
        else:
            odleglosc = abs(koniec - poczatek)
            delta = odleglosc / float(2)
            poczatek = poczatek - delta
            koniec = koniec + delta
        znaleziono = (funkcja(poczatek) * funkcja(koniec) < 0)
        warunek = (not znaleziono) and (i < limitIteracji) and (abs(koniec - poczatek) >= tolerancja)
    return poczatek, koniec, i

# main
funkcje = {
    1:("Wielomianowa: x^3 - 2x^2 - 5 (Horner)", funkcjaWielomianowa),
    2:("Trygonometryczna: sin(x) - 0.5", funkcjaTrygonometryczna),
    3:("Wykładnicza: exp(x) - 3", funkcjaWykladnicza),
    4:("Złożona: exp(sin(x)) - 2", funkcjaZlozona)
}
print("Dostępne funkcje:")
for klucz in funkcje:
    print(str(klucz) + ": " + funkcje[klucz][0])
wyborFunkcji = int(input("Podaj numer funkcji: "))

# zmienic tu
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

# DO ZROBIENIA
"""
1. wielomiany/funkcje-tryg/etc. mają mieć współczynniki do wpisania przez użytkownika (? zapytać się na labach)
2. dodać komentarze i zrozumieć kod
3. zmodyfikować wykres
4. pozmieniać np. "is not None"
5. rozdzielić funkcje na pliki źródłowe (na górze dodać 'import drugiplik.py')
6. kod się miejscami powtarza
"""