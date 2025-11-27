# Pobieranie liczb od użytkownika
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

# Obliczenia
suma = a + b
roznica = a - b
iloczyn = a * b

# Dzielenie z zabezpieczeniem przed dzieleniem przez 0
if b != 0:
    iloraz = a / b
else:
    iloraz = "Nie można dzielić przez 0"

# Wyświetlanie wyników
print(f"Suma: {suma}")
print(f"Różnica: {roznica}")
print(f"Iloczyn:", iloczyn)
print(f"Iloraz: {iloraz}")
