import sys
import re
from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from antlr_generated.SigmaScriptLexer import SigmaScriptLexer
from antlr_generated.SigmaScriptParser import SigmaScriptParser
from antlr_generated.SigmaScriptVisitor import SigmaScriptVisitor
from antlr4.error.ErrorListener import ErrorListener

# biblioteka runtime
RUNTIME_C = """#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// garbage collector dla tekstow
typedef struct StringNode {
    char* str;
    struct StringNode* next;
} StringNode;

StringNode* _string_pool = NULL;

void _rejestruj_tekst(char* str) {
    StringNode* node = (StringNode*)malloc(sizeof(StringNode));
    node->str = str;
    node->next = _string_pool;
    _string_pool = node;
}

// garbage collector dla tablic i struktur
typedef struct MemNode {
    void* ptr;
    struct MemNode* next;
} MemNode;

MemNode* _mem_pool = NULL;

void _rejestruj_pamiec(void* ptr) {
    if (!ptr) return;
    MemNode* node = (MemNode*)malloc(sizeof(MemNode));
    node->ptr = ptr;
    node->next = _mem_pool;
    _mem_pool = node;
}

void _wyczysc_pamiec() {
    // Sprzatanie tekstow
    StringNode* current_str = _string_pool;
    while (current_str != NULL) {
        StringNode* next = current_str->next;
        free(current_str->str);
        free(current_str);
        current_str = next;
    }
    // Sprzatanie tablic
    MemNode* current_mem = _mem_pool;
    while (current_mem != NULL) {
        MemNode* next = current_mem->next;
        free(current_mem->ptr);
        free(current_mem);
        current_mem = next;
    }
    _string_pool = NULL;
    _mem_pool = NULL;
}
//koniec gc

char* _polacz_teksty(const char* a, const char* b) {
    // alokujemy pamiec na nowy tekst
    char* wynik = (char*)malloc(strlen(a) + strlen(b) + 1);
    if (wynik != NULL) {
        strcpy(wynik, a);
        strcat(wynik, b);
        _rejestruj_tekst(wynik); // Automatycznie oddajemy pod opieke GC
    }
    return wynik;
}

float _x = 0.0; // teraz startujemy z (0, 0)
float _y = 0.0;
float _kat = -90.0; // -90 stopni -- patrzymy w gore
int _pisak_opuszczony = 1; // 1 = opuszczony (rysuje), 0 = podniesiony (nie rysuje)

void _podnies_pisak() {
    _pisak_opuszczony = 0;
}

void _opusc_pisak() {
    _pisak_opuszczony = 1;
}

// zmienne sledzace granice rysunku (bounding box)
float _min_x = 0.0;
float _max_x = 0.0;
float _min_y = 0.0;
float _max_y = 0.0;

// lista kierunkowa do trzymania listy instrukcji
typedef struct LineNode {
    float x1, y1, x2, y2;
    struct LineNode* next;
} LineNode;

LineNode* _lines_head = NULL;
LineNode* _lines_tail = NULL;

void _init_svg() {
    // wartosci startowe
    _min_x = _x;
    _max_x = _x;
    _min_y = _y;
    _max_y = _y;
}

void _zapisz_svg() {
    FILE *svg_file = fopen("wynik.svg", "w");
    if (!svg_file) return;

    // dodajemy margines
    float padding = 20.0;
    float v_min_x = _min_x - padding;
    float v_min_y = _min_y - padding;
    float v_width = (_max_x - _min_x) + (padding * 2);
    float v_height = (_max_y - _min_y) + (padding * 2);

    // zabezpieczenie gdy brak rusunku
    if (v_width <= 0) v_width = 10;
    if (v_height <= 0) v_height = 10;

    // tag svg z dynamicznymi wymiarami
    fprintf(svg_file, "<svg width=\\"%.2f\\" height=\\"%.2f\\" viewBox=\\"%.2f %.2f %.2f %.2f\\" xmlns=\\"http://www.w3.org/2000/svg\\">\\n", v_width, v_height, v_min_x, v_min_y, v_width, v_height);
    
    // rysujemy tlo
    fprintf(svg_file, "<rect x=\\"%.2f\\" y=\\"%.2f\\" width=\\"%.2f\\" height=\\"%.2f\\" fill=\\"#ffffff\\"/>\\n", v_min_x, v_min_y, v_width, v_height);

    // iterujemy po liniach i wrzucamy do pliku
    LineNode* current = _lines_head;
    while (current != NULL) {
        fprintf(svg_file, "<line x1=\\"%.2f\\" y1=\\"%.2f\\" x2=\\"%.2f\\" y2=\\"%.2f\\" stroke=\\"#2c3e50\\" stroke-width=\\"3\\" stroke-linecap=\\"round\\" />\\n",
                current->x1, current->y1, current->x2, current->y2);
        
        // zwalniamy pamiec
        LineNode* to_free = current;
        current = current->next;
        free(to_free);
    }

    fprintf(svg_file, "</svg>\\n");
    fclose(svg_file);
    _wyczysc_pamiec();
    printf("[+] Misja zakonczona. Wygenerowano plik wynik.svg!\\n");
}

void _naprzod(float dystans) {
    float rad = _kat * (3.14159265 / 180.0);
    float new_x = _x + dystans * cos(rad);
    float new_y = _y + dystans * sin(rad);

    if (_pisak_opuszczony){
        // wrzucamy linie do pamieci podrecznej 
        LineNode* node = (LineNode*)malloc(sizeof(LineNode));
        node->x1 = _x; node->y1 = _y; node->x2 = new_x; node->y2 = new_y;
        node->next = NULL;
    
        if (_lines_tail == NULL) {
            _lines_head = node;
            _lines_tail = node;
        } else {
            _lines_tail->next = node;
            _lines_tail = node;
        }
    }

    // sprawdzamy czy nie poszerzylismy granic
    if (new_x < _min_x) _min_x = new_x;
    if (new_x > _max_x) _max_x = new_x;
    if (new_y < _min_y) _min_y = new_y;
    if (new_y > _max_y) _max_y = new_y;

    // przesuwamy zolwia
    _x = new_x;
    _y = new_y;
}

void _obroc(float zmiana_kata) {
    _kat += zmiana_kata;
}

//ochrona przed dzieleniem przez zero
float _bezpieczne_dzielenie(float a, float b) {
    if (b == 0.0) {
        printf("[!] Ostrzeżenie: Próbowano podzielić przez zero! Wynik zamieniono na 0, aby program mógł działać dalej.\\n");
        return 0.0;
    }
    return a / b;
}
"""

class PolskiErrorListener(ErrorListener):
    def __init__(self):
        super(PolskiErrorListener, self).__init__()
        self.bledy = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # kolory do konsoli
        KOLOR_CZERWONY = '\033[91m'
        KOLOR_SZARY = '\033[90m'
        KOLOR_RESET = '\033[0m'

        znaki_pl = {
            "'{'": "klamry otwierającej '{'",
            "'}'": "klamry zamykającej '}'",
            "'('": "nawiasu otwierającego '('",
            "')'": "nawiasu zamykającego ')'",
            "'['": "nawiasu kwadratowego '['",
            "']'": "nawiasu kwadratowego ']'",
            "'='": "znaku równości '='",
            "','": "przecinka ','"
        }

        polska_wiadomosc = ""

        # zabezpieczenie przed naglym koncem pliku
        if "at '<EOF>'" in msg or "input '<EOF>'" in msg:
            # sprawdzamy czy brakuje nawiasu czy co innego
            if "'}'" in msg:
                polska_wiadomosc = "Plik skończył się niespodziewanie! Wygląda na to, że gdzieś wcześniej zapomniano zamknąć klamrę '}'."
            elif "')'" in msg:
                polska_wiadomosc = "Plik skończył się niespodziewanie! Wygląda na to, że brakuje nawiasu zamykającego ')'."
            else:
                polska_wiadomosc = "Kod urywa się nagle. Sprawdź, czy na pewno dokończono ostatnie polecenie."

        # blad tokenu
        elif msg.startswith("token recognition error"):
            match = re.search(r"at: '(.*?)'", msg)
            zly_znak = match.group(1) if match else "nieznany"
            polska_wiadomosc = f"Użyto znaku '{zly_znak}', którego ten język nie rozumie. Upewnij się, że nie używasz polskich znaków (np. ą, ę)."

        # brakujacy znak
        elif msg.startswith("missing "):
            match = re.search(r"missing (.*?) at", msg)
            if match:
                brakujacy_znak = match.group(1)
                przetlumaczony = znaki_pl.get(brakujacy_znak, f"elementu: {brakujacy_znak}")
                polska_wiadomosc = f"Wygląda na to, że brakuje {przetlumaczony}."

        # niezgodny znak
        elif msg.startswith("mismatched input "):
            match = re.search(r"expecting \{(.*?)}|expecting (.*)", msg)
            oczekiwane = ""
            if match:
                surowe_oczekiwane = match.group(1) if match.group(1) else match.group(2)
                for znak_ang, znak_pol in znaki_pl.items():
                    if znak_ang in surowe_oczekiwane:
                        oczekiwane = znak_pol
                        break
            if oczekiwane:
                polska_wiadomosc = f"Użyto niewłaściwego znaku. W tym miejscu spodziewano się {oczekiwane}."
            else:
                polska_wiadomosc = "Użyto niewłaściwego słowa lub znaku. Sprawdź, czy polecenie jest poprawnie napisane."

        # nadmiarowy znak
        elif msg.startswith("extraneous input "):
            polska_wiadomosc = "Ten znak lub słowo wydaje się tu niepotrzebne. Spróbuj je usunąć."

        # brak alternatywy
        elif msg.startswith("no viable alternative"):
            polska_wiadomosc = "Kompletnie nie rozumiem tego polecenia. Upewnij się, że zaczyna się od znanej instrukcji (np. ustaw, wypisz, jezeli)."

        else:
            polska_wiadomosc = "Coś poszło nie tak ze składnią, ale ciężko mi określić dokładnie co."

        #kolorowana wiadomosc
        blad = (
            f"{KOLOR_CZERWONY}Ups! Błąd w linii {line}, znak {column}: {polska_wiadomosc}{KOLOR_RESET}\n"
            f"{KOLOR_SZARY}   (Szczegóły dla zaawansowanych: {msg}){KOLOR_RESET}\n"
        )

        self.bledy.append(blad)
        print(blad)

class TabelaSymboli:
    def __init__(self):
        # stos slownikow do obslugi zasiegow
        self.stos_zasiegow = [{}]

    #wywolywane gdy wchodzimy do nawiasow
    def wejdz_do_bloku(self):
        self.stos_zasiegow.append({})

    #wywolywane gdy wychodzimy z nawiasow
    def wyjdz_z_bloku(self):
        if len(self.stos_zasiegow) > 1:
            self.stos_zasiegow.pop()

    #dodaje zmienna do obecnego bloku kodu
    def dodaj_zmienna(self, nazwa, typ, czy_tablica=False):
        obecny_zasieg = self.stos_zasiegow[-1]
        if nazwa in obecny_zasieg:
            return False  # rzucamy blad - zmienna juz istnieje w bloku

        obecny_zasieg[nazwa] = {'typ': typ, 'czy_tablica': czy_tablica}
        return True

    # szuka pelnych informacji o zmiennej
    def pobierz_zmienna(self, nazwa):
        for zasieg in reversed(self.stos_zasiegow):
            if nazwa in zasieg:
                return zasieg[nazwa]
        return None

    # szuka zmiennej od obecnego do globalnego bloku
    def pobierz_typ_zmiennej(self, nazwa):
        zmienna = self.pobierz_zmienna(nazwa)
        return zmienna['typ'] if zmienna else None

class KompilatorVisitor(SigmaScriptVisitor):
    def __init__(self):
        self.kod_struktur = []
        self.prototypy_funkcji = [] #na prototypy funkcji
        self.kod_globalny = [] #na funkcje i struktury
        self.kod_main = [] #na cala reszte
        self.w_funkcji = False
        self.oczekiwany_typ_zwracany = None

        # tabela symboli, rejestr struktur, rejestr funkcji i tablica bledow semantycznych
        self.symbole = TabelaSymboli()
        self.definicje_struktur = {}
        self.zadeklarowane_funkcje = {}
        self.bledy_semantyczne = []
        self.czy_zwrocono_wartosc = False

    def zglos_blad(self, ctx, wiadomosc):
        if ctx and hasattr(ctx, 'start'):
            linia = ctx.start.line
            kolumna = ctx.start.column
            blad = f"[!] Błąd logiczny (linia {linia}, kolumna {kolumna}): {wiadomosc}"
        else:
            blad = f"[!] Błąd logiczny: {wiadomosc}"

        if blad not in self.bledy_semantyczne:
            self.bledy_semantyczne.append(blad)

    def dodaj_kod(self, linia):
        if self.w_funkcji:
            self.kod_globalny.append(linia)
        else:
            self.kod_main.append(linia)

    def rozpoznawanie_typow(self, typ_bazowy):
        """Mapuje typy z języka SigmaScript na odpowiedniki w języku C."""
        if typ_bazowy == "calkowita":
            return "int"
        elif typ_bazowy == "rzeczywista":
            return "float"
        elif typ_bazowy == "logiczna":
            return "int"
        elif typ_bazowy == "tekst":
            return "char*"
        elif typ_bazowy == "pusta":
            return "void"
        else:
            # zwracamy oryginalna nazwe dla obiektow struktur
            return typ_bazowy

    # weryfikacja odwolan do pol struktur
    def weryfikuj_odwolanie(self, ctx: SigmaScriptParser.OdwolanieContext):
        glowna_zmienna = ctx.IDENT(0).getText()
        info_zmiennej = self.symbole.pobierz_zmienna(glowna_zmienna)

        # jesli zmienna nie istnieje - zglaszamy blad
        if not info_zmiennej:
            self.zglos_blad(ctx, f"Użyto zmiennej '{glowna_zmienna}', która nie została wcześniej zadeklarowana!")
            return

        obecny_typ = info_zmiennej['typ']
        czy_tablica = info_zmiennej['czy_tablica']
        poprzedni_element = glowna_zmienna

        # przechodzimy po AST znak po znaku
        for i in range(1, ctx.getChildCount()):
            znak = ctx.getChild(i).getText()

            if znak == '[':
                # napotkalismy nawiasy kwadratowe
                if czy_tablica:
                    czy_tablica = False  # zdjemujemy wymiar
                elif obecny_typ == 'tekst':
                    pass  # jak tekst to ok
                else:
                    self.zglos_blad(ctx,
                                    f"Próba użycia indeksu '[' na zmiennej '{poprzedni_element}', która nie jest tablicą!")
                    return

            elif znak == ']':
                pass  # ignorujemy zamkniecie nawiasu

            elif znak == '.':
                # proba wywolania pola na calej tablicy
                if czy_tablica:
                    self.zglos_blad(ctx,
                                    f"Próba odwołania do pola struktury z całej tablicy '{poprzedni_element}'. Brakuje indeksu, np. '{poprzedni_element}[0]'!")
                    return

            elif ctx.getChild(i - 1).getText() == '.':
                # jesli wczesniej byla kropka to znak jest nazwa pola
                nazwa_pola = znak

                # czy to na pewno struktura
                if obecny_typ not in self.definicje_struktur:
                    self.zglos_blad(ctx,
                                    f"Element '{poprzedni_element}' (typu {obecny_typ}) nie jest strukturą i nie posiada pól!")
                    return

                struktura = self.definicje_struktur[obecny_typ]

                # czy pole istnieje w strukturze
                if nazwa_pola not in struktura:
                    self.zglos_blad(ctx, f"Struktura '{obecny_typ}' nie posiada pola o nazwie '{nazwa_pola}'!")
                    return

                # aktualizujemy parametry na to czym jest aktualne pole
                obecny_typ = struktura[nazwa_pola]['typ_bazowy']
                czy_tablica = struktura[nazwa_pola]['czy_tablica']
                poprzedni_element = nazwa_pola

    def tlumacz_wyrazenie(self, ctx):

        if ctx is None:
            return ""

        # zabezpieczenie przed dzieleniem przez zero w wyrazeniach i konkatenacja tekstow
        if isinstance(ctx, SigmaScriptParser.Wyrazenie_arytmetyczneContext):
            # najpierw pobieramy typy obu stron
            lewe_ctx = ctx.wyrazenie_arytmetyczne(0)
            prawe_ctx = ctx.wyrazenie_arytmetyczne(1) if ctx.getChildCount() > 2 else None

            typ_lewe = self.pobierz_typ_wyrazenia(lewe_ctx)
            typ_prawe = self.pobierz_typ_wyrazenia(prawe_ctx) if prawe_ctx else None

            # blokujemy odejmnowanie mnozenie i dzielenie dla tekstow
            if (ctx.MINUS() or ctx.RAZY() or ctx.PRZEZ()) and (typ_lewe == 'tekst' or typ_prawe == 'tekst'):
                self.zglos_blad(ctx, "Nie można odejmować, mnożyć ani dzielić tekstów!")
                return "\"\""  # zwracamy cos

            if ctx.PRZEZ():
                # tlumaczymy lewa i prawa strone
                lewe = self.tlumacz_wyrazenie(ctx.wyrazenie_arytmetyczne(0))
                prawe = self.tlumacz_wyrazenie(ctx.wyrazenie_arytmetyczne(1))
                # wywolujemy bezpieczne dzielenie
                return f"_bezpieczne_dzielenie((float)({lewe}), (float)({prawe}))"

            if ctx.PLUS():
                # jesli obie tekst, to konkatenacja
                if typ_lewe == 'tekst' and typ_prawe == 'tekst':
                    lewy_kod = self.tlumacz_wyrazenie(lewe_ctx)
                    prawy_kod = self.tlumacz_wyrazenie(prawe_ctx)
                    return f"_polacz_teksty({lewy_kod}, {prawy_kod})"
                # blokada dodania tekstu do liczby
                elif typ_lewe == 'tekst' or typ_prawe == 'tekst':
                    self.zglos_blad(ctx, "Nie można dodawać tekstu do liczb!")
                    return "\"\""

        # porownywanie tekstow z strcmp
        if isinstance(ctx, SigmaScriptParser.Wyrazenie_logiczneContext):
            if ctx.ROWNY() or ctx.ROZNY():
                lewe_ctx = ctx.wyrazenie_logiczne(0)
                prawe_ctx = ctx.wyrazenie_logiczne(1)

                typ_lewe = self.pobierz_typ_wyrazenia(lewe_ctx)
                typ_prawe = self.pobierz_typ_wyrazenia(prawe_ctx)

                #lista bezpiecznych typow
                dozwolone_typy = ['calkowita', 'rzeczywista', 'logiczna', 'tekst', 'znak']

                # jesli typ niebazowy
                if typ_lewe not in dozwolone_typy or typ_prawe not in dozwolone_typy:
                    self.zglos_blad(ctx,
                                    f"Nie można bezpośrednio porównywać tablic ani struktur (próbowano porównać '{typ_lewe}' z '{typ_prawe}'). Porównuj ich konkretne elementy lub pola!")
                    return "0"

                # rzutujemy == i != na strcmp dla tekstow
                if typ_lewe == 'tekst' and typ_prawe == 'tekst':
                    lewe_kod = self.tlumacz_wyrazenie(lewe_ctx)
                    prawe_kod = self.tlumacz_wyrazenie(prawe_ctx)
                    if ctx.ROWNY():
                        return f"(strcmp({lewe_kod}, {prawe_kod}) == 0)"
                    else:
                        return f"(strcmp({lewe_kod}, {prawe_kod}) != 0)"

        # weryfikacja czy wywolywana funkcja istnieje
        if isinstance(ctx, SigmaScriptParser.Wywolanie_funkcjiContext):
            nazwa_funkcji = ctx.IDENT().getText()

            # weryfikacja z uzyciem slownika
            if nazwa_funkcji not in self.zadeklarowane_funkcje:
                self.zglos_blad(ctx, f"Próba wywołania nieznanej funkcji '{nazwa_funkcji}'!")
            else:
                # weryfikacja liczby argumentow
                lista_argumentow = ctx.argumenty().wyrazenie_ogolne() if ctx.argumenty() else []
                podane_argumenty = len(lista_argumentow)
                oczekiwane_argumenty = self.zadeklarowane_funkcje[nazwa_funkcji]['parametry']
                if podane_argumenty != oczekiwane_argumenty:
                    self.zglos_blad(ctx,
                                    f"Funkcja '{nazwa_funkcji}' oczekuje {oczekiwane_argumenty} argumentów, a podano {podane_argumenty}!")
                else:
                    # weryfikacja typow argumentow w pętli
                    oczekiwane_typy = self.zadeklarowane_funkcje[nazwa_funkcji]['typy_parametrow']

                    for i in range(podane_argumenty):
                        # obliczamy typ wyrazenia
                        podany_typ = self.pobierz_typ_wyrazenia(lista_argumentow[i])
                        oczekiwany_typ = oczekiwane_typy[i]

                        # sprawdzamy czy typy sie zgadzaja
                        if podany_typ and oczekiwany_typ and podany_typ != oczekiwany_typ:
                            self.zglos_blad(ctx,
                                            f"Niezgodność typów w wywołaniu '{nazwa_funkcji}'. Argument {i + 1} powinien być typu '{oczekiwany_typ}', a jest typu '{podany_typ}'!")

        # weryfikacja wywolan pol uzywanych w wyrazeniach
        if isinstance(ctx, SigmaScriptParser.OdwolanieContext):
            self.weryfikuj_odwolanie(ctx)

        # konwersja na C99 compound literals
        if isinstance(ctx, SigmaScriptParser.Inicjalizacja_tablicyContext):
            elementy = self.tlumacz_wyrazenie(ctx.argumenty()) if ctx.argumenty() else ""
            typ_tablicy = self.pobierz_typ_wyrazenia(ctx)

            # w locie budujemy tablice
            if typ_tablicy and typ_tablicy.endswith("[]"):
                typ_c = self.rozpoznawanie_typow(typ_tablicy[:-2])
                return f"({typ_c}[]){{{elementy}}}"
            return f"{{{elementy}}}"

        # jesli doszlismy do liscia w drzewie
        if isinstance(ctx, TerminalNode):
            tekst = ctx.getText()
            # tlumaczymy wylacznie wyizolowane slowa kluczowe
            if tekst == 'oraz': return ' && '
            if tekst == 'lub': return ' || '
            if tekst == 'nie': return ' ! '
            if tekst == 'prawda': return ' 1 '
            if tekst == 'falsz': return ' 0 '
            return tekst

        # jesli to galez - schodzimy glebiej
        wynik = ""
        for i in range(ctx.getChildCount()):
            wynik += self.tlumacz_wyrazenie(ctx.getChild(i))
        return wynik

    #do okreslenia jakiego typu jest cel do ktorego przypisujemy wartosc
    def pobierz_typ_odwolania(self, ctx: SigmaScriptParser.OdwolanieContext):
        glowna_zmienna = ctx.IDENT(0).getText()
        info_zmiennej = self.symbole.pobierz_zmienna(glowna_zmienna)

        if not info_zmiennej:
            return None

        obecny_typ = info_zmiennej['typ']
        czy_tablica = info_zmiennej['czy_tablica']

        # przechozimy po odwolaniach od lewej do prawej
        for i in range(1, ctx.getChildCount()):
            znak = ctx.getChild(i).getText()

            if znak == '[':
                # napotkalismy indeksowanie
                if czy_tablica:
                    czy_tablica = False  # zdejmujemy jeden wymiar tablicy
                elif obecny_typ == 'tekst':
                    obecny_typ = 'znak'  # wyciagamy znak z tekstu
            elif znak == '.':
                pass  # ignorujemy kropke
            elif ctx.getChild(i - 1).getText() == '.':
                # jesli wczesniej kropka, to mamy nazwe pola
                nazwa_pola = znak
                if obecny_typ in self.definicje_struktur and nazwa_pola in self.definicje_struktur[obecny_typ]:
                    pole = self.definicje_struktur[obecny_typ][nazwa_pola]
                    obecny_typ = pole['typ_bazowy']
                    czy_tablica = pole['czy_tablica']
                else:
                    return None  # odwolanie do nieistniejacego pola

        if czy_tablica:
            return f"{obecny_typ}[]"

        return obecny_typ

    #do dynamicnzego okreslania typu na potrzeby funkcji wypisz
    def pobierz_typ_wyrazenia(self, ctx):
        if ctx is None:
            return None

        # zabezpieczenie przed trafieniem w same liscie
        if isinstance(ctx, TerminalNode):
            return None

        # dynamiczne ustlanie typu inicjalizowanej tablicy
        if isinstance(ctx, SigmaScriptParser.Inicjalizacja_tablicyContext):
            if ctx.argumenty():
                pierwszy_elem = ctx.argumenty().wyrazenie_ogolne(0)
                typ_elementu = self.pobierz_typ_wyrazenia(pierwszy_elem)
                if typ_elementu:
                    return f"{typ_elementu}[]"
            return 'tablica'

        # konkretne bloki gramatyki - wywolania i odwolania
        if isinstance(ctx, SigmaScriptParser.Wywolanie_funkcjiContext):
            nazwa_funkcji = ctx.IDENT().getText()
            if nazwa_funkcji in self.zadeklarowane_funkcje:
                typ = self.zadeklarowane_funkcje[nazwa_funkcji]['typ_zwracany']

                # ucinamy nawiasy
                if hasattr(ctx, 'L_KWADRAT') and len(ctx.L_KWADRAT()) > 0 and typ.endswith("[]"):
                    return typ[:-2]
                return typ
            return None

        if isinstance(ctx, SigmaScriptParser.OdwolanieContext):
            return self.pobierz_typ_odwolania(ctx)

        # wyrazenia logiczne
        if isinstance(ctx, SigmaScriptParser.Wyrazenie_logiczneContext):
            if ctx.ROWNY() or ctx.ROZNY() or ctx.operator_rel() or ctx.ORAZ() or ctx.LUB() or ctx.NIE() or \
                    (hasattr(ctx, 'PRAWDA') and ctx.PRAWDA()) or (hasattr(ctx, 'FALSZ') and ctx.FALSZ()):
                return 'logiczna'

        # wyrazenia arytmetyczne
        if isinstance(ctx, SigmaScriptParser.Wyrazenie_arytmetyczneContext):

            # obsluga unarnego minusa
            if ctx.MINUS() and ctx.getChildCount() == 2:
                return self.pobierz_typ_wyrazenia(ctx.wyrazenie_arytmetyczne(0))
            # dzielenie rzutujemy na float
            if ctx.PRZEZ():
                return 'rzeczywista'
            # sprawdzamy co jest po obu stronach
            if ctx.PLUS() or ctx.MINUS() or ctx.RAZY():
                lewy_typ = self.pobierz_typ_wyrazenia(ctx.wyrazenie_arytmetyczne(0))
                prawy_typ = self.pobierz_typ_wyrazenia(
                    ctx.wyrazenie_arytmetyczne(1)) if ctx.getChildCount() > 2 else None

                if lewy_typ == 'tekst' or prawy_typ == 'tekst':
                    # mozemy dodac tekst do tekstu
                    if ctx.PLUS() and lewy_typ == 'tekst' and prawy_typ == 'tekst':
                        return 'tekst'
                    return None #rzucamy blad

                if lewy_typ == 'rzeczywista' or prawy_typ == 'rzeczywista':
                    return 'rzeczywista'
                return 'calkowita'

        # sprawdzenie surowych danych
        if hasattr(ctx, 'TEKST') and ctx.TEKST():
            return 'tekst'
        if hasattr(ctx, 'LICZ_RZECZ') and ctx.LICZ_RZECZ():
            return 'rzeczywista'
        if hasattr(ctx, 'LICZ_CALK') and ctx.LICZ_CALK():
            return 'calkowita'

        # jesli to wezel nadrzedny
        for i in range(ctx.getChildCount()):
            dziecko = ctx.getChild(i)
            typ = self.pobierz_typ_wyrazenia(dziecko)
            if typ:
                return typ

        return 'calkowita'  # domyslnie typ calkowity

    def visitProgram(self, ctx: SigmaScriptParser.ProgramContext):
        print("[Kompilator] Rozpoczynam analizę programu...")

        # skanowanie wstepne (rejestracja funkcji i struktur)
        for definicja in ctx.definicja():
            # rejestracja funkcji
            if definicja.definicja_funkcji():
                f_ctx = definicja.definicja_funkcji()
                nazwa = f_ctx.IDENT().getText()

                # zabezpieczenie przed powtorzona nazwa funkcji
                if nazwa in self.zadeklarowane_funkcje or nazwa in self.definicje_struktur:
                    self.zglos_blad(f_ctx, f"Nazwa funkcji '{nazwa}' jest już zajęta przez inną strukturę lub funkcję!")
                else:
                    typ_zwracany = f_ctx.typ_zwracany().getText()

                    # zapisujemy typy parametrow
                    typy_parametrow = []
                    if f_ctx.parametry():
                        for param in f_ctx.parametry().parametr():
                            bazowy = param.typ().getChild(0).getText()
                            if param.typ().wymiar_tablicy():
                                bazowy += "[]"
                            typy_parametrow.append(bazowy)

                    self.zadeklarowane_funkcje[nazwa] = {
                        'parametry': len(typy_parametrow),
                        'typy_parametrow': typy_parametrow,  # zapisana lista typow
                        'typ_zwracany': typ_zwracany
                    }
            # rejestracja struktur
            elif definicja.definicja_struktury():
                s_ctx = definicja.definicja_struktury()
                nazwa_struktury = s_ctx.IDENT().getText()

                # zabezpieczenie przed powtorzona nazwa struktury
                if nazwa_struktury in self.definicje_struktur or nazwa_struktury in self.zadeklarowane_funkcje:
                    self.zglos_blad(s_ctx,
                                    f"Nazwa struktury '{nazwa_struktury}' jest już zajęta przez inną strukturę lub funkcję!")
                else:
                    self.definicje_struktur[nazwa_struktury] = {}
                    for dekl in s_ctx.deklaracja_zmiennej():
                        typ_bazowy = dekl.typ().getChild(0).getText()
                        nazwa_pola = dekl.IDENT().getText()
                        czy_tablica = dekl.typ().wymiar_tablicy() is not None

                        # zapisujemy kompleksowa informacje o polu
                        self.definicje_struktur[nazwa_struktury][nazwa_pola] = {
                            'typ_bazowy': typ_bazowy,
                            'czy_tablica': czy_tablica
                        }

        # standardowy przebieg
        self.visitChildren(ctx)

        ostateczny_kod = [RUNTIME_C]

        if self.kod_struktur:
            ostateczny_kod.extend(self.kod_struktur)

        if self.prototypy_funkcji:
            ostateczny_kod.append("\n//PROTOTYPY FUNKCJI")
            ostateczny_kod.extend(self.prototypy_funkcji)

        ostateczny_kod.extend(self.kod_globalny)
        ostateczny_kod.append("\nint main() {")
        ostateczny_kod.append("    _init_svg();")
        ostateczny_kod.extend(self.kod_main)
        ostateczny_kod.append("    _zapisz_svg();\n    return 0;\n}")
        return "\n".join(ostateczny_kod)

    # STRUKTURY
    def visitDefinicja_struktury(self, ctx: SigmaScriptParser.Definicja_strukturyContext):
        nazwa_struktury = ctx.IDENT().getText()
        print(f"[Kompilator] Definicja struktury: {nazwa_struktury}")

        # struktury trafiaja na sama gore - uzywamy dedykowanej listy
        self.kod_struktur.append(f"\ntypedef struct {{")

        # czytamy pola struktury
        for deklaracja in ctx.deklaracja_zmiennej():
            typ_bazowy = deklaracja.typ().getChild(0).getText()
            nazwa_pola = deklaracja.IDENT().getText()
            wymiar = deklaracja.typ().wymiar_tablicy().getText() if deklaracja.typ().wymiar_tablicy() else ""

            typ_c = self.rozpoznawanie_typow(typ_bazowy)

            if wymiar == "[]":
                self.kod_struktur.append(f"    {typ_c}* {nazwa_pola};")
            else:
                self.kod_struktur.append(f"    {typ_c} {nazwa_pola}{wymiar};")

        self.kod_struktur.append(f"}} {nazwa_struktury};")

        return None

    # FUNKCJE
    def visitDefinicja_funkcji(self, ctx: SigmaScriptParser.Definicja_funkcjiContext):
        # pobieramy pelna nazwe typu
        typ_zwracany = ctx.typ_zwracany().getText()

        # wyciagamy typ dla C
        if ctx.typ_zwracany().PUSTA():
            typ_c = "void"
        else:
            typ_bazowy_sigma = ctx.typ_zwracany().typ().getChild(0).getText()
            typ_c = self.rozpoznawanie_typow(typ_bazowy_sigma)

            # jesli funkcja zwraca tablice dajemy wskaznik w C
            if ctx.typ_zwracany().typ().wymiar_tablicy() is not None:
                typ_c += "*"

        nazwa_funkcji = ctx.IDENT().getText()
        print(f"[Kompilator] Deklaracja funkcji: {nazwa_funkcji} (zwraca: {typ_c})")

        # rejestrujemy funkcje wraz z informacją o parametrach
        typy_parametrow = []
        if ctx.parametry():
            for param in ctx.parametry().parametr():
                bazowy = param.typ().getChild(0).getText()
                if param.typ().wymiar_tablicy():
                    bazowy += "[]"
                typy_parametrow.append(bazowy)

        self.zadeklarowane_funkcje[nazwa_funkcji] = {
            'parametry': len(typy_parametrow),
            'typy_parametrow': typy_parametrow,
            'typ_zwracany': typ_zwracany
        }

        parametry_c = []
        if ctx.parametry():
            for param in ctx.parametry().parametr():
                typ_param_sigma = param.typ().getChild(0).getText()
                wymiar = param.typ().wymiar_tablicy().getText() if param.typ().wymiar_tablicy() else ""

                p_typ = self.rozpoznawanie_typow(typ_param_sigma)

                # typ, nazwa oraz ewentualny wymiar tablicy
                parametry_c.append(f"{p_typ} {param.IDENT().getText()}{wymiar}")

        # rejestracja prototypu funkcji
        prototyp = f"{typ_c} {nazwa_funkcji}({', '.join(parametry_c)});"
        if prototyp not in self.prototypy_funkcji:
            self.prototypy_funkcji.append(prototyp)

        self.w_funkcji = True
        self.oczekiwany_typ_zwracany = typ_zwracany
        self.czy_zwrocono_wartosc = False

        self.dodaj_kod(f"\n{typ_c} {nazwa_funkcji}({', '.join(parametry_c)}) {{")
        self.symbole.wejdz_do_bloku()
        # rejestrujemy parametry w lokalnej tablicy symboli
        if ctx.parametry():
            for param in ctx.parametry().parametr():
                typ_param_sigma = param.typ().getChild(0).getText()
                nazwa_param = param.IDENT().getText()
                czy_tablica = param.typ().wymiar_tablicy() is not None
                self.symbole.dodaj_zmienna(nazwa_param, typ_param_sigma, czy_tablica)
        self.visit(ctx.blok_kodu())

        # Sprawdzamy czy funkcja (inna niz pusta) miala instrukcje zwroc
        if self.oczekiwany_typ_zwracany != "pusta" and not self.czy_zwrocono_wartosc:
            self.zglos_blad(ctx,
                            f"Funkcja '{nazwa_funkcji}' powinna zwracać typ '{self.oczekiwany_typ_zwracany}', ale brakuje instrukcji 'zwroc'!")

        self.oczekiwany_typ_zwracany = None
        self.symbole.wyjdz_z_bloku()
        self.dodaj_kod("}")
        self.w_funkcji = False
        return None

    def visitInstrukcja_zwrotu(self, ctx: SigmaScriptParser.Instrukcja_zwrotuContext):
        self.czy_zwrocono_wartosc = True
        wartosc = self.tlumacz_wyrazenie(ctx.wyrazenie_ogolne()) if ctx.wyrazenie_ogolne() else ""

        # walidacja typu zwracanego
        if self.w_funkcji:
            if wartosc:
                # pobieramy faktyczny typ
                faktyczny_typ = self.pobierz_typ_wyrazenia(ctx.wyrazenie_ogolne())

                # upewniamy sie ze nie zwracamy wartosci z funkcji typu pusta
                if self.oczekiwany_typ_zwracany == "pusta":
                    self.zglos_blad(ctx,
                                    "Próbujesz zwrócić wartość, ale funkcja została oznaczona jako 'pusta' (niezwracająca niczego)!")
                # porownujemy typ deklarowany z faktycznym
                elif faktyczny_typ != self.oczekiwany_typ_zwracany:
                    self.zglos_blad(ctx,
                                    f"Funkcja powinna zwracać typ '{self.oczekiwany_typ_zwracany}', a próbuje zwrócić '{faktyczny_typ}'!")
            else:
                # puste zwroc w funkcji innej niz pusta
                if self.oczekiwany_typ_zwracany != "pusta":
                    self.zglos_blad(ctx,
                                    f"Użyto instrukcji 'zwroc;' bez podania wartości, mimo że funkcja wymaga typu '{self.oczekiwany_typ_zwracany}'!")

        if not self.w_funkcji:
            # jestesmy w programie glownym wiec zapisujemy plik svg przed wyjsciem
            self.dodaj_kod("    _zapisz_svg();")
            if wartosc:
                self.dodaj_kod(f"    return {wartosc};")
            else:
                self.dodaj_kod("    return 0;")
        else:
            # standardowy return z wnetrza funkcji
            if wartosc:
                self.dodaj_kod(f"    return {wartosc};")
            else:
                self.dodaj_kod("    return;")
        return None

    def visitWywolanie_funkcji(self, ctx: SigmaScriptParser.Wywolanie_funkcjiContext):
        kod = self.tlumacz_wyrazenie(ctx)
        print(f"[Kompilator] Wywołanie funkcji: {kod}")
        self.dodaj_kod(f"    {kod};")
        return None

    # ZMIENNE I TABLICE
    def visitDeklaracja_zmiennej(self, ctx: SigmaScriptParser.Deklaracja_zmiennejContext):
        typ_bazowy = ctx.typ().getChild(0).getText()
        wymiar = ctx.typ().wymiar_tablicy().getText() if ctx.typ().wymiar_tablicy() else ""
        nazwa = ctx.IDENT().getText()

        czy_tablica = ctx.typ().wymiar_tablicy() is not None

        # sprawdzenie czy zmienna juz istnieje
        sukces = self.symbole.dodaj_zmienna(nazwa, typ_bazowy, czy_tablica)
        if not sukces:
            self.zglos_blad(ctx, f"Zmienna '{nazwa}' jest już zadeklarowana w tym bloku kodu!")
            return None

        typ_c = self.rozpoznawanie_typow(typ_bazowy)

        wartosc_c = ""
        if ctx.wyrazenie_ogolne():
            wartosc_sigma = self.tlumacz_wyrazenie(ctx.wyrazenie_ogolne())
            czy_inicjalizacja_tablicy = isinstance(ctx.wyrazenie_ogolne(),
                                                   SigmaScriptParser.Inicjalizacja_tablicyContext)

            if czy_inicjalizacja_tablicy:
                wartosc_c = " = " + wartosc_sigma.split("]", 1)[-1] if wartosc_sigma.startswith(
                    "(") else " = " + wartosc_sigma
            else:
                wartosc_c = " = " + wartosc_sigma

        # walidacja pustych tablic
        if wymiar == "[]" and not wartosc_c:
            self.zglos_blad(ctx,
                            f"Tablica '{nazwa}' musi mieć z góry określony rozmiar (np. calkowita[10] {nazwa}) lub zostać natychmiast zainicjowana wartościami!")
            return None

        print(f"[Kompilator] Deklaracja zmiennej: {nazwa} ({typ_c})")

        # sprawdzamy czy jestesmy globalnie
        jest_globalnie = (len(self.symbole.stos_zasiegow) == 1)

        if jest_globalnie:
            if czy_tablica:
                typ_wskaznika = f"{typ_c}*"
                if wartosc_c and wartosc_c.startswith(" = {"):
                    self.kod_globalny.append(f"{typ_c} {nazwa}{wymiar}{wartosc_c};")
                else:
                    # globalne wskazniki
                    self.kod_globalny.append(f"{typ_wskaznika} {nazwa} = NULL;")
                    if wartosc_c:
                        self.kod_main.append(f"    {nazwa}{wartosc_c};")
                    # rezerwacja pamieci
                    elif wymiar and wymiar != "[]":
                        rozmiar_liczb = wymiar[1:-1]
                        self.kod_main.append(
                            f"    {nazwa} = ({typ_wskaznika})calloc({rozmiar_liczb}, sizeof({typ_c}));")
                        self.kod_main.append(f"    _rejestruj_pamiec({nazwa});")
            else:
                self.kod_globalny.append(f"{typ_c} {nazwa}{wymiar};")
                if wartosc_c:
                    self.kod_main.append(f"    {nazwa}{wartosc_c};")
        else:
            if czy_tablica:
                typ_wskaznika = f"{typ_c}*"
                if wartosc_c and wartosc_c.startswith(" = {"):
                    self.dodaj_kod(f"    {typ_c} _tmp_{nazwa}[] {wartosc_c};")
                    self.dodaj_kod(f"    {typ_wskaznika} {nazwa} = ({typ_wskaznika})malloc(sizeof(_tmp_{nazwa}));")
                    self.dodaj_kod(f"    memcpy({nazwa}, _tmp_{nazwa}, sizeof(_tmp_{nazwa}));")
                    self.dodaj_kod(f"    _rejestruj_pamiec({nazwa});")
                # alokujemy puste tylko jak nie dodano
                elif wymiar and wymiar != "[]" and not wartosc_c:
                    rozmiar_liczb = wymiar[1:-1]
                    self.dodaj_kod(
                        f"    {typ_wskaznika} {nazwa} = ({typ_wskaznika})calloc({rozmiar_liczb}, sizeof({typ_c}));")
                    self.dodaj_kod(f"    _rejestruj_pamiec({nazwa});")
                else:
                    self.dodaj_kod(f"    {typ_wskaznika} {nazwa}{wartosc_c};")
            else:
                self.dodaj_kod(f"    {typ_c} {nazwa}{wymiar}{wartosc_c};")

        return None

    def visitPrzypisanie(self, ctx: SigmaScriptParser.PrzypisanieContext):
        pelne_odwolanie = ctx.odwolanie().getText()
        glowna_zmienna = ctx.odwolanie().IDENT(0).getText()

        #pobieramy typ zmiennej
        typ_zmiennej = self.symbole.pobierz_typ_zmiennej(glowna_zmienna)

        #sprawdzamy czy zmienna istnieje
        if typ_zmiennej is None:
            self.zglos_blad(ctx, f"Próbujesz zmienić wartość '{glowna_zmienna}', ale taka zmienna nie istnieje!")
            return None

        # weryfikacja wywolan pol
        self.weryfikuj_odwolanie(ctx.odwolanie())

        wyrazenie_c = self.tlumacz_wyrazenie(ctx.wyrazenie_ogolne())

        # scisla kontrola typow
        typ_docelowy = self.pobierz_typ_odwolania(ctx.odwolanie())
        typ_wyrazenia = self.pobierz_typ_wyrazenia(ctx.wyrazenie_ogolne())

        if typ_docelowy and typ_wyrazenia and typ_docelowy != typ_wyrazenia:
            self.zglos_blad(ctx,
                            f"Niezgodność typów! Próba przypisania wartości typu '{typ_wyrazenia}' do zmiennej typu '{typ_docelowy}'.")

        # blokada przypisywania calej tablicy po deklaracji
        czy_inicjalizacja_tablicy = isinstance(ctx.wyrazenie_ogolne(), SigmaScriptParser.Inicjalizacja_tablicyContext)
        if czy_inicjalizacja_tablicy:
            self.zglos_blad(ctx, "Nie można przypisać całej nowej tablicy po deklaracji. Zmieniaj pojedyncze elementy!")
            return None

        self.dodaj_kod(f"    {pelne_odwolanie} = {wyrazenie_c};")
        return None

    # STEROWANIE I LOGIKA
    def visitPolecenie_ruchu(self, ctx):
        kod_wyrazenia = self.tlumacz_wyrazenie(ctx.wyrazenie_arytmetyczne())
        print(f"[Kompilator] Znalazłem ruch: naprzod {ctx.wyrazenie_arytmetyczne().getText()}")
        self.dodaj_kod(f"    _naprzod({kod_wyrazenia});")
        return None

    def visitPolecenie_obrotu(self, ctx):
        kod_wyrazenia = self.tlumacz_wyrazenie(ctx.wyrazenie_arytmetyczne())
        print(f"[Kompilator] Znalazłem obrót: obroc {ctx.wyrazenie_arytmetyczne().getText()}")
        self.dodaj_kod(f"    _obroc({kod_wyrazenia});")
        return None

    def visitPolecenie_pisaka(self, ctx):
        if ctx.PODNIES():
            print("[Kompilator] Znalazłem polecenie: podnies_pisak")
            self.dodaj_kod("    _podnies_pisak();")
        elif ctx.OPUSC():
            print("[Kompilator] Znalazłem polecenie: opusc_pisak")
            self.dodaj_kod("    _opusc_pisak();")
        return None

    def visitWypisanie(self, ctx):
        wyraz = ctx.wyrazenie_ogolne()
        typ_wyrazu = self.pobierz_typ_wyrazenia(wyraz)

        # zabezpieczenie przed wypisywaniem calych struktur
        if typ_wyrazu in self.definicje_struktur:
            self.zglos_blad(ctx,
                            f"Nie można wypisać całego obiektu typu '{typ_wyrazu}'. Odwołaj się do konkretnego pola tej struktury!")
            return None

        kod_wyrazu = self.tlumacz_wyrazenie(wyraz)

        if typ_wyrazu == 'tekst':
            self.dodaj_kod(f"    printf(\"%s\\n\", {kod_wyrazu});")
        elif typ_wyrazu == 'znak':
            self.dodaj_kod(f"    printf(\"%c\\n\", {kod_wyrazu});")
        elif typ_wyrazu == 'rzeczywista':
            self.dodaj_kod(f"    printf(\"%f\\n\", {kod_wyrazu});")
        else:
            self.dodaj_kod(f"    printf(\"%d\\n\", {kod_wyrazu});")
        return None

    def visitPetla(self, ctx: SigmaScriptParser.PetlaContext):
        ile = self.tlumacz_wyrazenie(ctx.wyrazenie_arytmetyczne())
        print(f"[Kompilator] Znalazłem pętlę: powtorz {ile}")
        z_petli = f"_i_{id(ctx)}"
        self.dodaj_kod(f"    for(int {z_petli} = 0; {z_petli} < (int)({ile}); {z_petli}++) {{")
        self.symbole.wejdz_do_bloku()
        self.visit(ctx.blok_kodu())
        self.symbole.wyjdz_z_bloku()
        self.dodaj_kod("    }")
        return None

    def visitPetla_warunkowa(self, ctx: SigmaScriptParser.Petla_warunkowaContext):
        warunek_c = self.tlumacz_wyrazenie(ctx.wyrazenie_logiczne())
        print(f"[Kompilator] Znalazłem pętlę warunkową (dopoki): {warunek_c}")
        self.dodaj_kod(f"    while ({warunek_c}) {{")
        self.symbole.wejdz_do_bloku()
        self.visit(ctx.blok_kodu())
        self.symbole.wyjdz_z_bloku()
        self.dodaj_kod("    }")
        return None

    def visitInstrukcja_warunkowa(self, ctx: SigmaScriptParser.Instrukcja_warunkowaContext):
        warunek_c = self.tlumacz_wyrazenie(ctx.wyrazenie_logiczne())
        print(f"[Kompilator] Znalazłem instrukcję warunkową (jezeli): {warunek_c}")
        self.dodaj_kod(f"    if ({warunek_c}) {{")
        self.symbole.wejdz_do_bloku()
        self.visit(ctx.blok_kodu(0))
        self.symbole.wyjdz_z_bloku()
        self.dodaj_kod("    }")
        if ctx.INACZEJ():
            self.dodaj_kod("    else {")
            self.symbole.wejdz_do_bloku()
            self.visit(ctx.blok_kodu(1))
            self.symbole.wyjdz_z_bloku()
            self.dodaj_kod("    }")
        return None


def main():
    if len(sys.argv) < 2:
        print("Uzycie: python main.py <plik.ss>")
        return

    plik_wejsciowy = sys.argv[1]
    input_stream = FileStream(plik_wejsciowy, encoding='utf-8')

    error_listener = PolskiErrorListener()

    lexer = SigmaScriptLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    parser = SigmaScriptParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if len(error_listener.bledy) > 0:
        print("\n[!] Znalazłem błędy w Twoim kodzie. Popraw je, aby przejść dalej!")
        return

    visitor = KompilatorVisitor()
    gotowy_kod_c = visitor.visit(tree)

    if len(visitor.bledy_semantyczne) > 0:
        print("\n[!] Znalazłem błędy logiczne w Twoim kodzie. Popraw je, aby przejść dalej!")
        for blad in visitor.bledy_semantyczne:
            print(blad)
        return

    with open("wynik.c", "w", encoding='utf-8') as f:
        f.write(gotowy_kod_c)

    print("\n[Sukces] Wygenerowano kod docelowy w wynik.c")


if __name__ == '__main__':
    main()