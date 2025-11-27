# Wyświetlanie pierwszych 10 liczb ciągu Fibonacciego

a = 0   # pierwsza liczba
b = 1   # druga liczba

print(a)  # wypisz 0
print(b)  # wypisz 1

for i in range(8):  # jeszcze 8 kolejnych liczb, razem będzie 10
    c = a + b       # nowa liczba to suma dwóch poprzednich
    print(c)        # wypisz nową liczbę
    a = b           # przesuń liczby do przodu
    b = c

