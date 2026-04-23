# Język do programowania dla uczniów szkół podstawowych
# 1. Autorzy
Aleksandra Dousa: adousa@student.agh.edu.pl

Paweł Czyżewski: czeski@student.agh.edu.pl

# 3. Założenia programu
## Ogólne cele programu: 
Stworzenie prostego, edukacyjnego języka programowania (wzorowanego na LOGO i środowiskach typu micro:bit), przeznaczonego dla dzieci w szkole podstawowej. Język będzie posiadał przyjazną i intuicyjną składnię, mającą na celu obniżenie progu wejścia przy nauce podstaw algorytmiki i logicznego myślenia.

## Rodzaj translatora: 
Kompilator

## Planowany wynik działania programu: 
Kompilator autorskiego języka edukacyjnego do kodu w języku C (konwerter source-to-source). Wygenerowany kod C będzie gotowy do skompilowania przez standardowe narzędzia (np. GCC) i uruchomienia.

## Planowany język implementacji: 
Python

## Sposób realizacji skanera/parsera: 
Użycie generatora skanerów i parserów: ANTLR4 w celu zautomatyzowania procesu analizy leksykalnej i syntaktycznej.

# 4. Opis Tokenów

| Kategoria      | Nazwa Tokena | Regex/Literal            | Opis                            |
|----------------|--------------|--------------------------|---------------------------------|
| Słowa kluczowe | NAPRZOD      | `naprzod`                | Ruch do przodu                  | 
|                | OBROC        | `obroc`                  | Obrót o kąt                     | 
|                | POWTORZ      | `powtorz`                | Pętla o stałej liczbie iteracji | 
|                | JEZELI       | `jezeli`                 | Instrukcja warunkowa            | 
|                | INACZEJ      | `inaczej`                | Alternatywa warunkowa           |
|                | WYPISZ       | `wypisz`                 | Wyświetlanie tekstu/wyniku      | 
|                | USTAW        | `ustaw`                  | Utowrzenie zmiennej             | 
| Operatory      | PLUS / MINUS | `+` / `-`                | Operacje arytmetyczne           | 
|                | RAZY / PRZEZ | `*` / `/`                | Mnożenie i dzielenie            | 
|                | PRZYPIS      | `=`                      | Operator przypisania            | 
|                | ROWNY        | `==`                     | Operator porównania             | 
|                | MNIEJSZY     | `<`                      | Relacja mniejszości             | 
|                | WIEKSZY      | `>`                      | Relacja większości              | 
|                | ORAZ         | `oraz`                   | Koniunkcja logiczna             |
|                | LUB          | `lub`                    | Alternatywa logiczna            |
| Separatory     | L_NAWIAS     | `(`                      | Początek wyrażenia/argumentów   | 
|                | P_NAWIAS     | `)`                      | Koniec wyrażenia/argumentów     | 
|                | L_KLAMRA     | `{`                      | Początek bloku kodu             | 
|                | P_KLAMRA     | `}`                      | Koniec bloku kodu               | 
| Wartości       | LICZBA       | `[0-9]+`                 | Liczby całkowite                | 
|                | IDENT        | `[a-zA-Z_][a-zA-Z0-9_]*` | Nazwy zmiennych                 | 
|                | TEKST        | `"[^"]*"`                | Napisy w cudzysłowie            | 
| Ignorowane     | BIALE_ZNAKI  | `[ \t\r\n]+`             | Spacje, taby, entery            |
|                | KOMENTARZ	   | `//.*`                   | Komentarze jednolinijkowe       |

# 5. Gramatyka
Gramatyka została zapisana w notacji generatora ANTLR4 
(z pominięciem reguł leksykalnych, które opisano w tabeli powyżej).

```antlr
program: instrukcja* EOF ;

instrukcja: polecenie_ruchu
          | polecenie_obrotu
          | petla
          | instrukcja_warunkowa
          | wypisanie
          | przypisanie
          ;

polecenie_ruchu: (NAPRZOD | NPRZ) wyrazenie ;
polecenie_obrotu: (OBROC | OBR) wyrazenie ;

petla: POWTORZ wyrazenie L_KLAMRA instrukcja* P_KLAMRA ;

instrukcja_warunkowa: JEZELI L_NAWIAS warunek P_NAWIAS L_KLAMRA instrukcja* P_KLAMRA (INACZEJ L_KLAMRA instrukcja* P_KLAMRA)? ;

wypisanie: WYPISZ (wyrazenie | TEKST) ;

przypisanie: USTAW IDENT PRZYPIS wyrazenie ;

warunek: wyrazenie operator_rel wyrazenie
       | warunek (ORAZ | LUB) warunek
       ;

operator_rel: ROWNY | MNIEJSZY | WIEKSZY ;

wyrazenie: wyrazenie (RAZY | PRZEZ) wyrazenie
         | wyrazenie (PLUS | MINUS) wyrazenie
         | LICZBA
         | IDENT
         | L_NAWIAS wyrazenie P_NAWIAS
         ;
```
# 6. Wymagania wstępne

- Python 3.8+
- ANTLR4 Python3 Runtime: Biblioteka niezbędna do zrozumienia składni języka.

Instalacja: ```pip install antlr4-python3-runtime```

- Kompilator C (np. GCC lub Clang)
- Biblioteka Standardowa C

# 7. 

# 8. Przykładowy program napisany w języku

``` ustaw kroki = 10
powtorz 4 {
    naprzod kroki
    obroc 90
}
wypisz "Kwadrat narysowany!"```
