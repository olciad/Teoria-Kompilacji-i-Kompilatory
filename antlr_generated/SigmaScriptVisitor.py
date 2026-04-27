# Generated from SigmaScript.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SigmaScriptParser import SigmaScriptParser
else:
    from SigmaScriptParser import SigmaScriptParser

# This class defines a complete generic visitor for a parse tree produced by SigmaScriptParser.

class SigmaScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SigmaScriptParser#program.
    def visitProgram(self, ctx:SigmaScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#definicja.
    def visitDefinicja(self, ctx:SigmaScriptParser.DefinicjaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#definicja_struktury.
    def visitDefinicja_struktury(self, ctx:SigmaScriptParser.Definicja_strukturyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#definicja_funkcji.
    def visitDefinicja_funkcji(self, ctx:SigmaScriptParser.Definicja_funkcjiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#parametry.
    def visitParametry(self, ctx:SigmaScriptParser.ParametryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#parametr.
    def visitParametr(self, ctx:SigmaScriptParser.ParametrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#typ_zwracany.
    def visitTyp_zwracany(self, ctx:SigmaScriptParser.Typ_zwracanyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#typ.
    def visitTyp(self, ctx:SigmaScriptParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#wymiar_tablicy.
    def visitWymiar_tablicy(self, ctx:SigmaScriptParser.Wymiar_tablicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#blok_kodu.
    def visitBlok_kodu(self, ctx:SigmaScriptParser.Blok_koduContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#instrukcja.
    def visitInstrukcja(self, ctx:SigmaScriptParser.InstrukcjaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#polecenie_ruchu.
    def visitPolecenie_ruchu(self, ctx:SigmaScriptParser.Polecenie_ruchuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#polecenie_obrotu.
    def visitPolecenie_obrotu(self, ctx:SigmaScriptParser.Polecenie_obrotuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#petla.
    def visitPetla(self, ctx:SigmaScriptParser.PetlaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#petla_warunkowa.
    def visitPetla_warunkowa(self, ctx:SigmaScriptParser.Petla_warunkowaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#instrukcja_warunkowa.
    def visitInstrukcja_warunkowa(self, ctx:SigmaScriptParser.Instrukcja_warunkowaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#wypisanie.
    def visitWypisanie(self, ctx:SigmaScriptParser.WypisanieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#deklaracja_zmiennej.
    def visitDeklaracja_zmiennej(self, ctx:SigmaScriptParser.Deklaracja_zmiennejContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#przypisanie.
    def visitPrzypisanie(self, ctx:SigmaScriptParser.PrzypisanieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#instrukcja_zwrotu.
    def visitInstrukcja_zwrotu(self, ctx:SigmaScriptParser.Instrukcja_zwrotuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#odwolanie.
    def visitOdwolanie(self, ctx:SigmaScriptParser.OdwolanieContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#wywolanie_funkcji.
    def visitWywolanie_funkcji(self, ctx:SigmaScriptParser.Wywolanie_funkcjiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#argumenty.
    def visitArgumenty(self, ctx:SigmaScriptParser.ArgumentyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#inicjalizacja_tablicy.
    def visitInicjalizacja_tablicy(self, ctx:SigmaScriptParser.Inicjalizacja_tablicyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#wyrazenie_ogolne.
    def visitWyrazenie_ogolne(self, ctx:SigmaScriptParser.Wyrazenie_ogolneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#wyrazenie_logiczne.
    def visitWyrazenie_logiczne(self, ctx:SigmaScriptParser.Wyrazenie_logiczneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#operator_rel.
    def visitOperator_rel(self, ctx:SigmaScriptParser.Operator_relContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SigmaScriptParser#wyrazenie_arytmetyczne.
    def visitWyrazenie_arytmetyczne(self, ctx:SigmaScriptParser.Wyrazenie_arytmetyczneContext):
        return self.visitChildren(ctx)



del SigmaScriptParser