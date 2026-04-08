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
Użycie generatora skanerów i parserów: PLY (Python Lex-Yacc) / ANTLR4 w celu zautomatyzowania procesu analizy leksykalnej i syntaktycznej.