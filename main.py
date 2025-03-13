import matplotlib.pyplot as plt
import numpy as np
import metoda_bisekcji as bis
import metoda_siecznych as sie
import rownania as r


def rysowanieFunkcji(funkcja, poczatek=-20.0, koniec=20.0, miejsceZeroweBisekcji=None, miejsceZeroweSiecznych=None):
    # Przygotowanie danych do wykresu – obliczenie wartości funkcji dla tablicy punktów
    iloscPunktow = 400
    tablicaX = np.linspace(poczatek, koniec, iloscPunktow)
    tablicaY = []

    for x in tablicaX:
        tablicaY.append(funkcja(x))

    # Rysowanie wykresu
    plt.figure(figsize=(8, 6))
    plt.plot(tablicaX, tablicaY, label="f(x)")
    plt.axhline(0, color="black", linewidth=0.5)
    if miejsceZeroweBisekcji is not None:
        plt.scatter(miejsceZeroweBisekcji, 0, color="None", zorder=5,
                    label="Bisekcja", marker="^", edgecolors="red", s=100)
    if miejsceZeroweSiecznych is not None:
        plt.scatter(miejsceZeroweSiecznych, 0, color="None", zorder=5,
                    label="Sieczne", marker="X", edgecolors="blue", s=100)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres funkcji")
    plt.legend()
    plt.grid(True)
    plt.show()


# main
funkcje = {
    1:("Wielomianowa: 3x^6 + x^3 - 2x^2 - 1 (Horner)", r.funkcjaWielomianowa),
    2:("Trygonometryczna: sin(x) - 0.5", r.funkcjaTrygonometryczna),
    3:("Wykładnicza: exp(x) - 3", r.funkcjaWykladnicza),
    4:("Złożona: exp(sin(x)) - 2", r.funkcjaZlozona),
    5:("Kwadratowa: (bez miejsc zerowych)", r.funkcjaBezMiejscZerowych)
}
print("Dostępne funkcje:")
for klucz in funkcje:
    print(str(klucz) + ": " + funkcje[klucz][0])
wyborFunkcji = int(input("Podaj numer funkcji: ")) #input - dodać zabezpieczenia

funkcjaWybrana = funkcje[wyborFunkcji][1]

rysowanieFunkcji(funkcjaWybrana)

poczatekPrzedzialu = float(input("Podaj początek przedziału a: ")) #input - dodać zabezpieczenia
koniecPrzedzialu = float(input("Podaj koniec przedziału b: ")) #input - dodać zabezpieczenia

# sprawdzenie czy funkcja zmienia znak na koncach przedzialu
if funkcjaWybrana(poczatekPrzedzialu) * funkcjaWybrana(koniecPrzedzialu) >= 0:
    print("Funkcja nie zmienia znaku na końcach przedziału, warunek bisekcji nie został spełniony.")
    # exit(0)

print("Wybierz kryterium stopu:")
print("1: Osiągnięcie zadanej dokładności |f(x)| < epsilon")
print("2: Wykonanie określonej liczby iteracji")
wyborKryterium = int(input("Podaj numer kryterium: ")) #input - dodać zabezpieczenia
dokladnosc = 0
maksIteracji = 0
if wyborKryterium == 1:
    dokladnosc = float(input("Podaj epsilon: ")) #input - dodać zabezpieczenia
else:
    maksIteracji = int(input("Podaj liczbę iteracji: ")) #input - dodać zabezpieczenia

# metoda bisekcji tutaj liczona
miejsceZeroweBisekcji, iterBisekcji = bis.metodaBisekcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweBisekcji is not None:
    print("\nMetoda bisekcji:")
    print("Miejsce zerowe: " + str(miejsceZeroweBisekcji))
    print("Liczba iteracji: " + str(iterBisekcji))
    print("f(miejsce zerowe) = " + str(funkcjaWybrana(miejsceZeroweBisekcji)))

# tutaj sieczne
miejsceZeroweSiecznych, iterSiecznych = sie.metodaSiecznych(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweSiecznych is not None:
    print("\nMetoda siecznych:")
    print("Miejsce zerowe: " + str(miejsceZeroweSiecznych))
    print("Liczba iteracji: " + str(iterSiecznych))
    print("f(miejsce zerowe) = " + str(funkcjaWybrana(miejsceZeroweSiecznych)))

rysowanieFunkcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, miejsceZeroweBisekcji, miejsceZeroweSiecznych)

"""
3. zmodyfikować wykres (zmienić kropkę na trójkąt i dać przezroczyste wypełnienie)
4. pozmieniać np. "is not None" i poprawić kod stylistycznie (wygląda sus) + dodawać zmienne pośrednie
6. kod się miejscami powtarza
7. zmodyfikować kod, żeby w przypadku funkcji bez miejsc zerowych w metodzie sieczych był limit iteracji np. 200
"""