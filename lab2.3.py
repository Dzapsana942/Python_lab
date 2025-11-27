import math  # importujemy funkcje matematyczne, np. pierwiastek

# Pobieramy dane od użytkownika
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

# Obliczamy deltę (czyli Δ)
delta = b**2 - 4 * a * c

# Sprawdzamy ile jest rozwiązań
if delta > 0:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Dwa pierwiastki: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Jedno rozwiązanie: x = {x}")
else:
    print("Brak pierwiastków rzeczywistych")

