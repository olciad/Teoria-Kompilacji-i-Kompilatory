// 1. DEKLARACJE STRUKTUR
// Testuje tworzenie własnych typów danych złożonych z różnych typów wbudowanych.
struktura Dron {
    rzeczywista bateria
    logiczna w_powietrzu
}

// 2. DEKLARACJE FUNKCJI
// Funkcja przyjmująca naszą strukturę jako parametr i zwracająca wartość logiczną.
// Testuje wyrażenia logiczne i operatory relacyjne.
funkcja logiczna czy_moze_leciec(Dron d, rzeczywista koszt_ruchu) {
    // Rozdzielenie arytmetyki i logiki
    jezeli (d.bateria >= koszt_ruchu oraz d.w_powietrzu == prawda) {
        zwroc prawda
    } inaczej {
        zwroc falsz
    }
}

// 3. Glowny program
Dron moj_dron
ustaw moj_dron.bateria = 100.0
ustaw moj_dron.w_powietrzu = prawda

calkowita[4] trasa = [20, 30, 40, 50]
calkowita indeks = 0

wypisz "Rozpoczynam misje!"

dopoki (indeks < 4 oraz moj_dron.bateria > 0.0) {
    calkowita krok = trasa[indeks]
    rzeczywista koszt = 20.0

    jezeli (czy_moze_leciec(moj_dron, koszt) == prawda) {
        // Symulacja np. rysowania kwadratu po przylocie do punktu
        powtorz 4 {
            naprzod krok
            obroc 90
        }
        obroc 45 // Zmiana kierunku po kwadracie
        ustaw moj_dron.bateria = moj_dron.bateria - koszt
    } inaczej {
        ustaw moj_dron.w_powietrzu = falsz
    }

    ustaw indeks = indeks + 1
}

jezeli (moj_dron.w_powietrzu == falsz) {
    wypisz "Koniec baterii!"
}