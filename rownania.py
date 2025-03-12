# Obliczanie wielomianu metodą Hornera
import math

# Stare
# def obliczWielomianHornerem(x, wspolczynniki, dlugosc):
#     wynik = wspolczynniki[0]
#     i = 1
#     while i < dlugosc:
#         wynik = wynik * x + wspolczynniki[i]
#         i = i + 1
#     return wynik

def obliczWielomianHornerem(x, wspolczynniki):
    wynik = wspolczynniki[0]
    for wspolczynnik in wspolczynniki[1:]:
        wynik = wynik * x + wspolczynnik
    return wynik

# # Funkcja wielomianowa – przykładowo: 3x^6 + x^3 - 2x^2 - 1
# def funkcjaWielomianowa(x):
#     wspolczynniki = [3, 0, 0, 1, -2, 0, -1]  # odpowiada 3x^6 + x^3 - 2x^2 - 1
#     dlugosc = len(wspolczynniki)
#     return obliczWielomianHornerem(x, wspolczynniki, dlugosc)

# Funkcja wielomianowa – przykładowo: x^3 - 2x^2 - 5
def funkcjaWielomianowa(x):
    wspolczynniki = [1, -2, 0, -5]  # odpowiada x^3 - 2x^2 + 0*x - 5
    # dlugosc = len(wspolczynniki)
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