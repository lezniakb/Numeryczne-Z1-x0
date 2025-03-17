import matplotlib.pyplot as plt
import numpy as np
import metoda_bisekcji as bis
import metoda_siecznych as sie
import rownania as r


def rysowanieFunkcji(funkcja, poczatek=-15.0, koniec=15.0, miejsceZeroweBisekcji=None, miejsceZeroweSiecznych=None):
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
    1:("Wielomianowa: x^3 - 2x^2 - 5 (Horner)", r.funkcjaWielomianowaDodatnia),
    2:("Trygonometryczna: sin(x) - 0.5", r.funkcjaTrygonometryczna),
    3:("Wykładnicza: exp(x) - 3", r.funkcjaWykladnicza),
    4:("Złożona: exp(sin(x)) - 2", r.funkcjaZlozona),
    5:("Kwadratowa: x^2 + 5 (bez miejsc zerowych)", r.funkcjaBezMiejscZerowych),
    6:("Wielomianowa: -2x^3 + 4x^2 + 5 (Horner)", r.funkcjaWielomianowaUjemna)
}
nieIstnieje = None

# wybor funkcji przez uzytkownika
print("Wybierz funkcje:")
iteracja = 1
for wybor in funkcje:
    stringIteracja = str(iteracja)
    stringWybor = funkcje[wybor][0]
    print(stringIteracja + ": " + stringWybor)
    iteracja += 1

# zabezpieczenie przez wprowadzaniem zlego znaku albo nieistniejacej funkcji
wyborFunkcji = input("Podaj numer funkcji: ")
dostepneWybory = [1, 2, 3, 4, 5, 6]

# powtarzaj prosbe o podanie funkcji z zakresu
while (wyborFunkcji.isdigit() == False) or (int(wyborFunkcji) not in dostepneWybory):
    print("Podaj liczbę całkowitą z przedziału 1-6!")
    wyborFunkcji = input("Podaj numer funkcji: ")

# zapisz funkcje podana przez uzytkownika
wyborFunkcji = int(wyborFunkcji)
funkcjaWybrana = funkcje[wyborFunkcji][1]

# zmniejszenie przedzialow na rysunku dla widocznosci
if wyborFunkcji == 1 or wyborFunkcji == 6:
    rysowanieFunkcji(funkcjaWybrana, -2, 4)
elif wyborFunkcji == 3:
    rysowanieFunkcji(funkcjaWybrana, -2, 2.5)
else:
    rysowanieFunkcji(funkcjaWybrana, -5, 5)

# zabezpieczenie przed podaniem niewlasciwego przedzialu
poczatekPrzedzialu = input("Podaj początek przedziału: ")
while zabezpieczenie(poczatekPrzedzialu) == False:
    poczatekPrzedzialu = input("Podaj początek przedziału: ")

koniecPrzedzialu = input("Podaj koniec przedziału: ")
while zabezpieczenie(koniecPrzedzialu) == False:
    koniecPrzedzialu = input("Podaj koniec przedziału: ")

print("\n-------------\n"
      "Wybrana funkcja:", funkcje[wyborFunkcji][0],
      f"\nWybrany przedział: [{poczatekPrzedzialu}, {koniecPrzedzialu}]"
      f"\n-------------\n")

# zapisz przedzialy jako float
poczatekPrzedzialu = float(poczatekPrzedzialu)
koniecPrzedzialu = float(koniecPrzedzialu)

if koniecPrzedzialu <= poczatekPrzedzialu:
    print("Wprowadzono niewłaściwy przedział!")
    exit(0)

# wyswietl kryteria stopu
print("Wybierz kryterium stopu:\n"
      "1: Osiągnięcie zadanej dokładności |f(x)| < epsilon\n"
      "2: Wykonanie określonej liczby iteracji")

# pros uzytkownika w petli o poprawne wybranie kryterium stopu
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


# sprawdzaj w petli czy uzytkownik dobrze podal epsilon
if wyborKryterium == 1:
    while poprawnosc == 0:
        dokladnosc = input("Podaj epsilon: ")
        if dokladnosc.replace('.', '', 1).isdigit() and float(dokladnosc) > 0:
            dokladnosc = float(dokladnosc)
            print("\n-------------\n"
                  "Wybrane kryterium stopu: Epsilon =", dokladnosc,
                  "\n-------------\n")
            poprawnosc = 1
        else:
            print("Epsilon musi być liczbą większą niż 0")
# sprawdzaj w petli czy uzytkownik dobrze podal liczbe iteracji
else:
    while poprawnosc == 0:
        maksIteracji = input("Podaj liczbę iteracji: ")
        if maksIteracji.isdigit() and int(maksIteracji) > 0:
            maksIteracji = int(maksIteracji)
            print("\n-------------\n"
                  "Wybrane kryterium stopu: Liczba iteracji =", maksIteracji,
                  "\n-------------\n")
            poprawnosc = 1
        else:
            print("Liczba iteracji musi być liczbą całkowitą większą niż 0")


print("[Wyniki]")
# metoda bisekcji tutaj liczona
miejsceZeroweBisekcji, iterBisekcji = bis.metodaBisekcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweBisekcji != nieIstnieje and poczatekPrzedzialu < miejsceZeroweBisekcji < koniecPrzedzialu:
    znalezionaWartoscZerowego = funkcjaWybrana(miejsceZeroweBisekcji)
    print("------Metoda bisekcji------"
          "\nMiejsce zerowe: " + str(miejsceZeroweBisekcji) +
          "\nLiczba iteracji: " + str(iterBisekcji) +
          "\nf(miejsce zerowe) = " + str(znalezionaWartoscZerowego))
else:
    print("Nie udało się wykorzystać metody bisekcji do znalezienia miejsca zerowego w podanym przedziale!\n"
          "Spróbuj zmienić przedział.")
    miejsceZeroweBisekcji = nieIstnieje

# tutaj sieczne
miejsceZeroweSiecznych, iterSiecznych = sie.metodaSiecznych(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, dokladnosc, maksIteracji)
if miejsceZeroweSiecznych != nieIstnieje and poczatekPrzedzialu < miejsceZeroweSiecznych < koniecPrzedzialu:
    znalezionaWartoscZerowego = funkcjaWybrana(miejsceZeroweSiecznych)
    print("\n------Metoda siecznych------"
          "\nMiejsce zerowe: " + str(miejsceZeroweSiecznych) +
          "\nLiczba iteracji: " + str(iterSiecznych) +
          "\nf(miejsce zerowe) = " + str(znalezionaWartoscZerowego))
else:
    print("\nNie udało się wykorzystać metody siecznych do znalezienia miejsca zerowego w podanym przedziale!")
    miejsceZeroweSiecznych = nieIstnieje

rysowanieFunkcji(funkcjaWybrana, poczatekPrzedzialu, koniecPrzedzialu, miejsceZeroweBisekcji, miejsceZeroweSiecznych)