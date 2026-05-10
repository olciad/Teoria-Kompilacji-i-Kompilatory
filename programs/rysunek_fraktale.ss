// =======================================================================
// PROGRAM: Fraktalna Mandala Kocha
// Opis: Generuje skomplikowany wzór symetryczny, wykorzystując rekurencję
// do rysowania drzew fraktalnych oraz krzywych Kocha.
// =======================================================================

// 1. STRUKTURY DANYCH
// Struktura trzymająca zmienne konfiguracyjne dla drzewa fraktalnego
struktura ParametryDrzewa {
    rzeczywista dlugosc_pocz
    calkowita maks_iteracji
    rzeczywista kat_odchylenia
    rzeczywista wspolczynnik_skali
}

// Struktura organizująca ustawienia głównej sceny rysowania
struktura KonfiguracjaSceny {
    calkowita ilosc_elementow
    logiczna rysuj_sniezynki
    logiczna wysoki_detal
}

// 2. FUNKCJE REKURENCYJNE
// Funkcja używająca rekurencji do narysowania pojedynczego drzewa fraktalnego
funkcja pusta rysuj_drzewo(rzeczywista dlugosc, calkowita iteracja, ParametryDrzewa parametry) {
    jezeli (iteracja == 0) {
        zwroc
    }

    // Rysujemy główny pień/gałąź
    naprzod dlugosc

    // Obliczamy nową długość dla mniejszych gałęzi
    rzeczywista nowa_dlugosc = dlugosc * parametry.wspolczynnik_skali

    // Przejście w lewą stronę
    obroc (0.0 - parametry.kat_odchylenia)
    rysuj_drzewo(nowa_dlugosc, iteracja - 1, parametry)

    // Powrót do osi i przejście w prawą stronę (2 * kąt odchylenia)
    obroc (parametry.kat_odchylenia * 2.0)
    rysuj_drzewo(nowa_dlugosc, iteracja - 1, parametry)

    // Powrót do wyrównania gałęzi
    obroc (0.0 - parametry.kat_odchylenia)

    // Cofnięcie żółwia do początku tej gałęzi (ponieważ nie mamy funkcji 'podnieś pisak')
    obroc 180.0
    naprzod dlugosc
    obroc 180.0
}

// Funkcja generująca pojedynczą krawędź śnieżynki Kocha (krzywa Kocha)
funkcja pusta krzywa_kocha(rzeczywista dlugosc, calkowita iteracja) {
    jezeli (iteracja == 0) {
        naprzod dlugosc
    } inaczej {
        rzeczywista porcja = dlugosc / 3.0

        krzywa_kocha(porcja, iteracja - 1)
        obroc (0.0 - 60.0)

        krzywa_kocha(porcja, iteracja - 1)
        obroc 120.0

        krzywa_kocha(porcja, iteracja - 1)
        obroc (0.0 - 60.0)

        krzywa_kocha(porcja, iteracja - 1)
    }
}

// Funkcja składająca 3 krzywe w pełną śnieżynkę
funkcja pusta rysuj_sniezynke(rzeczywista bok, calkowita iteracja) {
    powtorz 3 {
        krzywa_kocha(bok, iteracja)
        obroc 120.0
    }
}

// 3. LOGIKA GŁÓWNA (Orkiestrator Sceny)
funkcja calkowita generuj_obraz(KonfiguracjaSceny scena) {
    wypisz "Trwa renderowanie skomplikowanego fraktala..."

    // Zadeklarowanie tablic uzywanych do konfiguracji pozycji na płótnie
    rzeczywista[] katy_obrotu = [0.0, 90.0, 180.0, 270.0]
    calkowita[] modyfikatory_wielkosci = [1, 2, 1, 2]

    // Inicjalizacja struktury parametrów drzewa
    ParametryDrzewa drzewo
    ustaw drzewo.dlugosc_pocz = 60.0
    ustaw drzewo.maks_iteracji = 4
    ustaw drzewo.kat_odchylenia = 30.0
    ustaw drzewo.wspolczynnik_skali = 0.7

    calkowita i = 0

    // Pętla warunkowa wykorzystująca tablice i operatory logiczne
    dopoki (i < scena.ilosc_elementow oraz nie (scena.ilosc_elementow > 4)) {
        wypisz "Rysuje symetryczny element numer:"
        wypisz i

        // Ustawienie żółwia w wybranym kierunku
        obroc katy_obrotu[i]

        // Logika sterująca poziomem skomplikowania w oparciu o tablicę
        jezeli (scena.wysoki_detal lub modyfikatory_wielkosci[i] == 2) {
            ustaw drzewo.maks_iteracji = 5
            ustaw drzewo.dlugosc_pocz = 75.0
        } inaczej {
            ustaw drzewo.maks_iteracji = 4
            ustaw drzewo.dlugosc_pocz = 60.0
        }

        // 1. Rysujemy drzewo
        rysuj_drzewo(drzewo.dlugosc_pocz, drzewo.maks_iteracji, drzewo)

        // 2. Rysujemy śnieżynkę na samym końcu ramienia
        jezeli (scena.rysuj_sniezynki) {
            naprzod 140.0 // odsunięcie w głąb płótna
            rysuj_sniezynke(45.0, 3)
            obroc 180.0
            naprzod 140.0 // powrót żółwia na środek osi
            obroc 180.0
        }

        // Reset obrotu przed rozpoczęciem kolejnej iteracji
        obroc (0.0 - katy_obrotu[i])

        // Inkrementacja licznika
        ustaw i = i + 1
    }

    wypisz "Zakonczono generowanie bazowe."
    zwroc 1
}

// =======================================================================
// 4. PUNKT STARTOWY PROGRAMU (MAIN)
// =======================================================================
wypisz "=== Witaj w SigmaScript System ==="
wypisz "Konfiguruje obszar roboczy..."

// Konstrukcja głównej zmiennej strukturalnej na bazie definicji
KonfiguracjaSceny ust_sceny
ustaw ust_sceny.ilosc_elementow = 4
ustaw ust_sceny.rysuj_sniezynki = prawda
ustaw ust_sceny.wysoki_detal = prawda

// Przesunięcie żółwia z domyślnego lewego górnego/środkowego punktu
// - zrobienie miejsca na duży, symetryczny rysunek.
obroc 90.0
naprzod 50.0
obroc (0.0 - 90.0)

// Oddelegowanie procesu do funkcji głównej
calkowita status_wykonania = generuj_obraz(ust_sceny)

jezeli (status_wykonania == 1) {
    wypisz "Obraz zostal wygenerowany."
    wypisz "Dodawanie ozdobnej ramki zewnetrznej..."

    // Rysowanie zamykającej ramki (wymusza ruch do krawędzi)
    obroc (0.0 - 90.0)
    naprzod 350.0
    obroc 90.0
    powtorz 4 {
        naprzod 700.0
        obroc 90.0
    }
} inaczej {
    wypisz "Blad! Zgloszono problem podczas tworzenia fraktala."
}

wypisz "Operacja rysowania przebiegla z sukcesem (Koniec Skryptu)."