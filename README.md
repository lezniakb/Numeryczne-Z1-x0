# Metody numeryczne Zadanie 1
## Opis
[PL]
Repozytorium zawiera algorytm wyszukiwania miejsca zerowego przy użyciu metod bisekcji i siecznych w języku Python. Zadanie realizowane jest w ramach przedmiotu "*Metody numeryczne i optymalizacja*" na Politechnice Łódzkiej - 4 semestr na kierunku Informatyka Stosowana

[EN]
The repository contains an algorithm for finding the zero of a function using the bisection and secant methods in Python. The task is carried out as part of the "Numerical Methods and Optimization" course at Lodz University of Technology – 4th semester in Computer Science.

## Dodatkowe informacje na temat zadania
W zadaniu zaimplementowane zostały dwie metody stopu (zakończenia poszukiwań):
- zadana dokładność obliczeń (Epsilon)
- wykonanie określonej przez użytkownika liczby iteracji

### Funkcjonalność
- [x] 1. Menu główne z wyborem funkcji matematycznych, metody stopu, oraz zabezpieczeniami
- [x] 2. Implementacja metody bisekcji (własny algorytm)
- [x] 3. Implementacja metody siecznych (własny algorytm)
- [x] 4. Rysowanie funkcji przy użyciu matplotlib

## Opis rozwiązania
W zadaniu wykorzystano dwie metody wyznaczania miejsca zerowego: 
- metodę bisekcji
- metodę siecznych
Użytkownik wybiera warunek stopu, który kończy działanie pętli. Warunkiem stopu jest osiągnięcie zadanej dokładności obliczeń (w naszym przypadku wariant B) lub wykonanie określonej przez użytkownika liczby iteracji.

## Metoda Bisekcji
Sposób znajdywania miejsca zerowego funkcji przez zapętlone eliminowanie połowy przedziału, a następnie wybranie tej połowy, która zawiera poszukiwany pierwiastek (gdzie funkcja zmienia znak).
### Działanie algorytmu:
1. Sprawdzany jest warunek początkowy (wzór 1). 
Jeśli nie jest on spełniony, to metoda nie jest wykonywana.<br />
2. Uruchomiona zostaję pętla, zaczynająca się od znalezienia trzech punktów: 
f(a), f(b) oraz x_0 (wzór 2) jednakowo odległych od siebie.<br />
3. Sprawdzany jest warunek stopu wybrany przez użytkownika:<br />
3. a) Dla warunku osiągnięcia zadanej dokładności, pętla kończy się gdy zostanie osiągnięty warunek ze wzoru 3. Użytkownik podaje wybrany przez siebie epsilon przed wywołaniem funkcji. W przypadku naszego kodu zamieszczono dodatkowy licznik iteracji zapobiegający uzyskaniu nieskończonej pętli.<br />
3. b) Dla warunku wykonania określonej liczby iteracji, pętla kończy się (i funkcja od razu zwraca wartości) gdy program wykona określoną przez użytkownika liczbę iteracji.<br />
4. Jeśli wybrany warunek stopu nie został spełniony, przedział jest zmniejszany zgodnie ze wzorem 4. lub 5.

## Metoda Siecznych
Metoda siecznych polega na wyznaczaniu miejsca przecięcia:
- siecznej poprowadzonej między wartościami na krańcach przedziału podanego przez użytkownika
- osi OX.
### Działanie algorytmu:
1. Na początku zapisywane są dwa wybrane punkty – x_1 oraz x_2, kolejno początek i koniec przedziału podanego przez użytkownika.
2. Zostaje uruchomiona pętla, która zaczyna się od obliczenia mianownika we wzorze funkcji w celu sprawdzenia czy nie doszedł on do 0.
3. Następnie w pętli obliczana jest wartość x_3, zgodnie z wzorem 1. Następuje aktualizacja (nadpisanie) wartości: 
- x_1 staje się wartością x_2 sprzed wykonania obliczenia,
- x_2 jest zastąpiona wyznaczonym x_3.
4. Dla warunku osiągnięcia zadanej dokładności, pętla kończy się gdy zostanie osiągnięty warunek ze wzoru 3. Użytkownik podaje wybrany przez siebie epsilon przed wywołaniem funkcji. W przypadku naszego kodu zamieszczono dodatkowy licznik iteracji zapobiegający uzyskaniu nieskończonej pętli.
5. Dla warunku wykonania określonej liczby iteracji, pętla kończy się (i funkcja od razu zwraca wartości) gdy program wykona określoną przez użytkownika liczbę iteracji.
6. Pętla jest kontynuowana dopóki nie zostanie spełniony wybrany warunek (lub gdy wartość mianownika wyniesie 0).

