# Język do programowania dla uczniów szkół podstawowych — SigmaScript
# 1. Autorzy
Aleksandra Dousa: adousa@student.agh.edu.pl

Paweł Czyżewski: czeski@student.agh.edu.pl

# 3. Założenia programu
## Ogólne cele programu: 
Stworzenie prostego, edukacyjnego języka programowania (wzorowanego na LOGO i środowiskach typu micro:bit), przeznaczonego dla dzieci w szkole podstawowej. Język będzie posiadał przyjazną i intuicyjną składnię, mającą na celu obniżenie progu wejścia przy nauce podstaw algorytmiki i logicznego myślenia.

## Rodzaj translatora: 
Kompilator

## Planowany wynik działania programu: 
Kompilator autorskiego języka edukacyjnego do kodu w języku C (konwerter source-to-source). Wygenerowany kod C będzie tworzył po uruchomieniu obrazek SVG na podstawie programu.

## Planowany język implementacji: 
Python

## Sposób realizacji skanera/parsera: 
Użycie generatora skanerów i parserów: ANTLR4 w celu zautomatyzowania procesu analizy leksykalnej i syntaktycznej.

# 4. Przykładowy program

```SigmaScript
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
```

# 5. Opis Tokenów

| **Kategoria** | **Nazwa Tokena** |  | **Opis** |
| --- | --- | --- | --- |
| Typy danych | CALKOWITA | `calkowita` | Liczba całkowita |
|  | RZECZYWISTA | `rzeczywista` | Liczba zmiennoprzecinkowa |
|  | LOGICZNA | `logiczna` | Wartość logiczna (prawda/fałsz) |
|  | TEKST_TYP | `tekst` | Typ znakowy / string |
|  | PUSTA | `pusta` | Typ pusty (void) do procedur |
| Wartości log. | PRAWDA | `prawda` | Stała logiczna: prawda |
|  | FALSZ | `falsz` | Stała logiczna: fałsz |
| Konstrukcje | STRUKTURA | `struktura` | Deklaracja własnego typu danych |
|  | FUNKCJA | `funkcja` | Deklaracja funkcji |
|  | ZWROC | `zwroc` | Zwrócenie wartości z funkcji |
| Słowa kluczowe | NAPRZOD | `naprzod` | Ruch do przodu (wbudowane) |
|  | OBROC | `obroc` | Obrót o kąt (wbudowane) |
|  | POWTORZ | `powtorz` | Pętla o stałej liczbie iteracji |
|  | DOPOKI | `dopoki` | Pętla warunkowa (while) |
|  | JEZELI | `jezeli` | Instrukcja warunkowa |
|  | INACZEJ | `inaczej` | Alternatywa warunkowa |
|  | WYPISZ | `wypisz` | Wyświetlanie tekstu/wyniku |
|  | USTAW | `ustaw` | Przypisanie nowej wartości |
| Operatory | PLUS / MINUS | `+` / `-` | Operacje arytmetyczne |
|  | RAZY / PRZEZ | `*` / `/` | Mnożenie i dzielenie |
|  | PRZYPIS | `=` | Operator przypisania |
|  | ROWNY | `==` | Operator porównania |
|  | ROZNY | `!=` | Operator różności |
|  | MNIEJSZY | `<` | Relacja mniejszości |
|  | WIEKSZY | `>` | Relacja większości |
|  | MNIEJ_ROWN | `<=` | Relacja mniejszy lub równy |
|  | WIEC_ROWN | `>=` | Relacja większy lub równy |
|  | ORAZ | `oraz` | Koniunkcja logiczna |
|  | LUB | `lub` | Alternatywa logiczna |
|  | NIE | `nie` | Negacja logiczna |
| Separatory | L_NAWIAS | `(` | Początek wyrażenia/argumentów |
|  | P_NAWIAS | `)` | Koniec wyrażenia/argumentów |
|  | L_KLAMRA | `{` | Początek bloku kodu |
|  | P_KLAMRA | `}` | Koniec bloku kodu |
|  | L_KWADRAT | `[` | Początek indeksu tablicy / listy |
|  | P_KWADRAT | `]` | Koniec indeksu tablicy / listy |
|  | KROPKA | `.` | Dostęp do pól struktury |
|  | PRZECINEK | `,` | Oddzielenie argumentów |
| Wartości | LICZ_CALK | `[0-9]+` | Literały całkowite |
|  | LICZ_RZECZ | `[0-9]+\.[0-9]+` | Literały rzeczywiste (z kropką) |
|  | IDENT | `[a-zA-Z_][a-zA-Z0-9_]*` | Nazwy zmiennych, funkcji, struktur |
|  | TEKST | `"[^"]*"` | Napisy w cudzysłowie |
| Ignorowane | BIALE_ZNAKI | `[ \t\r\n]+` | Spacje, taby, entery |
|  | KOMENTARZ | `//.*` | Komentarze jednolinijkowe |

# 6. Gramatyka
Gramatyka została zapisana w notacji generatora ANTLR4 
(z pominięciem reguł leksykalnych, które opisano w tabeli powyżej).

```antlr
program: definicja* EOF ;

// --- ELEMENTY GLOBALNE ---
definicja: instrukcja
         | definicja_struktury
         | definicja_funkcji
         ;

definicja_struktury: STRUKTURA IDENT L_KLAMRA deklaracja_zmiennej* P_KLAMRA ;

definicja_funkcji: FUNKCJA typ_zwracany IDENT L_NAWIAS parametry? P_NAWIAS blok_kodu ;

parametry: parametr (PRZECINEK parametr)* ;
parametr: typ IDENT ;

typ_zwracany: typ | PUSTA ;
typ: (CALKOWITA | RZECZYWISTA | LOGICZNA | TEKST_TYP | IDENT) wymiar_tablicy? ;
wymiar_tablicy: L_KWADRAT LICZ_CALK? P_KWADRAT ;

blok_kodu: L_KLAMRA instrukcja* P_KLAMRA ;

// --- INSTRUKCJE ---
instrukcja: polecenie_ruchu
          | polecenie_obrotu
          | petla
          | petla_warunkowa
          | instrukcja_warunkowa
          | wypisanie
          | deklaracja_zmiennej
          | przypisanie
          | instrukcja_zwrotu
          | wywolanie_funkcji
          ;

polecenie_ruchu: (NAPRZOD | NPRZ) wyrazenie_arytmetyczne ;
polecenie_obrotu: (OBROC | OBR) wyrazenie_arytmetyczne ;

// Petla for-like (powtorz n razy)
petla: POWTORZ wyrazenie_arytmetyczne blok_kodu ;

// Petla while-like (wymaga wyrazenia logicznego!)
petla_warunkowa: DOPOKI L_NAWIAS wyrazenie_logiczne P_NAWIAS blok_kodu ;

// Instrukcja if (wymaga wyrazenia logicznego!)
instrukcja_warunkowa: JEZELI L_NAWIAS wyrazenie_logiczne P_NAWIAS blok_kodu (INACZEJ blok_kodu)? ;

wypisanie: WYPISZ wyrazenie_ogolne ;

deklaracja_zmiennej: typ IDENT (PRZYPIS wyrazenie_ogolne)? ;
przypisanie: USTAW odwolanie PRZYPIS wyrazenie_ogolne ;
instrukcja_zwrotu: ZWROC wyrazenie_ogolne? ;

// --- ODWOLANIA I FUNKCJE ---
// Zmienna, element tablicy lub pole struktury (np. tablica[0].x)
odwolanie: IDENT (L_KWADRAT wyrazenie_arytmetyczne P_KWADRAT | KROPKA IDENT)* ;

wywolanie_funkcji: IDENT L_NAWIAS argumenty? P_NAWIAS ;
argumenty: wyrazenie_ogolne (PRZECINEK wyrazenie_ogolne)* ;

inicjalizacja_tablicy: L_KWADRAT argumenty P_KWADRAT ;

// --- WYRAZENIA (ROZDZIELENIE LOGIKI I ARYTMETYKI) ---
wyrazenie_ogolne: wyrazenie_arytmetyczne
                | wyrazenie_logiczne
                | TEKST
                | inicjalizacja_tablicy
                ;

// Tylko to moze wejsc do instrukcji JEZELI oraz DOPOKI
wyrazenie_logiczne: wyrazenie_arytmetyczne operator_rel wyrazenie_arytmetyczne
                  | wyrazenie_logiczne (ORAZ | LUB) wyrazenie_logiczne
                  | NIE wyrazenie_logiczne
                  | PRAWDA 
                  | FALSZ
                  | odwolanie          // jesli to zmienna boolowska
                  | wywolanie_funkcji  // jesli funkcja zwraca bool
                  | L_NAWIAS wyrazenie_logiczne P_NAWIAS
                  ;

operator_rel: ROWNY | ROZNY | MNIEJSZY | WIEKSZY | MNIEJ_ROWN | WIEC_ROWN ;

// Tradycyjne operacje matematyczne
wyrazenie_arytmetyczne: wyrazenie_arytmetyczne (RAZY | PRZEZ) wyrazenie_arytmetyczne
                      | wyrazenie_arytmetyczne (PLUS | MINUS) wyrazenie_arytmetyczne
                      | LICZ_CALK
                      | LICZ_RZECZ
                      | odwolanie          // jesli zmienna to liczba
                      | wywolanie_funkcji  // jesli funkcja zwraca liczbe
                      | L_NAWIAS wyrazenie_arytmetyczne P_NAWIAS
                      ;
```
# 7. Wymagania wstępne i instalacja

Aby poprawnie wygenerować parser, skompilować kod języka oraz uruchomić program docelowy, wymagane jest następujące oprogramowanie:

### Środowisko Python i ANTLR
- **Python 3.8+**
- **Java (JRE/JDK):** Wymagana pod spodem przez narzędzie ANTLR do generowania plików parsera.
- **antlr4-tools:** Oficjalne narzędzie do generowania klas z plików `.g4`.
- **antlr4-python3-runtime:** Biblioteka w Pythonie niezbędna do analizy drzewa składniowego (AST) i działania naszego Visitora.

**Instalacja pakietów Python:**
```bash
pip install antlr4-tools antlr4-python3-runtime
```

### Środowisko C

* Kompilator C: np. GCC lub Clang.

* Biblioteka matematyczna: Wygenerowany kod w języku C korzysta z biblioteki <math.h> (funkcje sin, cos) do obliczania wektorów ruchu żółwia/drona.

Ważna uwaga dotycząca kompilacji w C: Podczas kompilowania pliku `wynik.c` na systemach Linux/macOS, należy pamiętać o dodaniu flagi `-lm` w celu zlinkowania biblioteki matematycznej:

```bash
gcc wynik.c -o rysownik -lm
```