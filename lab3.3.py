def kompresuj_rle(tekst):
    if not tekst.isascii():
        raise ValueError("Tekst zawiera znaki spoza ASCII.")

    if not tekst:  # jeśli pusty
        return ""

    wynik = ""
    aktualny_znak = tekst[0]
    licznik = 1

    for znak in tekst[1:]:
        if znak == aktualny_znak:
            licznik += 1
        else:
            wynik += aktualny_znak + str(licznik)
            aktualny_znak = znak
            licznik = 1

    # dodaj ostatni ciąg znaków
    wynik += aktualny_znak + str(licznik)
    return wynik
