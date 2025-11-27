def sformatuj_liste(lista):
    wynik = []

    for element in lista:
        if isinstance(element, list):
            wynik.extend(sformatuj_liste(element))
        elif isinstance(element, (int, float)):
            wynik.append(element)
        else:
            raise TypeError(f"Nieprawidłowy typ: {type(element)} – tylko liczby i listy są dozwolone.")

    return wynik


# ⬇️ Łapiemy błąd, żeby program się nie wywalił
dane = [1, [2, [3, 4], 5], "ola"]

try:
    wynik = sformatuj_liste(dane)
    print("Spłaszczona lista:", wynik)
except TypeError as e:
    print("Błąd:", e)


