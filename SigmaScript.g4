// Plik: SigmaScript.g4
grammar SigmaScript;

// ==========================================
// PARSER (GRAMATYKA)
// ==========================================

// Glowna regula programu - program sklada sie z definicji (instrukcji, struktur, funkcji)
program: definicja* EOF ;

definicja: instrukcja
         | definicja_struktury
         | definicja_funkcji
         ;

// --- STRUKTURY I FUNKCJE ---
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

// Wbudowane polecenia dla robota/zółwia
polecenie_ruchu: NAPRZOD wyrazenie_arytmetyczne ;
polecenie_obrotu: OBROC wyrazenie_arytmetyczne ;

// Petle
petla: POWTORZ wyrazenie_arytmetyczne blok_kodu ;
petla_warunkowa: DOPOKI L_NAWIAS wyrazenie_logiczne P_NAWIAS blok_kodu ;

// Instrukcje warunkowe (wymaga wyrazenia logicznego)
instrukcja_warunkowa: JEZELI L_NAWIAS wyrazenie_logiczne P_NAWIAS blok_kodu (INACZEJ blok_kodu)? ;

// Inne
wypisanie: WYPISZ wyrazenie_ogolne ;
deklaracja_zmiennej: typ IDENT (PRZYPIS wyrazenie_ogolne)? ;
przypisanie: USTAW odwolanie PRZYPIS wyrazenie_ogolne ;
instrukcja_zwrotu: ZWROC wyrazenie_ogolne? ;

// --- ODWOLANIA I FUNKCJE ---
// Pozwala np. na: tablica[0].wspolrzedna_x
odwolanie: IDENT (L_KWADRAT wyrazenie_arytmetyczne P_KWADRAT | KROPKA IDENT)* ;

wywolanie_funkcji: IDENT L_NAWIAS argumenty? P_NAWIAS ;
argumenty: wyrazenie_ogolne (PRZECINEK wyrazenie_ogolne)* ;

inicjalizacja_tablicy: L_KWADRAT argumenty? P_KWADRAT ;

// --- WYRAZENIA ---
wyrazenie_ogolne: wyrazenie_arytmetyczne
                | wyrazenie_logiczne
                | TEKST
                | inicjalizacja_tablicy
                ;

// Wyrazenia logiczne (z zachowaniem priorytetow od gory do dolu)
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

// Wyrazenia arytmetyczne (z zachowaniem priorytetow matematycznych)
wyrazenie_arytmetyczne: L_NAWIAS wyrazenie_arytmetyczne P_NAWIAS
                      | wywolanie_funkcji
                      | odwolanie
                      | LICZ_CALK
                      | LICZ_RZECZ
                      | wyrazenie_arytmetyczne (RAZY | PRZEZ) wyrazenie_arytmetyczne
                      | wyrazenie_arytmetyczne (PLUS | MINUS) wyrazenie_arytmetyczne
                      ;

// ==========================================
// LEXER (TOKENY)
// ==========================================

// --- Typy danych ---
CALKOWITA: 'calkowita';
RZECZYWISTA: 'rzeczywista';
LOGICZNA: 'logiczna';
TEKST_TYP: 'tekst';
PUSTA: 'pusta';

// --- Slowa kluczowe narzedziowe ---
STRUKTURA: 'struktura';
FUNKCJA: 'funkcja';
ZWROC: 'zwroc';

// --- Wartosci logiczne ---
PRAWDA: 'prawda';
FALSZ: 'falsz';

// --- Instrukcje bazowe ---
NAPRZOD: 'naprzod';
OBROC: 'obroc';
POWTORZ: 'powtorz';
DOPOKI: 'dopoki';
JEZELI: 'jezeli';
INACZEJ: 'inaczej';
WYPISZ: 'wypisz';
USTAW: 'ustaw';

// --- Operatory logiczne ---
ORAZ: 'oraz';
LUB: 'lub';
NIE: 'nie';

// --- Operatory matematyczne i przypisania ---
PLUS: '+';
MINUS: '-';
RAZY: '*';
PRZEZ: '/';
PRZYPIS: '=';

// --- Operatory relacyjne ---
ROWNY: '==';
ROZNY: '!=';
MNIEJ_ROWN: '<=';
WIEC_ROWN: '>=';
MNIEJSZY: '<';
WIEKSZY: '>';

// --- Separatory ---
L_NAWIAS: '(';
P_NAWIAS: ')';
L_KLAMRA: '{';
P_KLAMRA: '}';
L_KWADRAT: '[';
P_KWADRAT: ']';
KROPKA: '.';
PRZECINEK: ',';

// --- Wyrazenia regularne dla zmiennych i stalych ---
LICZ_CALK: [0-9]+ ;
LICZ_RZECZ: [0-9]+ '.' [0-9]+ ;
IDENT: [a-zA-Z_][a-zA-Z0-9_]* ;
TEKST: '"' ~'"'* '"' ; // Akceptuje wszystko wewnatrz cudzyslowow

// --- Ignorowanie znakow i komentarze ---
WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;