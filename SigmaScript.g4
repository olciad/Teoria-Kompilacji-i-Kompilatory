// Plik: SigmaScript.g4
grammar SigmaScript;

// ==========================================
// PUNKT 5: GRAMATYKA (PARSER)
// ==========================================

// glowna regula programu - program to instrukcje i znak konca pliku
program: instrukcja* EOF ;

// czym jest instrukcja
instrukcja: polecenie_ruchu
          | polecenie_obrotu
          | petla
          | instrukcja_warunkowa
          | wypisanie
          | przypisanie
          ;

// konkretne instrukcje
polecenie_ruchu: NAPRZOD wyrazenie ;
polecenie_obrotu: OBROC wyrazenie ;

petla: POWTORZ wyrazenie L_KLAMRA instrukcja* P_KLAMRA ;

instrukcja_warunkowa: JEZELI L_NAWIAS warunek P_NAWIAS L_KLAMRA instrukcja* P_KLAMRA (INACZEJ L_KLAMRA instrukcja* P_KLAMRA)? ;

wypisanie: WYPISZ (wyrazenie | TEKST) ;

przypisanie: USTAW IDENT PRZYPIS wyrazenie ;

// obsluga warunkow logicznych
warunek: wyrazenie operator_rel wyrazenie
       | warunek (ORAZ | LUB) warunek
       ;

operator_rel: ROWNY | MNIEJSZY | WIEKSZY ;

// wyrazenia matematyczne (ANTLR radzi sobie z kolejnoscia dzialan)
wyrazenie: wyrazenie (RAZY | PRZEZ) wyrazenie
         | wyrazenie (PLUS | MINUS) wyrazenie
         | LICZBA
         | IDENT
         | L_NAWIAS wyrazenie P_NAWIAS
         ;


// ==========================================
// PUNKT 4: TOKENY (LEXER)
// ==========================================

// slowa kluczowe
NAPRZOD: 'naprzod';
OBROC: 'obroc';
POWTORZ: 'powtorz';
JEZELI: 'jezeli';
INACZEJ: 'inaczej';
WYPISZ: 'wypisz';
USTAW: 'ustaw';

// operatory logiczne
ORAZ: 'oraz';
LUB: 'lub';

// operatory
PLUS: '+';
MINUS: '-';
RAZY: '*';
PRZEZ: '/';
PRZYPIS: '=';
ROWNY: '==';
MNIEJSZY: '<';
WIEKSZY: '>';

// separatory
L_NAWIAS: '(';
P_NAWIAS: ')';
L_KLAMRA: '{';
P_KLAMRA: '}';

// wartosci (wyrazenia regularne)
LICZBA: [0-9]+ ;
IDENT: [a-zA-Z_][a-zA-Z0-9_]* ;
TEKST: '"' ~'"'* '"' ; //akceptuje wszystko wewnatrz cudzyslowow

// ignorowanie bialych znakow i komentarzy
WS: [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;