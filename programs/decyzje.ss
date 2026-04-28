// 1. Zmienne
calkowita dlugosc_boku = 150
logiczna czy_rysujemy_kwadrat = falsz

// 2. Prosty warunek z użyciem zmiennej
jezeli (czy_rysujemy_kwadrat == prawda oraz dlugosc_boku > 100) {
    // Rysuje kwadrat
    powtorz 4 {
        naprzod dlugosc_boku
        obroc 90
    }
} inaczej {
    // Rysuje trójkąt, używając operatorów matematycznych
    powtorz 3 {
        naprzod dlugosc_boku / 2
        obroc 120
    }
}