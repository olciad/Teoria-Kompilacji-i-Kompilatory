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
