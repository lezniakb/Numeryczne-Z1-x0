import math
import matplotlib.pyplot as plt
import numpy as np
import metoda_bisekcji as bis
import metoda_siecznych as sie
import rownania as r

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
    1:("Wielomianowa: 3x^6 + x^3 - 2x^2 - 1 (Horner)", r.funkcjaWielomianowa),
    2:("Trygonometryczna: sin(x) - 0.5", r.funkcjaTrygonometryczna),
    3:("Wykładnicza: exp(x) - 3", r.funkcjaWykladnicza),
    4:("Złożona: exp(sin(x)) - 2", r.funkcjaZlozona)
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
miejsceZeroweBisekcji, iterBisekcji = bis.metodaBisekcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweBisekcji is not None:
    print("\nMetoda bisekcji:")
    print("Miejsce zerowe: " + str(miejsceZeroweBisekcji))
    print("Liczba iteracji: " + str(iterBisekcji))
    print("f(miejsce zerowe) = " + str(funkcjaWybrana(miejsceZeroweBisekcji)))

# Obliczenia metodą siecznych
miejsceZeroweSiecznych, iterSiecznych = sie.metodaSiecznych(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
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