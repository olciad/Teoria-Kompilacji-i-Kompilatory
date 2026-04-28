// 1. Definicja funkcji
funkcja pusta rysuj_wielokat(calkowita ile_bokow, rzeczywista dlugosc) {
    rzeczywista kat = 360.0 / ile_bokow
    powtorz ile_bokow {
        naprzod dlugosc
        obroc kat
    }
}

// 2. Tablice i pętla warunkowa (WHILE)
calkowita[4] rozmiary = [40, 60, 80, 100]
calkowita indeks = 0

// Użycie pętli dopoki z warunkiem
dopoki (indeks < 4) {
    // Odczyt z tablicy i wywołanie naszej funkcji
    calkowita aktualny_rozmiar = rozmiary[indeks]

    rysuj_wielokat(6, aktualny_rozmiar)

    // Odsunięcie żółwia
    naprzod 10
    obroc 20

    // Inkrementacja
    ustaw indeks = indeks + 1
}