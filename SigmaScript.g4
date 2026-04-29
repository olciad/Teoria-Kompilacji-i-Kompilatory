// Plik: SigmaScript.g4
grammar SigmaScript;

// ==========================================
// PARSER
// ==========================================

// glowna regula programu - zero lub wiecej definicji (instrukcji, struktur, funkcji)
program: definicja* EOF ;

// definicja moze byc instrukcja, struktura, lub funkcja
definicja: instrukcja
         | definicja_struktury
         | definicja_funkcji
         ;

// struktury i funkcje
definicja_struktury: STRUKTURA IDENT L_KLAMRA deklaracja_zmiennej* P_KLAMRA ;
definicja_funkcji: FUNKCJA typ_zwracany IDENT L_NAWIAS parametry? P_NAWIAS blok_kodu ;

// parametry funkcji
parametry: parametr (PRZECINEK parametr)* ;
parametr: typ IDENT ;

// typy
typ_zwracany: typ | PUSTA ;
typ: (CALKOWITA | RZECZYWISTA | LOGICZNA | TEKST_TYP | IDENT) wymiar_tablicy? ;
wymiar_tablicy: L_KWADRAT LICZ_CALK? P_KWADRAT ;

// blok kodu
blok_kodu: L_KLAMRA instrukcja* P_KLAMRA ;

// instrukcje
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

// polecenia zolwia
polecenie_ruchu: NAPRZOD wyrazenie_arytmetyczne ;
polecenie_obrotu: OBROC wyrazenie_arytmetyczne ;

// petle
petla: POWTORZ wyrazenie_arytmetyczne blok_kodu ;
petla_warunkowa: DOPOKI L_NAWIAS wyrazenie_logiczne P_NAWIAS blok_kodu ;

// instrukcje warunkowe
instrukcja_warunkowa: JEZELI L_NAWIAS wyrazenie_logiczne P_NAWIAS blok_kodu (INACZEJ blok_kodu)? ;

// inne
wypisanie: WYPISZ wyrazenie_ogolne ;
deklaracja_zmiennej: typ IDENT (PRZYPIS wyrazenie_ogolne)? ;
przypisanie: USTAW odwolanie PRZYPIS wyrazenie_ogolne ;
instrukcja_zwrotu: ZWROC wyrazenie_ogolne? ;

// odwolanie, pozwala na: tablica[0].wspolrzedna_x
odwolanie: IDENT (L_KWADRAT wyrazenie_arytmetyczne P_KWADRAT | KROPKA IDENT)* ;

// wywolywanie funkcji
wywolanie_funkcji: IDENT L_NAWIAS argumenty? P_NAWIAS ;
argumenty: wyrazenie_ogolne (PRZECINEK wyrazenie_ogolne)* ;

// inicjalizacja tablicy
inicjalizacja_tablicy: L_KWADRAT argumenty? P_KWADRAT ;

// wyrazenie
wyrazenie_ogolne: wyrazenie_arytmetyczne
                | wyrazenie_logiczne
                | TEKST
                | inicjalizacja_tablicy
                ;

// wyraznenie logiczne
wyrazenie_logiczne: L_NAWIAS wyrazenie_logiczne P_NAWIAS
                  | PRAWDA
                  | FALSZ
                  | wywolanie_funkcji
                  | odwolanie
                  | wyrazenie_arytmetyczne operator_rel wyrazenie_arytmetyczne
                  | wyrazenie_logiczne (ROWNY | ROZNY) wyrazenie_logiczne
                  | NIE wyrazenie_logiczne
                  | wyrazenie_logiczne ORAZ wyrazenie_logiczne
                  | wyrazenie_logiczne LUB wyrazenie_logiczne
                  ;
operator_rel: ROWNY | ROZNY | MNIEJSZY | WIEKSZY | MNIEJ_ROWN | WIEC_ROWN ;

// wyrazenie arytmetyczne
wyrazenie_arytmetyczne: L_NAWIAS wyrazenie_arytmetyczne P_NAWIAS
                      | wywolanie_funkcji
                      | odwolanie
                      | LICZ_CALK
                      | LICZ_RZECZ
                      | wyrazenie_arytmetyczne (RAZY | PRZEZ) wyrazenie_arytmetyczne
                      | wyrazenie_arytmetyczne (PLUS | MINUS) wyrazenie_arytmetyczne
                      | MINUS wyrazenie_arytmetyczne
                      ;

// ==========================================
// LEKSER
// ==========================================

// typy danych
CALKOWITA: 'calkowita';
RZECZYWISTA: 'rzeczywista';
LOGICZNA: 'logiczna';
TEKST_TYP: 'tekst';
PUSTA: 'pusta';

// slowa kluczowe i narzedziowe
STRUKTURA: 'struktura';
FUNKCJA: 'funkcja';
ZWROC: 'zwroc';

// wartosci logiczne
PRAWDA: 'prawda';
FALSZ: 'falsz';

// instrukcje bazowe
NAPRZOD: 'naprzod';
OBROC: 'obroc';
POWTORZ: 'powtorz';
DOPOKI: 'dopoki';
JEZELI: 'jezeli';
INACZEJ: 'inaczej';
WYPISZ: 'wypisz';
USTAW: 'ustaw';

// operatory logiczne
ORAZ: 'oraz';
LUB: 'lub';
NIE: 'nie';

// operatory matematyczne i przypisania
PLUS: '+';
MINUS: '-';
RAZY: '*';
PRZEZ: '/';
PRZYPIS: '=';

// operatory relacyjne
ROWNY: '==';
ROZNY: '!=';
MNIEJ_ROWN: '<=';
WIEC_ROWN: '>=';
MNIEJSZY: '<';
WIEKSZY: '>';

// separatory
L_NAWIAS: '(';
P_NAWIAS: ')';
L_KLAMRA: '{';
P_KLAMRA: '}';
L_KWADRAT: '[';
P_KWADRAT: ']';
KROPKA: '.';
PRZECINEK: ',';

// wyrazenia regularne dla zmiennych i liczb
LICZ_CALK: [0-9]+ ;
LICZ_RZECZ: [0-9]+ '.' [0-9]+ ;
IDENT: [a-zA-Z_][a-zA-Z0-9_]* ;
TEKST: '"' ~'"'* '"' ;

// ignorowanie znakow i komentarze
WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;