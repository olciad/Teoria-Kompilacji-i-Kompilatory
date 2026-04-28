import sys
from antlr4 import *
from antlr_generated.SigmaScriptLexer import SigmaScriptLexer
from antlr_generated.SigmaScriptParser import SigmaScriptParser
from antlr_generated.SigmaScriptVisitor import SigmaScriptVisitor

# biblioteka runtime
RUNTIME_C = """#include <stdio.h>
#include <math.h>

FILE *svg_file;
float _x = 500.0; // Startujemy na środku płótna 1000x1000
float _y = 500.0;
float _kat = -90.0; // -90 stopni oznacza, że na początku patrzymy "w górę" ekranu

void _init_svg() {
    svg_file = fopen("wynik.svg", "w");
    fprintf(svg_file, "<svg width=\\"1000\\" height=\\"1000\\" xmlns=\\"http://www.w3.org/2000/svg\\">\\n");
    fprintf(svg_file, "<rect width=\\"100%%\\" height=\\"100%%\\" fill=\\"#f0f0f0\\"/>\\n"); // Jasnoszare tło
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

    // Rysujemy linię w SVG
    fprintf(svg_file, "<line x1=\\"%.2f\\" y1=\\"%.2f\\" x2=\\"%.2f\\" y2=\\"%.2f\\" stroke=\\"#2c3e50\\" stroke-width=\\"3\\" stroke-linecap=\\"round\\" />\\n", _x, _y, new_x, new_y);

    // Aktualizujemy pozycję
    _x = new_x;
    _y = new_y;
}

void _obroc(float zmiana_kata) {
    _kat += zmiana_kata;
}
"""


class KompilatorVisitor(SigmaScriptVisitor):
    def __init__(self):
        self.kod_globalny = []
        self.kod_main = []
        self.w_funkcji = False

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
                typ_c = typ_bazowy  # Pozwala nawet na struktury w strukturach!

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

        if "calkowita" in typ_bazowy:
            typ_c = "int"
        elif "rzeczywista" in typ_bazowy:
            typ_c = "float"
        elif "logiczna" in typ_bazowy:
            typ_c = "int"
        else:
            typ_c = typ_bazowy  # Obsługa inicjalizacji struktury: Dron moj_dron

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
        self.dodaj_kod(
            f"    {ctx.odwolanie().getText()} = {ctx.wyrazenie_ogolne().getText().replace('prawda', '1').replace('falsz', '0')};")
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
        print("Użycie: python main.py <plik.ss>")
        return

    plik_wejsciowy = sys.argv[1]
    input_stream = FileStream(plik_wejsciowy, encoding='utf-8')
    lexer = SigmaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SigmaScriptParser(stream)
    tree = parser.program()

    visitor = KompilatorVisitor()
    gotowy_kod_c = visitor.visit(tree)

    with open("wynik.c", "w", encoding='utf-8') as f:
        f.write(gotowy_kod_c)

    print("\n[Sukces] Wygenerowano kod docelowy w wynik.c")


if __name__ == '__main__':
    main()