def dzielniki_wlasciwe(n):
    dzielniki = []
    for i in range(1, n):
        if n % i == 0:
            dzielniki.append(i)
    return dzielniki

# Przykładowe użycie:
print(dzielniki_wlasciwe(12))
