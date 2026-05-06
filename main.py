import sys
import re
from antlr4 import *
from antlr_generated.SigmaScriptLexer import SigmaScriptLexer
from antlr_generated.SigmaScriptParser import SigmaScriptParser
from antlr_generated.SigmaScriptVisitor import SigmaScriptVisitor
from antlr4.error.ErrorListener import ErrorListener


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
    printf("[Zolw] Misja zakonczona. Wygenerowano plik wynik.svg!\\n");
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
"""


class KompilatorVisitor(SigmaScriptVisitor):
    def __init__(self):
        self.kod_globalny = [] #na funkcje i struktury
        self.kod_main = [] #na cala reszte
        self.w_funkcji = False

        #tabela symboli i bledy semantyczne
        self.zadeklarowane_zmienne = set()
        self.zadeklarowane_struktury = set()
        self.bledy_semantyczne = []

    def dodaj_kod(self, linia):
        if self.w_funkcji:
            self.kod_globalny.append(linia)
        else:
            self.kod_main.append(linia)

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

        self.w_funkcji = True  # Struktury muszą trafić na samą górę pliku C
        self.dodaj_kod(f"\ntypedef struct {{")

        # Czytamy pola struktury
        for deklaracja in ctx.deklaracja_zmiennej():
            typ_bazowy = deklaracja.typ().getChild(0).getText()
            nazwa_pola = deklaracja.IDENT().getText()
            wymiar = deklaracja.typ().wymiar_tablicy().getText() if deklaracja.typ().wymiar_tablicy() else ""

            if "calkowita" in typ_bazowy:
                typ_c = "int"
            elif "rzeczywista" in typ_bazowy:
                typ_c = "float"
            elif "logiczna" in typ_bazowy:
                typ_c = "int"
            else:
                typ_c = typ_bazowy  # Pozwala nawet na struktury w strukturach

            self.dodaj_kod(f"    {typ_c} {nazwa_pola}{wymiar};")

        self.dodaj_kod(f"}} {nazwa_struktury};")
        self.w_funkcji = False
        return None

    # FUNKCJE
    def visitDefinicja_funkcji(self, ctx: SigmaScriptParser.Definicja_funkcjiContext):
        typ_zwracany = ctx.typ_zwracany().getText()
        if "calkowita" in typ_zwracany:
            typ_c = "int"
        elif "rzeczywista" in typ_zwracany:
            typ_c = "float"
        elif "logiczna" in typ_zwracany:
            typ_c = "int"
        elif "pusta" in typ_zwracany:
            typ_c = "void"
        else:
            typ_c = typ_zwracany  # Zwracanie obiektów struktur

        nazwa_funkcji = ctx.IDENT().getText()
        print(f"[Kompilator] Deklaracja funkcji: {nazwa_funkcji}")

        parametry_c = []
        if ctx.parametry():
            for param in ctx.parametry().parametr():
                typ_param_sigma = param.typ().getChild(0).getText()
                if "calkowita" in typ_param_sigma:
                    p_typ = "int"
                elif "rzeczywista" in typ_param_sigma:
                    p_typ = "float"
                elif "logiczna" in typ_param_sigma:
                    p_typ = "int"
                else:
                    p_typ = typ_param_sigma  # Parametr typu struktury

                parametry_c.append(f"{p_typ} {param.IDENT().getText()}")

        self.w_funkcji = True
        self.dodaj_kod(f"\n{typ_c} {nazwa_funkcji}({', '.join(parametry_c)}) {{")
        self.visit(ctx.blok_kodu())
        self.dodaj_kod("}")
        self.w_funkcji = False
        return None

    def visitInstrukcja_zwrotu(self, ctx: SigmaScriptParser.Instrukcja_zwrotuContext):
        if ctx.wyrazenie_ogolne():
            wartosc = ctx.wyrazenie_ogolne().getText().replace("prawda", "1").replace("falsz", "0")
            self.dodaj_kod(f"    return {wartosc};")
        else:
            self.dodaj_kod("    return;")
        return None

    def visitWywolanie_funkcji(self, ctx: SigmaScriptParser.Wywolanie_funkcjiContext):
        kod = ctx.getText().replace("prawda", "1").replace("falsz", "0")
        print(f"[Kompilator] Wywołanie funkcji: {kod}")
        self.dodaj_kod(f"    {kod};")
        return None

    # ZMIENNE I TABLICE
    def visitDeklaracja_zmiennej(self, ctx: SigmaScriptParser.Deklaracja_zmiennejContext):
        typ_bazowy = ctx.typ().getChild(0).getText()
        wymiar = ctx.typ().wymiar_tablicy().getText() if ctx.typ().wymiar_tablicy() else ""
        nazwa = ctx.IDENT().getText()

        # sprawdzenie czy zmienna juz istnieje
        if nazwa in self.zadeklarowane_zmienne:
            blad = f"Błąd logiczny: Zmienna o nazwie '{nazwa}' została już wcześniej stworzona!"
            print(blad)
            self.bledy_semantyczne.append(blad)
            return None  # przerywamy przetwarzanie tej zmiennej

        self.zadeklarowane_zmienne.add(nazwa)

        if "calkowita" in typ_bazowy:
            typ_c = "int"
        elif "rzeczywista" in typ_bazowy:
            typ_c = "float"
        elif "logiczna" in typ_bazowy:
            typ_c = "int"
        else:
            typ_c = typ_bazowy  # obsluga inicjalizacji struktury: Dron moj_dron

        wartosc_c = ""
        if ctx.wyrazenie_ogolne():
            wartosc_sigma = ctx.wyrazenie_ogolne().getText()
            if wartosc_sigma.startswith("[") and wartosc_sigma.endswith("]"):
                wartosc_c = " = {" + wartosc_sigma[1:-1] + "}"
            else:
                wartosc_c = " = " + wartosc_sigma.replace("prawda", "1").replace("falsz", "0")

        print(f"[Kompilator] Deklaracja zmiennej: {nazwa} ({typ_c})")
        self.dodaj_kod(f"    {typ_c} {nazwa}{wymiar}{wartosc_c};")
        return None

    def visitPrzypisanie(self, ctx: SigmaScriptParser.PrzypisanieContext):
        pelne_odwolanie = ctx.odwolanie().getText()

        glowna_zmienna = ctx.odwolanie().IDENT(0).getText()

        #sprawdzamy czy zmienna istnieje
        if glowna_zmienna not in self.zadeklarowane_zmienne:
            blad = f"Błąd logiczny: Próbujesz zmienić wartość '{glowna_zmienna}', ale taka zmienna nie została zadeklarowana!"
            print(blad)
            self.bledy_semantyczne.append(blad)
            return None

        # jesli wszystko ok - generujemy kod w C
        wyrazenie_c = ctx.wyrazenie_ogolne().getText().replace('prawda', '1').replace('falsz', '0')
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
        self.dodaj_kod(f"    printf(\"%s\\n\", {ctx.wyrazenie_ogolne().getText()});")
        return None

    def visitPetla(self, ctx: SigmaScriptParser.PetlaContext):
        ile = ctx.wyrazenie_arytmetyczne().getText()
        print(f"[Kompilator] Znalazłem pętlę: powtorz {ile}")
        z_petli = f"_i_{id(ctx)}"
        self.dodaj_kod(f"    for(int {z_petli} = 0; {z_petli} < (int)({ile}); {z_petli}++) {{")
        self.visit(ctx.blok_kodu())
        self.dodaj_kod("    }")
        return None

    def visitPetla_warunkowa(self, ctx: SigmaScriptParser.Petla_warunkowaContext):
        warunek_c = ctx.wyrazenie_logiczne().getText().replace("oraz", "&&").replace("lub", "||").replace("prawda",
                                                                                                          "1").replace(
            "falsz", "0").replace("nie", "!")
        print(f"[Kompilator] Znalazłem pętlę warunkową (dopoki): {warunek_c}")
        self.dodaj_kod(f"    while ({warunek_c}) {{")
        self.visit(ctx.blok_kodu())
        self.dodaj_kod("    }")
        return None

    def visitInstrukcja_warunkowa(self, ctx: SigmaScriptParser.Instrukcja_warunkowaContext):
        warunek = ctx.wyrazenie_logiczne().getText().replace("oraz", "&&").replace("lub", "||").replace("prawda",
                                                                                                        "1").replace(
            "falsz", "0").replace("nie", "!")
        print(f"[Kompilator] Znalazłem instrukcję warunkową (jezeli): {warunek}")
        self.dodaj_kod(f"    if ({warunek}) {{")
        self.visit(ctx.blok_kodu(0))
        self.dodaj_kod("    }")
        if ctx.INACZEJ():
            self.dodaj_kod("    else {")
            self.visit(ctx.blok_kodu(1))
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
        return

    with open("wynik.c", "w", encoding='utf-8') as f:
        f.write(gotowy_kod_c)

    print("\n[Sukces] Wygenerowano kod docelowy w wynik.c")


if __name__ == '__main__':
    main()