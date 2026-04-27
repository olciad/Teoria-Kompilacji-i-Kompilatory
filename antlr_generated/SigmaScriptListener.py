# Generated from SigmaScript.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SigmaScriptParser import SigmaScriptParser
else:
    from SigmaScriptParser import SigmaScriptParser

# This class defines a complete listener for a parse tree produced by SigmaScriptParser.
class SigmaScriptListener(ParseTreeListener):

    # Enter a parse tree produced by SigmaScriptParser#program.
    def enterProgram(self, ctx:SigmaScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#program.
    def exitProgram(self, ctx:SigmaScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#definicja.
    def enterDefinicja(self, ctx:SigmaScriptParser.DefinicjaContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#definicja.
    def exitDefinicja(self, ctx:SigmaScriptParser.DefinicjaContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#definicja_struktury.
    def enterDefinicja_struktury(self, ctx:SigmaScriptParser.Definicja_strukturyContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#definicja_struktury.
    def exitDefinicja_struktury(self, ctx:SigmaScriptParser.Definicja_strukturyContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#definicja_funkcji.
    def enterDefinicja_funkcji(self, ctx:SigmaScriptParser.Definicja_funkcjiContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#definicja_funkcji.
    def exitDefinicja_funkcji(self, ctx:SigmaScriptParser.Definicja_funkcjiContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#parametry.
    def enterParametry(self, ctx:SigmaScriptParser.ParametryContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#parametry.
    def exitParametry(self, ctx:SigmaScriptParser.ParametryContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#parametr.
    def enterParametr(self, ctx:SigmaScriptParser.ParametrContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#parametr.
    def exitParametr(self, ctx:SigmaScriptParser.ParametrContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#typ_zwracany.
    def enterTyp_zwracany(self, ctx:SigmaScriptParser.Typ_zwracanyContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#typ_zwracany.
    def exitTyp_zwracany(self, ctx:SigmaScriptParser.Typ_zwracanyContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#typ.
    def enterTyp(self, ctx:SigmaScriptParser.TypContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#typ.
    def exitTyp(self, ctx:SigmaScriptParser.TypContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#wymiar_tablicy.
    def enterWymiar_tablicy(self, ctx:SigmaScriptParser.Wymiar_tablicyContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#wymiar_tablicy.
    def exitWymiar_tablicy(self, ctx:SigmaScriptParser.Wymiar_tablicyContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#blok_kodu.
    def enterBlok_kodu(self, ctx:SigmaScriptParser.Blok_koduContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#blok_kodu.
    def exitBlok_kodu(self, ctx:SigmaScriptParser.Blok_koduContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#instrukcja.
    def enterInstrukcja(self, ctx:SigmaScriptParser.InstrukcjaContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#instrukcja.
    def exitInstrukcja(self, ctx:SigmaScriptParser.InstrukcjaContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#polecenie_ruchu.
    def enterPolecenie_ruchu(self, ctx:SigmaScriptParser.Polecenie_ruchuContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#polecenie_ruchu.
    def exitPolecenie_ruchu(self, ctx:SigmaScriptParser.Polecenie_ruchuContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#polecenie_obrotu.
    def enterPolecenie_obrotu(self, ctx:SigmaScriptParser.Polecenie_obrotuContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#polecenie_obrotu.
    def exitPolecenie_obrotu(self, ctx:SigmaScriptParser.Polecenie_obrotuContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#petla.
    def enterPetla(self, ctx:SigmaScriptParser.PetlaContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#petla.
    def exitPetla(self, ctx:SigmaScriptParser.PetlaContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#petla_warunkowa.
    def enterPetla_warunkowa(self, ctx:SigmaScriptParser.Petla_warunkowaContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#petla_warunkowa.
    def exitPetla_warunkowa(self, ctx:SigmaScriptParser.Petla_warunkowaContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#instrukcja_warunkowa.
    def enterInstrukcja_warunkowa(self, ctx:SigmaScriptParser.Instrukcja_warunkowaContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#instrukcja_warunkowa.
    def exitInstrukcja_warunkowa(self, ctx:SigmaScriptParser.Instrukcja_warunkowaContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#wypisanie.
    def enterWypisanie(self, ctx:SigmaScriptParser.WypisanieContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#wypisanie.
    def exitWypisanie(self, ctx:SigmaScriptParser.WypisanieContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#deklaracja_zmiennej.
    def enterDeklaracja_zmiennej(self, ctx:SigmaScriptParser.Deklaracja_zmiennejContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#deklaracja_zmiennej.
    def exitDeklaracja_zmiennej(self, ctx:SigmaScriptParser.Deklaracja_zmiennejContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#przypisanie.
    def enterPrzypisanie(self, ctx:SigmaScriptParser.PrzypisanieContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#przypisanie.
    def exitPrzypisanie(self, ctx:SigmaScriptParser.PrzypisanieContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#instrukcja_zwrotu.
    def enterInstrukcja_zwrotu(self, ctx:SigmaScriptParser.Instrukcja_zwrotuContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#instrukcja_zwrotu.
    def exitInstrukcja_zwrotu(self, ctx:SigmaScriptParser.Instrukcja_zwrotuContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#odwolanie.
    def enterOdwolanie(self, ctx:SigmaScriptParser.OdwolanieContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#odwolanie.
    def exitOdwolanie(self, ctx:SigmaScriptParser.OdwolanieContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#wywolanie_funkcji.
    def enterWywolanie_funkcji(self, ctx:SigmaScriptParser.Wywolanie_funkcjiContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#wywolanie_funkcji.
    def exitWywolanie_funkcji(self, ctx:SigmaScriptParser.Wywolanie_funkcjiContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#argumenty.
    def enterArgumenty(self, ctx:SigmaScriptParser.ArgumentyContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#argumenty.
    def exitArgumenty(self, ctx:SigmaScriptParser.ArgumentyContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#inicjalizacja_tablicy.
    def enterInicjalizacja_tablicy(self, ctx:SigmaScriptParser.Inicjalizacja_tablicyContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#inicjalizacja_tablicy.
    def exitInicjalizacja_tablicy(self, ctx:SigmaScriptParser.Inicjalizacja_tablicyContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#wyrazenie_ogolne.
    def enterWyrazenie_ogolne(self, ctx:SigmaScriptParser.Wyrazenie_ogolneContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#wyrazenie_ogolne.
    def exitWyrazenie_ogolne(self, ctx:SigmaScriptParser.Wyrazenie_ogolneContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#wyrazenie_logiczne.
    def enterWyrazenie_logiczne(self, ctx:SigmaScriptParser.Wyrazenie_logiczneContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#wyrazenie_logiczne.
    def exitWyrazenie_logiczne(self, ctx:SigmaScriptParser.Wyrazenie_logiczneContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#operator_rel.
    def enterOperator_rel(self, ctx:SigmaScriptParser.Operator_relContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#operator_rel.
    def exitOperator_rel(self, ctx:SigmaScriptParser.Operator_relContext):
        pass


    # Enter a parse tree produced by SigmaScriptParser#wyrazenie_arytmetyczne.
    def enterWyrazenie_arytmetyczne(self, ctx:SigmaScriptParser.Wyrazenie_arytmetyczneContext):
        pass

    # Exit a parse tree produced by SigmaScriptParser#wyrazenie_arytmetyczne.
    def exitWyrazenie_arytmetyczne(self, ctx:SigmaScriptParser.Wyrazenie_arytmetyczneContext):
        pass



del SigmaScriptParser