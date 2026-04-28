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
        self.kod_c = []

    # 1. Wejście do programu
    def visitProgram(self, ctx: SigmaScriptParser.ProgramContext):
        print("[Kompilator] Rozpoczynam analizę programu...")

        # Wklejamy nasz runtime na górę pliku C
        self.kod_c.append(RUNTIME_C)
        self.kod_c.append("\nint main() {")
        self.kod_c.append("    _init_svg(); // Ukryta inicjalizacja płótna\n")

        # Odwiedzamy instrukcje napisane przez użytkownika
        self.visitChildren(ctx)

        # Zamykamy plik SVG i program C
        self.kod_c.append("\n    _zapisz_svg(); // Ukryte zapisanie pliku")
        self.kod_c.append("    return 0;\n}")
        return "".join(self.kod_c)

    # 2. Obsługa polecenia NAPRZOD
    def visitPolecenie_ruchu(self, ctx: SigmaScriptParser.Polecenie_ruchuContext):
        # Pobieramy to co jest po słowie "naprzod".
        # Dzięki ".getText()" tekst taki jak "50" lub "10+5" zostanie po prostu skopiowany do C
        dystans = ctx.wyrazenie_arytmetyczne().getText()
        print(f"[Kompilator] Znalazłem ruch: naprzod {dystans}")
        self.kod_c.append(f'    _naprzod({dystans});')
        return None

    # 3. Obsługa polecenia OBROC
    def visitPolecenie_obrotu(self, ctx: SigmaScriptParser.Polecenie_obrotuContext):
        kat = ctx.wyrazenie_arytmetyczne().getText()
        print(f"[Kompilator] Znalazłem obrót: obroc {kat}")
        self.kod_c.append(f'    _obroc({kat});')
        return None

    # 4. Obsługa pętli POWTORZ
    def visitPetla(self, ctx: SigmaScriptParser.PetlaContext):
        # Pobieramy liczbę powtórzeń (np. "4")
        ile_razy = ctx.wyrazenie_arytmetyczne().getText()
        print(f"[Kompilator] Znalazłem pętlę: powtorz {ile_razy}")

        # Używamy id(ctx), żeby każda pętla miała unikalną nazwę zmiennej (np. _i_12345).
        # Dzięki temu pętle w SigmaScript będzie można bezpiecznie zagnieżdżać!
        zmienna_petli = f"_i_{id(ctx)}"

        # Otwieramy pętlę for w C
        self.kod_c.append(f"    for(int {zmienna_petli} = 0; {zmienna_petli} < (int)({ile_razy}); {zmienna_petli}++) {{")

        # Odwiedzamy TYLKO blok kodu (instrukcje wewnątrz klamer)
        self.visit(ctx.blok_kodu())

        # Zamykamy klamrę pętli w C
        self.kod_c.append("    }")
        return None

    # 5. Obsługa deklaracji zmiennej (np. calkowita x = 10)
    def visitDeklaracja_zmiennej(self, ctx: SigmaScriptParser.Deklaracja_zmiennejContext):
        typ_sigma = ctx.typ().getText()
        nazwa = ctx.IDENT().getText()

        # Tłumaczenie typów z SigmaScript na C
        if "calkowita" in typ_sigma:
            typ_c = "int"
        elif "rzeczywista" in typ_sigma:
            typ_c = "float"
        elif "logiczna" in typ_sigma:
            typ_c = "int"
        elif "tekst" in typ_sigma:
            typ_c = "char*"
        else:
            typ_c = "int"  # Fallback np. dla własnych struktur

        # Jeśli zmienna ma od razu przypisaną wartość
        if ctx.wyrazenie_ogolne():
            wartosc = ctx.wyrazenie_ogolne().getText()
            # Tłumaczenie polskich słów logicznych na wartości dla C
            wartosc = wartosc.replace("prawda", "1").replace("falsz", "0")
            self.kod_c.append(f"    {typ_c} {nazwa} = {wartosc};")
        else:
            self.kod_c.append(f"    {typ_c} {nazwa};")

        return None

    # 6. Obsługa przypisania (np. ustaw x = 20)
    def visitPrzypisanie(self, ctx: SigmaScriptParser.PrzypisanieContext):
        odwolanie = ctx.odwolanie().getText()
        wartosc = ctx.wyrazenie_ogolne().getText()
        wartosc = wartosc.replace("prawda", "1").replace("falsz", "0")
        self.kod_c.append(f"    {odwolanie} = {wartosc};")
        return None

    # 7. Obsługa instrukcji warunkowej JEZELI ... INACZEJ
    def visitInstrukcja_warunkowa(self, ctx: SigmaScriptParser.Instrukcja_warunkowaContext):
        # Pobieramy polski warunek logiczny z kodu
        warunek_sigma = ctx.wyrazenie_logiczne().getText()

        # Szybkie tłumaczenie polskich operatorów na C
        warunek_c = warunek_sigma.replace("oraz", "&&") \
            .replace("lub", "||") \
            .replace("prawda", "1") \
            .replace("falsz", "0") \
            .replace("nie", "!")

        # Otwieramy IF w C
        self.kod_c.append(f"    if ({warunek_c}) {{")

        # Odwiedzamy pierwszy blok kodu (wykona się, gdy prawda)
        self.visit(ctx.blok_kodu(0))
        self.kod_c.append("    }")

        # Jeśli uczeń dopisał słowo "inaczej" (else), odwiedzamy drugi blok kodu
        if ctx.INACZEJ():
            self.kod_c.append("    else {")
            self.visit(ctx.blok_kodu(1))
            self.kod_c.append("    }")

        return None
    # (Zostawiamy na razie puste metody na zmienne, żeby uniknąć błędów)
    def visitWypisanie(self, ctx: SigmaScriptParser.WypisanieContext):
        wyrazenie = ctx.wyrazenie_ogolne().getText()
        self.kod_c.append(f'    printf("%s\\n", {wyrazenie});')
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