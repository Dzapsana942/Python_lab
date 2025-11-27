Opis laboratoriów i zadań
LAB 1 – Operacje matematyczne
Zadanie 1

Program pobiera dwie liczby i oblicza:

sumę

różnicę

iloczyn

iloraz

Zadanie 2

Program pobiera dwie liczby zespolone (część rzeczywista + urojona), tworzy obiekty typu complex i oblicza podstawowe działania.

LAB 2 – Pętle, instrukcje warunkowe, obliczenia
Zadanie 1

Wyświetlenie pierwszych 10 liczb ciągu Fibonacciego.

Zadanie 2

Wyświetlenie choinki o zadanej wysokości zbudowanej ze znaków *.

Zadanie 3

Rozwiązanie równania kwadratowego

𝑎
𝑥
2
+
𝑏
𝑥
+
𝑐
=
0
ax
2
+bx+c=0

Obliczenie pierwiastków i wyświetlenie wyniku.

LAB 3 – Funkcje i operacje na kolekcjach
Zadanie 1

Funkcja zwracająca listę dzielników właściwych liczby.

Zadanie 2

Funkcja spłaszczająca listę zagnieżdżoną.
Walidacja: dopuszczalne są tylko liczby i listy → inaczej TypeError.

Zadanie 3

Kompresja napisu metodą RLE (“aaabbc” → “a3b2c1”).
Niedozwolone znaki poza ASCII → ValueError.

LAB 4 – Programowanie obiektowe (OOP)
Zadanie 1 – System biblioteczny

Klasy:

Książka: tytuł, autor, rok wydania

Biblioteka: dodawanie książek, wypożyczanie, wyświetlanie dostępnych pozycji

Zadanie 2 – Talia kart

Klasy:

Karta: kolor + wartość

Talia: tworzenie talii 52 kart, tasowanie, dobieranie kart
Z użyciem random.shuffle().

LAB 5 – Podstawy Pandas

Praca na pliku lab5.xlsx:

wczytywanie pliku Excel

filtrowanie i selekcja danych

grupowanie

podstawowe statystyki

sortowanie i analiza prostych zależności

LAB 6 – Analiza danych jakości powietrza (GIOŚ)

Na podstawie zestawów udostępnionych przez:
https://powietrze.gios.gov.pl/pjp/archives

Zakres:

wczytanie danych z pliku lab6.xlsx

wybór dwóch metryk jakości powietrza (np. PM10, SO₂)

filtrowanie, grupowanie i sortowanie danych

podstawowe pytania analityczne, np.:

które stacje mają najniższą kompletność pomiarów?

które miasta notują najwyższe średnie wartości metryk?

ile pomiarów przypada na poszczególne województwa?

Bez EDA, bez wizualizacji — tylko analiza tabelaryczna.

🛠️ Użyte technologie

Python 3.x

Pandas

NumPy

OpenPyXL

▶️ Jak uruchomić projekt

Instalacja pakietów:

pip install pandas numpy openpyxl


Uruchom wybrany skrypt:

python Lab3.2.py
