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
#include <math.h>

FILE *svg_file;
float _x = 500.0; // poczatek na srodku plotna
float _y = 500.0;
float _kat = -90.0; // -90 stopni -- patrzymy w gore

void _init_svg() {
    svg_file = fopen("wynik.svg", "w");
    fprintf(svg_file, "<svg width=\\"1000\\" height=\\"1000\\" xmlns=\\"http://www.w3.org/2000/svg\\">\\n"); //poczatek svg z deklaracja przestrzeni nazw
    fprintf(svg_file, "<rect width=\\"100%%\\" height=\\"100%%\\" fill=\\"#f0f0f0\\"/>\\n"); // jasnoszare tlo
}

void _zapisz_svg() {
    fprintf(svg_file, "</svg>\\n");
    fclose(svg_file);
    printf("[+] Misja zakonczona. Wygenerowano plik wynik.svg!\\n");
}

void _naprzod(float dystans) {
    float rad = _kat * (3.14159265 / 180.0);
    float new_x = _x + dystans * cos(rad);
    float new_y = _y + dystans * sin(rad);

    // rysujemy linie w svg
    fprintf(svg_file, "<line x1=\\"%.2f\\" y1=\\"%.2f\\" x2=\\"%.2f\\" y2=\\"%.2f\\" stroke=\\"#2c3e50\\" stroke-width=\\"3\\" stroke-linecap=\\"round\\" />\\n", _x, _y, new_x, new_y);

    // aktualizujemy pozycje
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
    def dodaj_zmienna(self, nazwa, typ):
        obecny_zasieg = self.stos_zasiegow[-1]
        if nazwa in obecny_zasieg:
            return False  # rzucamy blad - zmienna juz istnieje w bloku

        obecny_zasieg[nazwa] = {'typ': typ}
        return True

    #szuka zmiennej od obecnego do globalnego bloku
    def pobierz_typ_zmiennej(self, nazwa):
        for zasieg in reversed(self.stos_zasiegow):
            if nazwa in zasieg:
                return zasieg[nazwa]['typ']
        return None  # rzucamy blad gdy zmienna nie istnieje

class KompilatorVisitor(SigmaScriptVisitor):
    def __init__(self):
        self.kod_globalny = [] #na funkcje i struktury
        self.kod_main = [] #na cala reszte
        self.w_funkcji = False

        # tabela symboli, rejestr struktur, rejestr funkcji i tablica bledow semantycznych
        self.symbole = TabelaSymboli()
        self.definicje_struktur = {}
        self.zadeklarowane_funkcje = {}
        self.bledy_semantyczne = []

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
        typ_zmiennej = self.symbole.pobierz_typ_zmiennej(glowna_zmienna)

        # jesli zmienna nie istnieje - zglaszamy blad
        if typ_zmiennej is None:
            blad = f"[!] Błąd logiczny: Użyto zmiennej '{glowna_zmienna}', która nie została wcześniej zadeklarowana!"
            if blad not in self.bledy_semantyczne:
                self.bledy_semantyczne.append(blad)
            return

        # sprawdzamy czy sa odwolania do pol
        if len(ctx.IDENT()) > 1:
            obecny_typ = typ_zmiennej
            identyfikatory = ctx.IDENT()

            for i in range(1, len(identyfikatory)):
                nazwa_pola = identyfikatory[i].getText()

                # czy to na pewno struktura
                if obecny_typ not in self.definicje_struktur:
                    blad = f"[!] Błąd logiczny: Zmienna '{identyfikatory[i - 1].getText()}' (typu {obecny_typ}) nie jest strukturą i nie posiada pól!"
                    if blad not in self.bledy_semantyczne: self.bledy_semantyczne.append(blad)
                    return

                struktura = self.definicje_struktur[obecny_typ]

                # czy pole istnieje w strukturze
                if nazwa_pola not in struktura:
                    blad = f"[!] Błąd logiczny: Struktura '{obecny_typ}' nie posiada pola o nazwie '{nazwa_pola}'!"
                    if blad not in self.bledy_semantyczne: self.bledy_semantyczne.append(blad)
                    return

                # aktualizujemy typ (obsluga zagniezdzen)
                obecny_typ = struktura[nazwa_pola]

    def tlumacz_wyrazenie(self, ctx):

        if ctx is None:
            return ""

        # zabezpieczenie przed dzieleniem przez zero w wyrazeniach
        if isinstance(ctx, SigmaScriptParser.Wyrazenie_arytmetyczneContext):
            if ctx.PRZEZ():
                # tlumaczymy lewa i prawa strone
                lewe = self.tlumacz_wyrazenie(ctx.wyrazenie_arytmetyczne(0))
                prawe = self.tlumacz_wyrazenie(ctx.wyrazenie_arytmetyczne(1))
                # wywolujemy bezpieczne dzielenie
                return f"_bezpieczne_dzielenie((float)({lewe}), (float)({prawe}))"

        # weryfikacja czy wywolywana funkcja istnieje
        if isinstance(ctx, SigmaScriptParser.Wywolanie_funkcjiContext):
            nazwa_funkcji = ctx.IDENT().getText()

            # weryfikacja z uzyciem slownika
            if nazwa_funkcji not in self.zadeklarowane_funkcje:
                blad = f"[!] Błąd logiczny: Próba wywołania nieznanej funkcji '{nazwa_funkcji}'!"
                if blad not in self.bledy_semantyczne: self.bledy_semantyczne.append(blad)
            else:
                # weryfikacja liczby argumentow
                podane_argumenty = len(ctx.argumenty().wyrazenie_ogolne()) if ctx.argumenty() else 0
                oczekiwane_argumenty = self.zadeklarowane_funkcje[nazwa_funkcji]
                if podane_argumenty != oczekiwane_argumenty:
                    blad = f"[!] Błąd logiczny: Funkcja '{nazwa_funkcji}' oczekuje {oczekiwane_argumenty} argumentów, a podano {podane_argumenty}!"
                    if blad not in self.bledy_semantyczne: self.bledy_semantyczne.append(blad)

        # weryfikacja wywolan pol uzywanych w wyrazeniach
        if isinstance(ctx, SigmaScriptParser.OdwolanieContext):
            self.weryfikuj_odwolanie(ctx)

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

    #do dynamicnzego okreslania typu na potrzeby funkcji wypisz
    def pobierz_typ_wyrazenia(self, ctx):
        if ctx.TEKST():
            return 'tekst'

        tekst_surowy = ctx.getText()

        # usuwamy indeksy tablicy z analizowanego tekstu
        tekst_bez_indeksow = re.sub(r'\[.*?\]', '', tekst_surowy)

        # szukamy po wyczyszczonym tekscie
        odwolania = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*', tekst_bez_indeksow)
        for odw in odwolania:
            czlon = odw.split('.')
            if czlon[0] in ['prawda', 'falsz', 'oraz', 'lub', 'nie']:
                continue

            typ = self.symbole.pobierz_typ_zmiennej(czlon[0])

            # jesli zmienna jest struktura i wyraznie ma kropki to schodzimy do jej pol
            if typ and len(czlon) > 1:
                for pole in czlon[1:]:
                    if typ in self.definicje_struktur and pole in self.definicje_struktur[typ]:
                        typ = self.definicje_struktur[typ][pole]

            # sprawdzamy ostateczny lisc z naszej sciezki
            if typ == 'rzeczywista':
                return 'rzeczywista'
            elif typ == 'tekst':
                return 'tekst'

        # jesli sa kropki ale to nie tekst
        if '.' in tekst_surowy and '"' not in tekst_surowy:
            return 'rzeczywista'

        return 'calkowita'  # domyslnie typ calkowity

    def visitProgram(self, ctx: SigmaScriptParser.ProgramContext):
        print("[Kompilator] Rozpoczynam analizę programu...")
        self.visitChildren(ctx)

        ostateczny_kod = [RUNTIME_C]
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

        # tworzymy wpis w slowniku struktur
        self.definicje_struktur[nazwa_struktury] = {}

        # struktury trafiaja na sama gore
        self.w_funkcji = True
        self.dodaj_kod(f"\ntypedef struct {{")

        # Czytamy pola struktury
        for deklaracja in ctx.deklaracja_zmiennej():
            typ_bazowy = deklaracja.typ().getChild(0).getText()
            nazwa_pola = deklaracja.IDENT().getText()
            wymiar = deklaracja.typ().wymiar_tablicy().getText() if deklaracja.typ().wymiar_tablicy() else ""

            # rejestrujemy pole w naszym rejestrze struktur
            self.definicje_struktur[nazwa_struktury][nazwa_pola] = typ_bazowy

            typ_c = self.rozpoznawanie_typow(typ_bazowy)

            self.dodaj_kod(f"    {typ_c} {nazwa_pola}{wymiar};")

        self.dodaj_kod(f"}} {nazwa_struktury};")
        self.w_funkcji = False
        return None

    # FUNKCJE
    def visitDefinicja_funkcji(self, ctx: SigmaScriptParser.Definicja_funkcjiContext):
        typ_zwracany = ctx.typ_zwracany().getText()

        typ_c = self.rozpoznawanie_typow(typ_zwracany)

        nazwa_funkcji = ctx.IDENT().getText()
        print(f"[Kompilator] Deklaracja funkcji: {nazwa_funkcji}")

        # rejestrujemy funkcje wraz z liczba jej parametrow
        liczba_parametrow = len(ctx.parametry().parametr()) if ctx.parametry() else 0
        self.zadeklarowane_funkcje[nazwa_funkcji] = liczba_parametrow

        parametry_c = []
        if ctx.parametry():
            for param in ctx.parametry().parametr():
                typ_param_sigma = param.typ().getChild(0).getText()
                wymiar = param.typ().wymiar_tablicy().getText() if param.typ().wymiar_tablicy() else ""

                p_typ = self.rozpoznawanie_typow(typ_param_sigma)

                # typ, nazwa oraz ewentualny wymiar tablicy
                parametry_c.append(f"{p_typ} {param.IDENT().getText()}{wymiar}")

        self.w_funkcji = True
        self.dodaj_kod(f"\n{typ_c} {nazwa_funkcji}({', '.join(parametry_c)}) {{")
        self.symbole.wejdz_do_bloku()
        # rejestrujemy parametry w lokalnej tablicy symboli
        if ctx.parametry():
            for param in ctx.parametry().parametr():
                typ_param_sigma = param.typ().getChild(0).getText()
                nazwa_param = param.IDENT().getText()
                self.symbole.dodaj_zmienna(nazwa_param, typ_param_sigma)
        self.visit(ctx.blok_kodu())
        self.symbole.wyjdz_z_bloku()
        self.dodaj_kod("}")
        self.w_funkcji = False
        return None

    def visitInstrukcja_zwrotu(self, ctx: SigmaScriptParser.Instrukcja_zwrotuContext):
        if ctx.wyrazenie_ogolne():
            wartosc = self.tlumacz_wyrazenie(ctx.wyrazenie_ogolne())
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

        # sprawdzenie czy zmienna juz istnieje
        sukces = self.symbole.dodaj_zmienna(nazwa, typ_bazowy)
        if not sukces:
            blad = f"[!] Błąd logiczny: Zmienna '{nazwa}' jest już zadeklarowana w tym bloku kodu!"
            self.bledy_semantyczne.append(blad)
            return None

        typ_c = self.rozpoznawanie_typow(typ_bazowy)

        wartosc_c = ""
        if ctx.wyrazenie_ogolne():
            wartosc_sigma = self.tlumacz_wyrazenie(ctx.wyrazenie_ogolne())
            if wartosc_sigma.startswith("[") and wartosc_sigma.endswith("]"):
                wartosc_c = " = {" + wartosc_sigma[1:-1] + "}"
            else:
                wartosc_c = " = " + wartosc_sigma

        print(f"[Kompilator] Deklaracja zmiennej: {nazwa} ({typ_c})")

        # jesli jestesmy poza funkcjami (globalnie)
        if not self.w_funkcji:
            # tablice inicjalizujemy globalnie
            if wartosc_c and wartosc_c.startswith(" = {"):
                self.kod_globalny.append(f"{typ_c} {nazwa}{wymiar}{wartosc_c};")
            else:
                # rozdzielamy deklaracje od inicjalizacji
                self.kod_globalny.append(f"{typ_c} {nazwa}{wymiar};")
                if wartosc_c:
                    self.kod_main.append(f"    {nazwa}{wartosc_c};")
        else:
            #wewnatrz funkcji deklarujemy standardowo
            self.dodaj_kod(f"    {typ_c} {nazwa}{wymiar}{wartosc_c};")

        return None

    def visitPrzypisanie(self, ctx: SigmaScriptParser.PrzypisanieContext):
        pelne_odwolanie = ctx.odwolanie().getText()
        glowna_zmienna = ctx.odwolanie().IDENT(0).getText()

        #pobieramy typ zmiennej
        typ_zmiennej = self.symbole.pobierz_typ_zmiennej(glowna_zmienna)

        #sprawdzamy czy zmienna istnieje
        if typ_zmiennej is None:
            blad = f"[!] Błąd logiczny: Próbujesz zmienić wartość '{glowna_zmienna}', ale taka zmienna nie istnieje (lub nie jest tu widoczna)!"
            self.bledy_semantyczne.append(blad)
            return None

        # weryfikacja wywolan pol
        self.weryfikuj_odwolanie(ctx.odwolanie())

        wyrazenie_c = self.tlumacz_wyrazenie(ctx.wyrazenie_ogolne())

        # blokada przypisywania calej tablicy po deklaracji
        if wyrazenie_c.startswith("[") and wyrazenie_c.endswith("]"):
            blad = f"[!] Błąd logiczny: Nie można przypisać całej nowej tablicy {wyrazenie_c} po deklaracji. Zmieniaj pojedyncze elementy!"
            if blad not in self.bledy_semantyczne: self.bledy_semantyczne.append(blad)
            return None

        self.dodaj_kod(f"    {pelne_odwolanie} = {wyrazenie_c};")
        return None

    # STEROWANIE I LOGIKA
    def visitPolecenie_ruchu(self, ctx):
        print(f"[Kompilator] Znalazłem ruch: naprzod {ctx.wyrazenie_arytmetyczne().getText()}")
        self.dodaj_kod(f"    _naprzod({ctx.wyrazenie_arytmetyczne().getText()});")
        return None

    def visitPolecenie_obrotu(self, ctx):
        print(f"[Kompilator] Znalazłem obrót: obroc {ctx.wyrazenie_arytmetyczne().getText()}")
        self.dodaj_kod(f"    _obroc({ctx.wyrazenie_arytmetyczne().getText()});")
        return None

    def visitWypisanie(self, ctx):
        wyraz = ctx.wyrazenie_ogolne()
        typ_wyrazu = self.pobierz_typ_wyrazenia(wyraz)
        kod_wyrazu = self.tlumacz_wyrazenie(wyraz)

        if typ_wyrazu == 'tekst':
            self.dodaj_kod(f"    printf(\"%s\\n\", {kod_wyrazu});")
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