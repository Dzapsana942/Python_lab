# Poproś użytkownika o wysokość choinki
wysokosc = int(input("Podaj wysokość choinki: "))

# Tworzymy kolejne poziomy choinki
for i in range(wysokosc):
    spacje = " " * (wysokosc - i - 1)   # spacje z lewej, by choinka była wyśrodkowana
    gwiazdki = "*" * (2 * i + 1)        # liczba gwiazdek rośnie: 1, 3, 5, 7...
    print(spacje + gwiazdki)
