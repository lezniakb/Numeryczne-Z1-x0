import math

# Stary Horner
# def obliczWielomianHornerem(x, wspolczynniki, dlugosc):
#     wynik = wspolczynniki[0]
#     i = 1
#     while i < dlugosc:
#         wynik = wynik * x + wspolczynniki[i]
#         i = i + 1
#     return wynik

# Obliczanie wielomianu metodą Hornera
def obliczWielomianHornerem(x, wspolczynniki):
    wynik = wspolczynniki[0]
    for wspolczynnik in wspolczynniki[1:]:
        wynik = wynik * x + wspolczynnik
    return wynik

# Propozycja innej funkcji wielomianowej
# # Funkcja wielomianowa – przykładowo: x^5 + x^4 + 2x^3 - 5x - 4
# def funkcjaWielomianowa(x):
#     wspolczynniki = [1, 1, 2, 0, -5, -4] # odpowiada x^5 + x^4 + 2x^3 - 5x - 4
#     dlugosc = len(wspolczynniki)
#     return obliczWielomianHornerem(x, wspolczynniki, dlugosc)

# Funkcja wielomianowa – przykładowo: x^3 - 2x^2 - 5
def funkcjaWielomianowa(x):
    wspolczynniki = [1, -2, 0, -5] # odpowiada x^3 - 2x^2 + 0*x - 5
    # dlugosc = len(wspolczynniki) - cofnąć odznaczenie, jak zostajemy ze starą metodą obliczania Hornera
    return obliczWielomianHornerem(x, wspolczynniki) #, dlugosc)

# Funkcja trygonometryczna: sin(x) - 0.5
def funkcjaTrygonometryczna(x):
    return math.sin(x) - 0.5

# Funkcja wykładnicza: exp(x) - 3
def funkcjaWykladnicza(x):
    return math.e**(x) - 3

# Funkcja złożona: exp(sin(x)) - 2
def funkcjaZlozona(x):
    return math.e**(math.sin(x)) - 2

# Funkcja kwadratowa, bez miejsc zerowych:  x^2 + 5
def funkcjaBezMiejscZerowych(x):
    wspolczynniki = [1, 0, 5] # odpowiada x^2 + 5
    return obliczWielomianHornerem(x, wspolczynniki)