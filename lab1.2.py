# Pobieranie danych dla pierwszej liczby zespolonej
a_re = float(input("Podaj część rzeczywistą pierwszej liczby: "))
a_im = float(input("Podaj część urojoną pierwszej liczby: "))

# Pobieranie danych dla drugiej liczby zespolonej
b_re = float(input("Podaj część rzeczywistą drugiej liczby: "))
b_im = float(input("Podaj część urojoną drugiej liczby: "))

# Tworzenie liczb zespolonych
z1 = complex(a_re, a_im)
z2 = complex(b_re, b_im)

# Operacje
suma = z1 + z2
roznica = z1 - z2
iloczyn = z1 * z2

# Dzielenie z zabezpieczeniem
if z2 != 0:
    iloraz = z1 / z2
else:
    iloraz = "Nie można dzielić przez 0"

# Wyświetlanie wyników
print(f"\nPierwsza liczba: {z1}")
print(f"Druga liczba: {z2}")
print(f"Suma: {suma}")
print(f"Różnica: {roznica}")
print(f"Iloczyn: {iloczyn}")
print(f"Iloraz: {iloraz}")


