// ==========================================
// SCENA: MAGICZNE KRÓLESTWO
// Skomplikowany pejzaż w SigmaScript
// ==========================================

// --- FUNKCJE POMOCNICZE (RUCH I STAN) ---

funkcja pusta przesun_w_prawo(rzeczywista krok) {
    podnies
    obroc 90.0
    naprzod krok
    obroc -90.0
    opusc
}

funkcja pusta przesun_w_lewo(rzeczywista krok) {
    podnies
    obroc -90.0
    naprzod krok
    obroc 90.0
    opusc
}

// --- NATURA ---

funkcja pusta drzewo_fraktalne(rzeczywista dlugosc, calkowita poziom) {
    jezeli (poziom == 0) {
        zwroc
    }

    naprzod dlugosc

    // Prawa gałąź
    obroc 25.0
    drzewo_fraktalne(dlugosc * 0.75, poziom - 1)

    // Lewa gałąź
    obroc (0.0 - 50.0)
    drzewo_fraktalne(dlugosc * 0.75, poziom - 1)

    // Powrót do pionu i na dół pnia
    obroc 25.0
    podnies
    obroc 180.0
    naprzod dlugosc
    obroc 180.0
    opusc
}

funkcja pusta trawa() {
    obroc 30.0
    naprzod 10.0
    obroc 180.0
    naprzod 10.0
    obroc 120.0
    naprzod 10.0
    obroc 180.0
    naprzod 10.0
    obroc (0.0 - 150.0)
}

// --- ZWIERZĘTA I NIEBO ---

funkcja pusta ptak() {
    obroc 60.0
    naprzod 15.0
    obroc 180.0
    naprzod 15.0
    obroc 60.0
    naprzod 15.0
    obroc 180.0
    naprzod 15.0
    obroc (0.0 - 120.0)
}

funkcja pusta slonce(rzeczywista wielkosc) {
    podnies
    naprzod wielkosc
    opusc
    powtorz 36 {
        naprzod wielkosc
        obroc 160.0
        naprzod wielkosc
        obroc (0.0 - 150.0)
    }
}

// --- ARCHITEKTURA (ZAMEK I ELEMENTY) ---

funkcja pusta blok_budynku(rzeczywista szer, rzeczywista wys) {
    powtorz 2 {
        naprzod wys
        obroc 90.0
        naprzod szer
        obroc 90.0
    }
}

funkcja pusta dach(rzeczywista szerokosc) {
    // Trójkąt równoboczny jako dach, powrót do punktu startu
    obroc 30.0
    naprzod szerokosc
    obroc 120.0
    naprzod szerokosc
    obroc 120.0
    naprzod szerokosc
    obroc 90.0
}

funkcja pusta zamek() {
    // 1. Główna wieża (centrum)
    blok_budynku(100.0, 150.0)

    // Dach głównej wiezy
    podnies
    naprzod 150.0
    opusc
    dach(100.0)
    podnies
    obroc 180.0
    naprzod 150.0
    obroc 180.0
    opusc

    // Drzwi do zamku
    przesun_w_prawo(30.0)
    blok_budynku(40.0, 50.0)
    przesun_w_lewo(30.0)


    podnies
    przesun_w_prawo(50.0)
    naprzod 50.0
    podnies
    naprzod 50.0
    opusc

    // Rozeta (ogromne, geometryczne okno witrażowe na głównej wieży)
    powtorz 12 {
        powtorz 3 {
            naprzod 15.0
            obroc 120.0
        }
        obroc 30.0
    }

    podnies
    obroc 180.0
    naprzod 100.0
    obroc 180.0
    przesun_w_lewo(50.0)
    opusc

    // 2. Lewa wieżyczka obronna
    przesun_w_lewo(60.0)
    blok_budynku(60.0, 100.0)

    podnies
    naprzod 100.0
    opusc
    dach(60.0)

    podnies
    obroc 180.0
    naprzod 100.0
    obroc 180.0
    opusc
    przesun_w_prawo(60.0)

    // 3. Prawa wieżyczka obronna
    przesun_w_prawo(100.0)
    blok_budynku(60.0, 100.0)

    podnies
    naprzod 100.0
    opusc
    dach(60.0)

    podnies
    obroc 180.0
    naprzod 100.0
    obroc 180.0
    opusc
    przesun_w_lewo(100.0)
}

// ==========================================
// SKRYPT GŁÓWNY - REŻYSERIA SCENY
// ==========================================

wypisz "Rozpoczynam malowanie epickiego pejzażu..."

// Rysowanie fundamentów i horyzontu
podnies
obroc (0.0 - 90.0)
naprzod 400.0
obroc 90.0
opusc

// Linia ziemi
obroc 90.0
naprzod 800.0
podnies
obroc 180.0
naprzod 470.0
obroc 90.0
opusc
// Powrót na idealny środek sceny, orientacja: góra

// Stawiamy zamek w samym centrum
zamek()
obroc -90.0
naprzod -70
obroc 90.0

// Sadzimy stary, gęsty las z lewej strony (bardzo głębokie fraktale)
przesun_w_lewo(200.0)
drzewo_fraktalne(60.0, 6)
przesun_w_lewo(120.0)
drzewo_fraktalne(45.0, 5)

// Sadzimy rzadszy lasek z prawej strony
podnies
obroc 90.0
naprzod 470.0
obroc (0.0 - 90.0)
opusc
drzewo_fraktalne(75.0, 6)
przesun_w_prawo(130.0)
drzewo_fraktalne(50.0, 5)

// Umieszczamy detale w postaci kęp trawy na ziemi
przesun_w_prawo(30.0)
trawa()
przesun_w_lewo(130.0)
trawa()
przesun_w_lewo(50.0)
trawa()
przesun_w_lewo(300.0)
trawa()
przesun_w_lewo(100.0) // omijamy zamek i idziemy na lewą stronę
trawa()
przesun_w_lewo(100.0)
trawa()

// Wysyłamy ptaki na niebo
podnies
naprzod 280.0
przesun_w_prawo(150.0)
opusc
ptak()

podnies
przesun_w_prawo(70.0)
podnies
naprzod 30.0
opusc
ptak()

podnies
przesun_w_prawo(60.0)
obroc 180.0
podnies
naprzod 50.0
obroc 180.0
opusc
ptak()

// Na koniec zawieszamy potężne, geometryczne słońce w lewym górnym rogu

przesun_w_lewo(250.0)
slonce(18.0)

wypisz "Scena gotowa! Zobacz na własne oczy wynik.svg!"