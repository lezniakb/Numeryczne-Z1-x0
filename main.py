import matplotlib.pyplot as plt
import numpy as np
import metoda_bisekcji as bis
import metoda_siecznych as sie
import rownania as r


def rysowanieFunkcji(funkcja, poczatek=-14.0, koniec=14.0, miejsceZeroweBisekcji=None, miejsceZeroweSiecznych=None):
    punktow = 400
    tablicaX = np.linspace(poczatek, koniec, punktow)
    tablicaY = []

    for x in tablicaX:
        tablicaY.append(funkcja(x))

    plt.figure(figsize=(8.2, 6.2))
    plt.plot(tablicaX, tablicaY, label="f(x)")
    plt.axhline(0, color="black", linewidth=0.5)

    # jesli zostalo podane miejsce zerowe dla metody bisekcji to pokaz czerwony trójkąt
    if miejsceZeroweBisekcji != nieIstnieje:
        plt.scatter(miejsceZeroweBisekcji, 0, color="None", zorder=5,
                    label="Bisekcja", marker="^", edgecolors="red", s=100)

    # jesli zostalo podane miejsce zerowe dla metody siecznych to pokaz niebieski X
    if miejsceZeroweSiecznych != nieIstnieje:
        plt.scatter(miejsceZeroweSiecznych, 0, color="None", zorder=5,
                    label="Sieczne", marker="X", edgecolors="blue", s=100)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres funkcji")
    plt.legend()
    plt.grid(True)

    plt.show()


def zabezpieczenie(dane):
    if (dane.replace('.', '', 1).isdigit() or
            dane.lstrip('-').replace('.', '', 1).isdigit()):
        return True
    else:
        print("Musisz podać liczbę!")
        return False
# main
funkcje = {
    1:("Wielomianowa: 3x^6 + x^3 - 2x^2 - 1 (Horner)", r.funkcjaWielomianowa),
    2:("Trygonometryczna: sin(x) - 0.5", r.funkcjaTrygonometryczna),
    3:("Wykładnicza: exp(x) - 3", r.funkcjaWykladnicza),
    4:("Złożona: exp(sin(x)) - 2", r.funkcjaZlozona),
    5:("Kwadratowa: (bez miejsc zerowych)", r.funkcjaBezMiejscZerowych)
}
nieIstnieje = None
print("Wybierz funkcje:")
iteracja = 1
for wybor in funkcje:
    stringIteracja = str(iteracja)
    stringWybor = funkcje[wybor][0]
    print(stringIteracja + ": " + stringWybor)
    iteracja += 1

# zabezpieczenie przez wprowadzaniem zlego znaku albo nieistniejacej funkcji
wyborFunkcji = input("Podaj numer funkcji: ")
dostepneWybory = [1, 2, 3, 4, 5]

while (wyborFunkcji.isdigit() == False) or (int(wyborFunkcji) not in dostepneWybory):
    print("Podaj liczbę całkowitą z przedziału 1-5!")
    wyborFunkcji = input("Podaj numer funkcji: ")

wyborFunkcji = int(wyborFunkcji)
funkcjaWybrana = funkcje[wyborFunkcji][1]
rysowanieFunkcji(funkcjaWybrana)

poczatekPrzedzialu = input("Podaj początek przedziału: ")
while zabezpieczenie(poczatekPrzedzialu) == False:
    poczatekPrzedzialu = input("Podaj początek przedziału: ")

koniecPrzedzialu = input("Podaj koniec przedziału: ")
while zabezpieczenie(koniecPrzedzialu) == False:
    koniecPrzedzialu = input("Podaj koniec przedziału: ")

poczatekPrzedzialu = float(poczatekPrzedzialu)
koniecPrzedzialu = float(koniecPrzedzialu)

# sprawdzenie czy funkcja zmienia znak na koncach przedzialu
if funkcjaWybrana(poczatekPrzedzialu) * funkcjaWybrana(koniecPrzedzialu) >= 0:
    print("Funkcja nie zmienia znaku na końcach przedziału, warunek bisekcji nie został spełniony.")

print("Wybierz kryterium stopu:")
print("1: Osiągnięcie zadanej dokładności |f(x)| < epsilon")
print("2: Wykonanie określonej liczby iteracji")

dostepneWybory = [1, 2]
poprawnosc = 0
while poprawnosc == 0:
    wyborKryterium = input("Podaj numer kryterium: ")

    if wyborKryterium.isdigit() and int(wyborKryterium) in dostepneWybory:
        wyborKryterium = int(wyborKryterium)
        poprawnosc = 1
    else:
        print("Niewłaściwy wybór: wpisz 1 lub 2")

dokladnosc = 0
maksIteracji = 0
poprawnosc = 0

if wyborKryterium == 1:
    while poprawnosc == 0:
        dokladnosc = input("Podaj epsilon: ")
        if dokladnosc.replace('.', '', 1).isdigit() and float(dokladnosc) > 0:
            dokladnosc = float(dokladnosc)
            poprawnosc = 1
        else:
            print("Epsilon musi być większy niż 0")
else:
    while poprawnosc == 0:
        maksIteracji = input("Podaj liczbę iteracji: ")
        if maksIteracji.isdigit() and int(maksIteracji) > 0:
            maksIteracji = int(maksIteracji)
            poprawnosc = 1
        else:
            print("Liczba iteracji musi być większa niż 0")

# metoda bisekcji tutaj liczona
miejsceZeroweBisekcji, iterBisekcji = bis.metodaBisekcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweBisekcji != nieIstnieje:
    znalezionaWartoscZerowego = funkcjaWybrana(miejsceZeroweBisekcji)
    print("\nMetoda bisekcji:"
          "\nMiejsce zerowe:" + str(miejsceZeroweBisekcji) +
          "\nLiczba iteracji: " + str(iterBisekcji) +
          "\nf(miejsce zerowe) = " + str(znalezionaWartoscZerowego))

# tutaj sieczne
miejsceZeroweSiecznych, iterSiecznych = sie.metodaSiecznych(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweSiecznych != nieIstnieje:
    znalezionaWartoscZerowego = funkcjaWybrana(miejsceZeroweSiecznych)
    print("\nMetoda siecznych:"
          "\nMiejsce zerowe:" + str(miejsceZeroweSiecznych) +
          "\nLiczba iteracji: " + str(iterSiecznych) +
          "\nf(miejsce zerowe) = " + str(znalezionaWartoscZerowego))

# jesli miejsce zerowe
if miejsceZeroweBisekcji is not None and not (poczatekPrzedzialu < miejsceZeroweBisekcji < koniecPrzedzialu):
    print("DEBUG: miejsce zerowe bisekcji poza przedziałem!")
    rysowanieFunkcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, None, miejsceZeroweSiecznych)

elif miejsceZeroweSiecznych is not None and not (poczatekPrzedzialu < miejsceZeroweSiecznych < koniecPrzedzialu):
    print("DEBUG: miejsce zerowe siecznych poza przedziałem!")
    rysowanieFunkcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, miejsceZeroweBisekcji)

else:
    rysowanieFunkcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, miejsceZeroweBisekcji, miejsceZeroweSiecznych)

