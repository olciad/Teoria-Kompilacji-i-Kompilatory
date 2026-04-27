// 1. DEKLARACJE STRUKTUR
// Testuje tworzenie własnych typów danych złożonych z różnych typów wbudowanych.
struktura Dron {
    calkowita pozycja_x
    calkowita pozycja_y
    rzeczywista bateria
    logiczna w_powietrzu
}

// 2. DEKLARACJE FUNKCJI
// Funkcja przyjmująca naszą strukturę jako parametr i zwracająca wartość logiczną.
// Testuje wyrażenia logiczne i operatory relacyjne.
funkcja logiczna czy_moze_leciec(Dron d, rzeczywista koszt_ruchu) {
    // Rozdzielenie arytmetyki i logiki sprawdza się tu idealnie!
    jezeli (d.bateria >= koszt_ruchu oraz d.w_powietrzu == prawda) {
        zwroc prawda
    } inaczej {
        zwroc falsz
    }
}

// Funkcja wykonująca obliczenia matematyczne.
funkcja rzeczywista oblicz_koszt(calkowita dystans) {
    // Symulujemy, że każdy krok kosztuje 1.5 jednostki baterii
    zwroc dystans * 1.5
}

// 3. GŁÓWNY PROGRAM
// Deklaracja zmiennych z użyciem różnych typów i inicjalizacji.
wypisz "ROZPOCZECIE MISJI DRONA"

Dron moj_dron
ustaw moj_dron.pozycja_x = 0
ustaw moj_dron.pozycja_y = 0
ustaw moj_dron.bateria = 100.0
ustaw moj_dron.w_powietrzu = prawda

// Tablica symulująca trasę (kolejne odległości do pokonania)
calkowita[4] trasa = [20, 15, 30, 10]
calkowita indeks = 0

// Test pętli while (dopoki) z ułożonym warunkiem logicznym
dopoki (indeks < 4 oraz moj_dron.bateria > 0.0) {
    
    // Odczyt z tablicy i przypisanie do lokalnej zmiennej
    calkowita krok = trasa[indeks]
    rzeczywista koszt = oblicz_koszt(krok)
    
    wypisz "Planowany krok:"
    wypisz krok
    
    // Użycie funkcji w instrukcji warunkowej (wynik musi być logiczny)
    jezeli (czy_moze_leciec(moj_dron, koszt) == prawda) {
        
        wypisz "Wykonywanie ruchu..."
        
        // Pętla stała (powtorz) wewnątrz pętli warunkowej (dopoki)
        // Symulacja np. rysowania kwadratu po przylocie do punktu
        powtorz 4 {
            naprzod krok
            obroc 90
        }
        
        // Aktualizacja stanu struktury
        ustaw moj_dron.bateria = moj_dron.bateria - koszt
        ustaw moj_dron.pozycja_x = moj_dron.pozycja_x + krok
        
        wypisz "Pozostala bateria:"
        wypisz moj_dron.bateria
        
    } inaczej {
        wypisz "Blad: Zbyt niski poziom baterii na ten ruch!"
        ustaw moj_dron.w_powietrzu = falsz
    }
    
    // Inkrementacja indeksu pętli
    ustaw indeks = indeks + 1
}

wypisz "KONIEC MISJI"
jezeli (moj_dron.w_powietrzu == falsz) {
    wypisz "Dron awaryjnie wyladowal."
}