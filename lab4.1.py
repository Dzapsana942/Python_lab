class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def __str__(self):
        return f"{self.tytul} – {self.autor} ({self.rok_wydania})"


class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)
        print(f"Dodano książkę: {ksiazka}")

    def wypozycz_ksiazke(self, tytul):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul.lower() == tytul.lower():
                self.ksiazki.remove(ksiazka)
                print(f"Wypożyczono książkę: {ksiazka}")
                return
        print(f"Książka o tytule '{tytul}' nie jest dostępna.")

    def wyswietl_ksiazki(self):
        if not self.ksiazki:
            print("Brak dostępnych książek w bibliotece.")
        else:
            print("Dostępne książki w bibliotece:")
            for ksiazka in self.ksiazki:
                print("-", ksiazka)


# Przykładowe użycie
biblioteka = Biblioteka()

k1 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", 1834)
k2 = Ksiazka("Lalka", "Bolesław Prus", 1890)
k3 = Ksiazka("Quo Vadis", "Henryk Sienkiewicz", 1896)

biblioteka.dodaj_ksiazke(k1)
biblioteka.dodaj_ksiazke(k2)
biblioteka.dodaj_ksiazke(k3)

biblioteka.wyswietl_ksiazki()

biblioteka.wypozycz_ksiazke("Lalka")

biblioteka.wyswietl_ksiazki()
