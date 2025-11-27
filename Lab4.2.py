import random  # potrzebne do tasowania kart

class Karta:
    def __init__(self, rodzaj, wartosc):
        self.rodzaj = rodzaj
        self.wartosc = wartosc

    def __str__(self):
        return f"{self.wartosc} {self.rodzaj}"


class Talia:
    def __init__(self):
        self.karty = []

    def przetasuj(self):
        kolory = ["Kier", "Karo", "Trefl", "Pik"]
        wartosci = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.karty = [Karta(rodzaj, wartosc) for rodzaj in kolory for wartosc in wartosci]
        random.shuffle(self.karty)
        print("Talia została przetasowana.")

    def rozdaj(self):
        if self.karty:
            return self.karty.pop()  # zabiera ostatnią kartę z listy
        else:
            return "Brak kart w talii!"


# 🔍 Test działania:
talia = Talia()
talia.przetasuj()

print("Rozdane karty:")
for _ in range(5):  # rozdajemy 5 kart
    karta = talia.rozdaj()
    print("-", karta)
