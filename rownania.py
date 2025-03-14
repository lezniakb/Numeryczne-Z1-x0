import math


def obliczWielomianHornerem(x, wspolczynniki):
    wynik = wspolczynniki[0]
    for wspolczynnik in wspolczynniki[1:]:
        wynik = wynik * x + wspolczynnik
    return wynik


def funkcjaWielomianowa(x):
    wspolczynniki = [1, -2, 0, -5] # odpowiada x^3 - 2x^2 + 0*x - 5
    return obliczWielomianHornerem(x, wspolczynniki) #, dlugosc)

# sin(x) - 0.5
def funkcjaTrygonometryczna(x):
    return math.sin(x) - 0.5

# exp(x) - 3
def funkcjaWykladnicza(x):
    return math.e**(x) - 3

# exp(sin(x)) - 2
def funkcjaZlozona(x):
    return math.e**(math.sin(x)) - 2


def funkcjaBezMiejscZerowych(x):
    wspolczynniki = [1, 0, 5] # odpowiada x^2 + 5
    return obliczWielomianHornerem(x, wspolczynniki)