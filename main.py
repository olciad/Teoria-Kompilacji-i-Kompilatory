import sys
from antlr4 import *
from antlr_generated.SigmaScriptLexer import SigmaScriptLexer
from antlr_generated.SigmaScriptParser import SigmaScriptParser
from antlr_generated.SigmaScriptVisitor import SigmaScriptVisitor


# Nasza własna klasa kompilatora, nadpisująca domyślnego Visitora
class KompilatorVisitor(SigmaScriptVisitor):

    def __init__(self):
        # Tutaj będziemy zbierać wygenerowany kod w C
        self.kod_c = []

    # Odwiedzanie węzła reguły 'program'
    def visitProgram(self, ctx: SigmaScriptParser.ProgramContext):
        print("[Kompilator] Rozpoczynam analizę programu...")
        self.kod_c.append("#include <stdio.h>\n")
        self.kod_c.append("int main() {")

        # Odwiedź wszystkie dzieci (instrukcje w programie)
        self.visitChildren(ctx)

        self.kod_c.append("    return 0;\n}")
        return "".join(self.kod_c)

    # Odwiedzanie węzła reguły 'wypisanie'
    def visitWypisanie(self, ctx: SigmaScriptParser.WypisanieContext):
        # Pobieramy to, co zostało wpisane po słowie 'wypisz'
        wyrazenie = ctx.wyrazenie_ogolne().getText()
        print(f"[Kompilator] Znalazłem instrukcję WYPISZ: {wyrazenie}")

        # Generujemy odpowiednik w C (dla uproszczenia traktujemy jako string/liczbę bezpośrednio)
        # UWAGA: W pełnej wersji będziesz musiał sprawdzić typ, żeby dobrać %d, %f lub %s!
        self.kod_c.append(f'    printf("%s\\n", {wyrazenie});')

        return self.visitChildren(ctx)

    # Odwiedzanie węzła reguły 'deklaracja_zmiennej'
    def visitDeklaracja_zmiennej(self, ctx: SigmaScriptParser.Deklaracja_zmiennejContext):
        typ = ctx.typ().getText()
        nazwa = ctx.IDENT().getText()

        # Pobranie przypisywanej wartości (jeśli istnieje)
        wartosc = ""
        if ctx.wyrazenie_ogolne():
            wartosc = " = " + ctx.wyrazenie_ogolne().getText()

        print(f"[Kompilator] Deklaracja zmiennej: {typ} {nazwa}{wartosc}")

        # Prymitywne tłumaczenie typów na C
        typ_c = "int"
        if typ == "rzeczywista":
            typ_c = "float"
        elif typ == "logiczna":
            typ_c = "int"  # W C bool to często po prostu int
        elif typ == "tekst":
            typ_c = "char*"

        self.kod_c.append(f'    {typ_c} {nazwa}{wartosc};')

        return self.visitChildren(ctx)


def main():
    # Sprawdzanie, czy podano plik źródłowy
    if len(sys.argv) < 2:
        print("Użycie: python main.py <plik.sigma>")
        return

    plik_wejsciowy = sys.argv[1]

    # 1. Wczytanie pliku źródłowego
    input_stream = FileStream(plik_wejsciowy, encoding='utf-8')

    # 2. Analiza leksykalna (Lexer)
    lexer = SigmaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # 3. Analiza składniowa (Parser)
    parser = SigmaScriptParser(stream)
    tree = parser.program()  # Rozpoczynamy od reguły 'program'

    # 4. Przejście po drzewie AST (Visitor)
    visitor = KompilatorVisitor()
    gotowy_kod_c = visitor.visit(tree)

    # 5. Zapisanie wygenerowanego kodu C do pliku
    with open("wynik.c", "w", encoding='utf-8') as f:
        f.write(gotowy_kod_c)

    print("\n[Sukces] Wygenerowano plik wynik.c!")
    print("--- ZAWARTOSC PLIKU C ---")
    print(gotowy_kod_c)


if __name__ == '__main__':
    main()