# Generated from SigmaScript.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,5,0,60,8,0,10,0,12,0,63,9,0,1,0,1,0,1,1,
        1,1,1,1,3,1,70,8,1,1,2,1,2,1,2,1,2,5,2,76,8,2,10,2,12,2,79,9,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,88,8,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,
        96,8,4,10,4,12,4,99,9,4,1,5,1,5,1,5,1,6,1,6,3,6,106,8,6,1,7,1,7,
        3,7,110,8,7,1,8,1,8,3,8,114,8,8,1,8,1,8,1,9,1,9,5,9,120,8,9,10,9,
        12,9,123,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,138,8,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,3,16,165,8,16,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,3,18,174,8,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,3,20,183,8,
        20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,192,8,21,10,21,12,21,
        195,9,21,1,22,1,22,1,22,3,22,200,8,22,1,22,1,22,1,22,1,22,1,22,5,
        22,207,8,22,10,22,12,22,210,9,22,1,23,1,23,1,23,5,23,215,8,23,10,
        23,12,23,218,9,23,1,24,1,24,3,24,222,8,24,1,24,1,24,1,25,1,25,1,
        25,3,25,229,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,247,8,26,1,26,1,26,1,26,1,
        26,1,26,1,26,1,26,1,26,1,26,5,26,258,8,26,10,26,12,26,261,9,26,1,
        27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,3,28,277,8,28,1,28,1,28,1,28,1,28,1,28,1,28,5,28,285,8,28,10,
        28,12,28,288,9,28,1,28,0,2,52,56,29,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,6,2,0,1,
        4,45,45,1,0,13,14,1,0,29,30,1,0,29,34,1,0,26,27,1,0,24,25,309,0,
        61,1,0,0,0,2,69,1,0,0,0,4,71,1,0,0,0,6,82,1,0,0,0,8,92,1,0,0,0,10,
        100,1,0,0,0,12,105,1,0,0,0,14,107,1,0,0,0,16,111,1,0,0,0,18,117,
        1,0,0,0,20,137,1,0,0,0,22,139,1,0,0,0,24,142,1,0,0,0,26,145,1,0,
        0,0,28,147,1,0,0,0,30,151,1,0,0,0,32,157,1,0,0,0,34,166,1,0,0,0,
        36,169,1,0,0,0,38,175,1,0,0,0,40,180,1,0,0,0,42,184,1,0,0,0,44,196,
        1,0,0,0,46,211,1,0,0,0,48,219,1,0,0,0,50,228,1,0,0,0,52,246,1,0,
        0,0,54,262,1,0,0,0,56,276,1,0,0,0,58,60,3,2,1,0,59,58,1,0,0,0,60,
        63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,
        0,64,65,5,0,0,1,65,1,1,0,0,0,66,70,3,20,10,0,67,70,3,4,2,0,68,70,
        3,6,3,0,69,66,1,0,0,0,69,67,1,0,0,0,69,68,1,0,0,0,70,3,1,0,0,0,71,
        72,5,6,0,0,72,73,5,45,0,0,73,77,5,37,0,0,74,76,3,36,18,0,75,74,1,
        0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,
        77,1,0,0,0,80,81,5,38,0,0,81,5,1,0,0,0,82,83,5,7,0,0,83,84,3,12,
        6,0,84,85,5,45,0,0,85,87,5,35,0,0,86,88,3,8,4,0,87,86,1,0,0,0,87,
        88,1,0,0,0,88,89,1,0,0,0,89,90,5,36,0,0,90,91,3,18,9,0,91,7,1,0,
        0,0,92,97,3,10,5,0,93,94,5,42,0,0,94,96,3,10,5,0,95,93,1,0,0,0,96,
        99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,9,1,0,0,0,99,97,1,0,0,
        0,100,101,3,14,7,0,101,102,5,45,0,0,102,11,1,0,0,0,103,106,3,14,
        7,0,104,106,5,5,0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,13,1,0,0,
        0,107,109,7,0,0,0,108,110,3,16,8,0,109,108,1,0,0,0,109,110,1,0,0,
        0,110,15,1,0,0,0,111,113,5,39,0,0,112,114,5,43,0,0,113,112,1,0,0,
        0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,5,40,0,0,116,17,1,0,0,
        0,117,121,5,37,0,0,118,120,3,20,10,0,119,118,1,0,0,0,120,123,1,0,
        0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,
        0,0,124,125,5,38,0,0,125,19,1,0,0,0,126,138,3,22,11,0,127,138,3,
        24,12,0,128,138,3,26,13,0,129,138,3,28,14,0,130,138,3,30,15,0,131,
        138,3,32,16,0,132,138,3,34,17,0,133,138,3,36,18,0,134,138,3,38,19,
        0,135,138,3,40,20,0,136,138,3,44,22,0,137,126,1,0,0,0,137,127,1,
        0,0,0,137,128,1,0,0,0,137,129,1,0,0,0,137,130,1,0,0,0,137,131,1,
        0,0,0,137,132,1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,135,1,
        0,0,0,137,136,1,0,0,0,138,21,1,0,0,0,139,140,5,11,0,0,140,141,3,
        56,28,0,141,23,1,0,0,0,142,143,5,12,0,0,143,144,3,56,28,0,144,25,
        1,0,0,0,145,146,7,1,0,0,146,27,1,0,0,0,147,148,5,15,0,0,148,149,
        3,56,28,0,149,150,3,18,9,0,150,29,1,0,0,0,151,152,5,16,0,0,152,153,
        5,35,0,0,153,154,3,52,26,0,154,155,5,36,0,0,155,156,3,18,9,0,156,
        31,1,0,0,0,157,158,5,17,0,0,158,159,5,35,0,0,159,160,3,52,26,0,160,
        161,5,36,0,0,161,164,3,18,9,0,162,163,5,18,0,0,163,165,3,18,9,0,
        164,162,1,0,0,0,164,165,1,0,0,0,165,33,1,0,0,0,166,167,5,19,0,0,
        167,168,3,50,25,0,168,35,1,0,0,0,169,170,3,14,7,0,170,173,5,45,0,
        0,171,172,5,28,0,0,172,174,3,50,25,0,173,171,1,0,0,0,173,174,1,0,
        0,0,174,37,1,0,0,0,175,176,5,20,0,0,176,177,3,42,21,0,177,178,5,
        28,0,0,178,179,3,50,25,0,179,39,1,0,0,0,180,182,5,8,0,0,181,183,
        3,50,25,0,182,181,1,0,0,0,182,183,1,0,0,0,183,41,1,0,0,0,184,193,
        5,45,0,0,185,186,5,39,0,0,186,187,3,56,28,0,187,188,5,40,0,0,188,
        192,1,0,0,0,189,190,5,41,0,0,190,192,5,45,0,0,191,185,1,0,0,0,191,
        189,1,0,0,0,192,195,1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,
        43,1,0,0,0,195,193,1,0,0,0,196,197,5,45,0,0,197,199,5,35,0,0,198,
        200,3,46,23,0,199,198,1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,
        208,5,36,0,0,202,203,5,39,0,0,203,204,3,56,28,0,204,205,5,40,0,0,
        205,207,1,0,0,0,206,202,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,
        208,209,1,0,0,0,209,45,1,0,0,0,210,208,1,0,0,0,211,216,3,50,25,0,
        212,213,5,42,0,0,213,215,3,50,25,0,214,212,1,0,0,0,215,218,1,0,0,
        0,216,214,1,0,0,0,216,217,1,0,0,0,217,47,1,0,0,0,218,216,1,0,0,0,
        219,221,5,39,0,0,220,222,3,46,23,0,221,220,1,0,0,0,221,222,1,0,0,
        0,222,223,1,0,0,0,223,224,5,40,0,0,224,49,1,0,0,0,225,229,3,56,28,
        0,226,229,3,52,26,0,227,229,3,48,24,0,228,225,1,0,0,0,228,226,1,
        0,0,0,228,227,1,0,0,0,229,51,1,0,0,0,230,231,6,26,-1,0,231,232,5,
        35,0,0,232,233,3,52,26,0,233,234,5,36,0,0,234,247,1,0,0,0,235,247,
        5,9,0,0,236,247,5,10,0,0,237,247,5,46,0,0,238,247,3,44,22,0,239,
        247,3,42,21,0,240,241,3,56,28,0,241,242,3,54,27,0,242,243,3,56,28,
        0,243,247,1,0,0,0,244,245,5,23,0,0,245,247,3,52,26,3,246,230,1,0,
        0,0,246,235,1,0,0,0,246,236,1,0,0,0,246,237,1,0,0,0,246,238,1,0,
        0,0,246,239,1,0,0,0,246,240,1,0,0,0,246,244,1,0,0,0,247,259,1,0,
        0,0,248,249,10,4,0,0,249,250,7,2,0,0,250,258,3,52,26,5,251,252,10,
        2,0,0,252,253,5,21,0,0,253,258,3,52,26,3,254,255,10,1,0,0,255,256,
        5,22,0,0,256,258,3,52,26,2,257,248,1,0,0,0,257,251,1,0,0,0,257,254,
        1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,53,1,
        0,0,0,261,259,1,0,0,0,262,263,7,3,0,0,263,55,1,0,0,0,264,265,6,28,
        -1,0,265,266,5,35,0,0,266,267,3,56,28,0,267,268,5,36,0,0,268,277,
        1,0,0,0,269,277,3,44,22,0,270,277,3,42,21,0,271,277,5,43,0,0,272,
        277,5,44,0,0,273,274,5,25,0,0,274,277,3,56,28,4,275,277,5,46,0,0,
        276,264,1,0,0,0,276,269,1,0,0,0,276,270,1,0,0,0,276,271,1,0,0,0,
        276,272,1,0,0,0,276,273,1,0,0,0,276,275,1,0,0,0,277,286,1,0,0,0,
        278,279,10,3,0,0,279,280,7,4,0,0,280,285,3,56,28,4,281,282,10,2,
        0,0,282,283,7,5,0,0,283,285,3,56,28,3,284,278,1,0,0,0,284,281,1,
        0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,57,1,0,
        0,0,288,286,1,0,0,0,26,61,69,77,87,97,105,109,113,121,137,164,173,
        182,191,193,199,208,216,221,228,246,257,259,276,284,286
    ]

class SigmaScriptParser ( Parser ):

    grammarFileName = "SigmaScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'calkowita'", "'rzeczywista'", "'logiczna'", 
                     "'tekst'", "'pusta'", "'struktura'", "'funkcja'", "'zwroc'", 
                     "'prawda'", "'falsz'", "'naprzod'", "'obroc'", "'podnies'", 
                     "'opusc'", "'powtorz'", "'dopoki'", "'jezeli'", "'inaczej'", 
                     "'wypisz'", "'ustaw'", "'oraz'", "'lub'", "'nie'", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "CALKOWITA", "RZECZYWISTA", "LOGICZNA", 
                      "TEKST_TYP", "PUSTA", "STRUKTURA", "FUNKCJA", "ZWROC", 
                      "PRAWDA", "FALSZ", "NAPRZOD", "OBROC", "PODNIES", 
                      "OPUSC", "POWTORZ", "DOPOKI", "JEZELI", "INACZEJ", 
                      "WYPISZ", "USTAW", "ORAZ", "LUB", "NIE", "PLUS", "MINUS", 
                      "RAZY", "PRZEZ", "PRZYPIS", "ROWNY", "ROZNY", "MNIEJ_ROWN", 
                      "WIEC_ROWN", "MNIEJSZY", "WIEKSZY", "L_NAWIAS", "P_NAWIAS", 
                      "L_KLAMRA", "P_KLAMRA", "L_KWADRAT", "P_KWADRAT", 
                      "KROPKA", "PRZECINEK", "LICZ_CALK", "LICZ_RZECZ", 
                      "IDENT", "TEKST", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_definicja = 1
    RULE_definicja_struktury = 2
    RULE_definicja_funkcji = 3
    RULE_parametry = 4
    RULE_parametr = 5
    RULE_typ_zwracany = 6
    RULE_typ = 7
    RULE_wymiar_tablicy = 8
    RULE_blok_kodu = 9
    RULE_instrukcja = 10
    RULE_polecenie_ruchu = 11
    RULE_polecenie_obrotu = 12
    RULE_polecenie_pisaka = 13
    RULE_petla = 14
    RULE_petla_warunkowa = 15
    RULE_instrukcja_warunkowa = 16
    RULE_wypisanie = 17
    RULE_deklaracja_zmiennej = 18
    RULE_przypisanie = 19
    RULE_instrukcja_zwrotu = 20
    RULE_odwolanie = 21
    RULE_wywolanie_funkcji = 22
    RULE_argumenty = 23
    RULE_inicjalizacja_tablicy = 24
    RULE_wyrazenie_ogolne = 25
    RULE_wyrazenie_logiczne = 26
    RULE_operator_rel = 27
    RULE_wyrazenie_arytmetyczne = 28

    ruleNames =  [ "program", "definicja", "definicja_struktury", "definicja_funkcji", 
                   "parametry", "parametr", "typ_zwracany", "typ", "wymiar_tablicy", 
                   "blok_kodu", "instrukcja", "polecenie_ruchu", "polecenie_obrotu", 
                   "polecenie_pisaka", "petla", "petla_warunkowa", "instrukcja_warunkowa", 
                   "wypisanie", "deklaracja_zmiennej", "przypisanie", "instrukcja_zwrotu", 
                   "odwolanie", "wywolanie_funkcji", "argumenty", "inicjalizacja_tablicy", 
                   "wyrazenie_ogolne", "wyrazenie_logiczne", "operator_rel", 
                   "wyrazenie_arytmetyczne" ]

    EOF = Token.EOF
    CALKOWITA=1
    RZECZYWISTA=2
    LOGICZNA=3
    TEKST_TYP=4
    PUSTA=5
    STRUKTURA=6
    FUNKCJA=7
    ZWROC=8
    PRAWDA=9
    FALSZ=10
    NAPRZOD=11
    OBROC=12
    PODNIES=13
    OPUSC=14
    POWTORZ=15
    DOPOKI=16
    JEZELI=17
    INACZEJ=18
    WYPISZ=19
    USTAW=20
    ORAZ=21
    LUB=22
    NIE=23
    PLUS=24
    MINUS=25
    RAZY=26
    PRZEZ=27
    PRZYPIS=28
    ROWNY=29
    ROZNY=30
    MNIEJ_ROWN=31
    WIEC_ROWN=32
    MNIEJSZY=33
    WIEKSZY=34
    L_NAWIAS=35
    P_NAWIAS=36
    L_KLAMRA=37
    P_KLAMRA=38
    L_KWADRAT=39
    P_KWADRAT=40
    KROPKA=41
    PRZECINEK=42
    LICZ_CALK=43
    LICZ_RZECZ=44
    IDENT=45
    TEKST=46
    WS=47
    COMMENT=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SigmaScriptParser.EOF, 0)

        def definicja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.DefinicjaContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.DefinicjaContext,i)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SigmaScriptParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184373922270) != 0):
                self.state = 58
                self.definicja()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(SigmaScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefinicjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrukcja(self):
            return self.getTypedRuleContext(SigmaScriptParser.InstrukcjaContext,0)


        def definicja_struktury(self):
            return self.getTypedRuleContext(SigmaScriptParser.Definicja_strukturyContext,0)


        def definicja_funkcji(self):
            return self.getTypedRuleContext(SigmaScriptParser.Definicja_funkcjiContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_definicja

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicja" ):
                listener.enterDefinicja(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicja" ):
                listener.exitDefinicja(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicja" ):
                return visitor.visitDefinicja(self)
            else:
                return visitor.visitChildren(self)




    def definicja(self):

        localctx = SigmaScriptParser.DefinicjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_definicja)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 8, 11, 12, 13, 14, 15, 16, 17, 19, 20, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.instrukcja()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.definicja_struktury()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.definicja_funkcji()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definicja_strukturyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUKTURA(self):
            return self.getToken(SigmaScriptParser.STRUKTURA, 0)

        def IDENT(self):
            return self.getToken(SigmaScriptParser.IDENT, 0)

        def L_KLAMRA(self):
            return self.getToken(SigmaScriptParser.L_KLAMRA, 0)

        def P_KLAMRA(self):
            return self.getToken(SigmaScriptParser.P_KLAMRA, 0)

        def deklaracja_zmiennej(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Deklaracja_zmiennejContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Deklaracja_zmiennejContext,i)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_definicja_struktury

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicja_struktury" ):
                listener.enterDefinicja_struktury(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicja_struktury" ):
                listener.exitDefinicja_struktury(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicja_struktury" ):
                return visitor.visitDefinicja_struktury(self)
            else:
                return visitor.visitChildren(self)




    def definicja_struktury(self):

        localctx = SigmaScriptParser.Definicja_strukturyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definicja_struktury)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(SigmaScriptParser.STRUKTURA)
            self.state = 72
            self.match(SigmaScriptParser.IDENT)
            self.state = 73
            self.match(SigmaScriptParser.L_KLAMRA)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372088862) != 0):
                self.state = 74
                self.deklaracja_zmiennej()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(SigmaScriptParser.P_KLAMRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definicja_funkcjiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNKCJA(self):
            return self.getToken(SigmaScriptParser.FUNKCJA, 0)

        def typ_zwracany(self):
            return self.getTypedRuleContext(SigmaScriptParser.Typ_zwracanyContext,0)


        def IDENT(self):
            return self.getToken(SigmaScriptParser.IDENT, 0)

        def L_NAWIAS(self):
            return self.getToken(SigmaScriptParser.L_NAWIAS, 0)

        def P_NAWIAS(self):
            return self.getToken(SigmaScriptParser.P_NAWIAS, 0)

        def blok_kodu(self):
            return self.getTypedRuleContext(SigmaScriptParser.Blok_koduContext,0)


        def parametry(self):
            return self.getTypedRuleContext(SigmaScriptParser.ParametryContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_definicja_funkcji

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicja_funkcji" ):
                listener.enterDefinicja_funkcji(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicja_funkcji" ):
                listener.exitDefinicja_funkcji(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicja_funkcji" ):
                return visitor.visitDefinicja_funkcji(self)
            else:
                return visitor.visitChildren(self)




    def definicja_funkcji(self):

        localctx = SigmaScriptParser.Definicja_funkcjiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_definicja_funkcji)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(SigmaScriptParser.FUNKCJA)
            self.state = 83
            self.typ_zwracany()
            self.state = 84
            self.match(SigmaScriptParser.IDENT)
            self.state = 85
            self.match(SigmaScriptParser.L_NAWIAS)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372088862) != 0):
                self.state = 86
                self.parametry()


            self.state = 89
            self.match(SigmaScriptParser.P_NAWIAS)
            self.state = 90
            self.blok_kodu()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.ParametrContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.ParametrContext,i)


        def PRZECINEK(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.PRZECINEK)
            else:
                return self.getToken(SigmaScriptParser.PRZECINEK, i)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_parametry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametry" ):
                listener.enterParametry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametry" ):
                listener.exitParametry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametry" ):
                return visitor.visitParametry(self)
            else:
                return visitor.visitChildren(self)




    def parametry(self):

        localctx = SigmaScriptParser.ParametryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parametry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.parametr()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 93
                self.match(SigmaScriptParser.PRZECINEK)
                self.state = 94
                self.parametr()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(SigmaScriptParser.TypContext,0)


        def IDENT(self):
            return self.getToken(SigmaScriptParser.IDENT, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_parametr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametr" ):
                listener.enterParametr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametr" ):
                listener.exitParametr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametr" ):
                return visitor.visitParametr(self)
            else:
                return visitor.visitChildren(self)




    def parametr(self):

        localctx = SigmaScriptParser.ParametrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parametr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.typ()
            self.state = 101
            self.match(SigmaScriptParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typ_zwracanyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(SigmaScriptParser.TypContext,0)


        def PUSTA(self):
            return self.getToken(SigmaScriptParser.PUSTA, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_typ_zwracany

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp_zwracany" ):
                listener.enterTyp_zwracany(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp_zwracany" ):
                listener.exitTyp_zwracany(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp_zwracany" ):
                return visitor.visitTyp_zwracany(self)
            else:
                return visitor.visitChildren(self)




    def typ_zwracany(self):

        localctx = SigmaScriptParser.Typ_zwracanyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typ_zwracany)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.typ()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(SigmaScriptParser.PUSTA)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALKOWITA(self):
            return self.getToken(SigmaScriptParser.CALKOWITA, 0)

        def RZECZYWISTA(self):
            return self.getToken(SigmaScriptParser.RZECZYWISTA, 0)

        def LOGICZNA(self):
            return self.getToken(SigmaScriptParser.LOGICZNA, 0)

        def TEKST_TYP(self):
            return self.getToken(SigmaScriptParser.TEKST_TYP, 0)

        def IDENT(self):
            return self.getToken(SigmaScriptParser.IDENT, 0)

        def wymiar_tablicy(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wymiar_tablicyContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = SigmaScriptParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372088862) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 108
                self.wymiar_tablicy()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wymiar_tablicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_KWADRAT(self):
            return self.getToken(SigmaScriptParser.L_KWADRAT, 0)

        def P_KWADRAT(self):
            return self.getToken(SigmaScriptParser.P_KWADRAT, 0)

        def LICZ_CALK(self):
            return self.getToken(SigmaScriptParser.LICZ_CALK, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_wymiar_tablicy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWymiar_tablicy" ):
                listener.enterWymiar_tablicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWymiar_tablicy" ):
                listener.exitWymiar_tablicy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWymiar_tablicy" ):
                return visitor.visitWymiar_tablicy(self)
            else:
                return visitor.visitChildren(self)




    def wymiar_tablicy(self):

        localctx = SigmaScriptParser.Wymiar_tablicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_wymiar_tablicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(SigmaScriptParser.L_KWADRAT)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 112
                self.match(SigmaScriptParser.LICZ_CALK)


            self.state = 115
            self.match(SigmaScriptParser.P_KWADRAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Blok_koduContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_KLAMRA(self):
            return self.getToken(SigmaScriptParser.L_KLAMRA, 0)

        def P_KLAMRA(self):
            return self.getToken(SigmaScriptParser.P_KLAMRA, 0)

        def instrukcja(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.InstrukcjaContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.InstrukcjaContext,i)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_blok_kodu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlok_kodu" ):
                listener.enterBlok_kodu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlok_kodu" ):
                listener.exitBlok_kodu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlok_kodu" ):
                return visitor.visitBlok_kodu(self)
            else:
                return visitor.visitChildren(self)




    def blok_kodu(self):

        localctx = SigmaScriptParser.Blok_koduContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_blok_kodu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(SigmaScriptParser.L_KLAMRA)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184373922078) != 0):
                self.state = 118
                self.instrukcja()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(SigmaScriptParser.P_KLAMRA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrukcjaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def polecenie_ruchu(self):
            return self.getTypedRuleContext(SigmaScriptParser.Polecenie_ruchuContext,0)


        def polecenie_obrotu(self):
            return self.getTypedRuleContext(SigmaScriptParser.Polecenie_obrotuContext,0)


        def polecenie_pisaka(self):
            return self.getTypedRuleContext(SigmaScriptParser.Polecenie_pisakaContext,0)


        def petla(self):
            return self.getTypedRuleContext(SigmaScriptParser.PetlaContext,0)


        def petla_warunkowa(self):
            return self.getTypedRuleContext(SigmaScriptParser.Petla_warunkowaContext,0)


        def instrukcja_warunkowa(self):
            return self.getTypedRuleContext(SigmaScriptParser.Instrukcja_warunkowaContext,0)


        def wypisanie(self):
            return self.getTypedRuleContext(SigmaScriptParser.WypisanieContext,0)


        def deklaracja_zmiennej(self):
            return self.getTypedRuleContext(SigmaScriptParser.Deklaracja_zmiennejContext,0)


        def przypisanie(self):
            return self.getTypedRuleContext(SigmaScriptParser.PrzypisanieContext,0)


        def instrukcja_zwrotu(self):
            return self.getTypedRuleContext(SigmaScriptParser.Instrukcja_zwrotuContext,0)


        def wywolanie_funkcji(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wywolanie_funkcjiContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_instrukcja

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrukcja" ):
                listener.enterInstrukcja(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrukcja" ):
                listener.exitInstrukcja(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrukcja" ):
                return visitor.visitInstrukcja(self)
            else:
                return visitor.visitChildren(self)




    def instrukcja(self):

        localctx = SigmaScriptParser.InstrukcjaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_instrukcja)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.polecenie_ruchu()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.polecenie_obrotu()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.polecenie_pisaka()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.petla()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 130
                self.petla_warunkowa()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 131
                self.instrukcja_warunkowa()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 132
                self.wypisanie()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 133
                self.deklaracja_zmiennej()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 134
                self.przypisanie()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 135
                self.instrukcja_zwrotu()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 136
                self.wywolanie_funkcji()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polecenie_ruchuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAPRZOD(self):
            return self.getToken(SigmaScriptParser.NAPRZOD, 0)

        def wyrazenie_arytmetyczne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_polecenie_ruchu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolecenie_ruchu" ):
                listener.enterPolecenie_ruchu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolecenie_ruchu" ):
                listener.exitPolecenie_ruchu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolecenie_ruchu" ):
                return visitor.visitPolecenie_ruchu(self)
            else:
                return visitor.visitChildren(self)




    def polecenie_ruchu(self):

        localctx = SigmaScriptParser.Polecenie_ruchuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_polecenie_ruchu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(SigmaScriptParser.NAPRZOD)
            self.state = 140
            self.wyrazenie_arytmetyczne(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polecenie_obrotuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBROC(self):
            return self.getToken(SigmaScriptParser.OBROC, 0)

        def wyrazenie_arytmetyczne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_polecenie_obrotu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolecenie_obrotu" ):
                listener.enterPolecenie_obrotu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolecenie_obrotu" ):
                listener.exitPolecenie_obrotu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolecenie_obrotu" ):
                return visitor.visitPolecenie_obrotu(self)
            else:
                return visitor.visitChildren(self)




    def polecenie_obrotu(self):

        localctx = SigmaScriptParser.Polecenie_obrotuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_polecenie_obrotu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(SigmaScriptParser.OBROC)
            self.state = 143
            self.wyrazenie_arytmetyczne(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Polecenie_pisakaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PODNIES(self):
            return self.getToken(SigmaScriptParser.PODNIES, 0)

        def OPUSC(self):
            return self.getToken(SigmaScriptParser.OPUSC, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_polecenie_pisaka

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolecenie_pisaka" ):
                listener.enterPolecenie_pisaka(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolecenie_pisaka" ):
                listener.exitPolecenie_pisaka(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolecenie_pisaka" ):
                return visitor.visitPolecenie_pisaka(self)
            else:
                return visitor.visitChildren(self)




    def polecenie_pisaka(self):

        localctx = SigmaScriptParser.Polecenie_pisakaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_polecenie_pisaka)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PetlaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POWTORZ(self):
            return self.getToken(SigmaScriptParser.POWTORZ, 0)

        def wyrazenie_arytmetyczne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,0)


        def blok_kodu(self):
            return self.getTypedRuleContext(SigmaScriptParser.Blok_koduContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_petla

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPetla" ):
                listener.enterPetla(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPetla" ):
                listener.exitPetla(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPetla" ):
                return visitor.visitPetla(self)
            else:
                return visitor.visitChildren(self)




    def petla(self):

        localctx = SigmaScriptParser.PetlaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_petla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(SigmaScriptParser.POWTORZ)
            self.state = 148
            self.wyrazenie_arytmetyczne(0)
            self.state = 149
            self.blok_kodu()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Petla_warunkowaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOPOKI(self):
            return self.getToken(SigmaScriptParser.DOPOKI, 0)

        def L_NAWIAS(self):
            return self.getToken(SigmaScriptParser.L_NAWIAS, 0)

        def wyrazenie_logiczne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_logiczneContext,0)


        def P_NAWIAS(self):
            return self.getToken(SigmaScriptParser.P_NAWIAS, 0)

        def blok_kodu(self):
            return self.getTypedRuleContext(SigmaScriptParser.Blok_koduContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_petla_warunkowa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPetla_warunkowa" ):
                listener.enterPetla_warunkowa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPetla_warunkowa" ):
                listener.exitPetla_warunkowa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPetla_warunkowa" ):
                return visitor.visitPetla_warunkowa(self)
            else:
                return visitor.visitChildren(self)




    def petla_warunkowa(self):

        localctx = SigmaScriptParser.Petla_warunkowaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_petla_warunkowa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(SigmaScriptParser.DOPOKI)
            self.state = 152
            self.match(SigmaScriptParser.L_NAWIAS)
            self.state = 153
            self.wyrazenie_logiczne(0)
            self.state = 154
            self.match(SigmaScriptParser.P_NAWIAS)
            self.state = 155
            self.blok_kodu()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrukcja_warunkowaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JEZELI(self):
            return self.getToken(SigmaScriptParser.JEZELI, 0)

        def L_NAWIAS(self):
            return self.getToken(SigmaScriptParser.L_NAWIAS, 0)

        def wyrazenie_logiczne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_logiczneContext,0)


        def P_NAWIAS(self):
            return self.getToken(SigmaScriptParser.P_NAWIAS, 0)

        def blok_kodu(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Blok_koduContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Blok_koduContext,i)


        def INACZEJ(self):
            return self.getToken(SigmaScriptParser.INACZEJ, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_instrukcja_warunkowa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrukcja_warunkowa" ):
                listener.enterInstrukcja_warunkowa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrukcja_warunkowa" ):
                listener.exitInstrukcja_warunkowa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrukcja_warunkowa" ):
                return visitor.visitInstrukcja_warunkowa(self)
            else:
                return visitor.visitChildren(self)




    def instrukcja_warunkowa(self):

        localctx = SigmaScriptParser.Instrukcja_warunkowaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_instrukcja_warunkowa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(SigmaScriptParser.JEZELI)
            self.state = 158
            self.match(SigmaScriptParser.L_NAWIAS)
            self.state = 159
            self.wyrazenie_logiczne(0)
            self.state = 160
            self.match(SigmaScriptParser.P_NAWIAS)
            self.state = 161
            self.blok_kodu()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 162
                self.match(SigmaScriptParser.INACZEJ)
                self.state = 163
                self.blok_kodu()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WypisanieContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WYPISZ(self):
            return self.getToken(SigmaScriptParser.WYPISZ, 0)

        def wyrazenie_ogolne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_ogolneContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_wypisanie

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWypisanie" ):
                listener.enterWypisanie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWypisanie" ):
                listener.exitWypisanie(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWypisanie" ):
                return visitor.visitWypisanie(self)
            else:
                return visitor.visitChildren(self)




    def wypisanie(self):

        localctx = SigmaScriptParser.WypisanieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_wypisanie)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(SigmaScriptParser.WYPISZ)
            self.state = 167
            self.wyrazenie_ogolne()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deklaracja_zmiennejContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(SigmaScriptParser.TypContext,0)


        def IDENT(self):
            return self.getToken(SigmaScriptParser.IDENT, 0)

        def PRZYPIS(self):
            return self.getToken(SigmaScriptParser.PRZYPIS, 0)

        def wyrazenie_ogolne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_ogolneContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_deklaracja_zmiennej

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeklaracja_zmiennej" ):
                listener.enterDeklaracja_zmiennej(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeklaracja_zmiennej" ):
                listener.exitDeklaracja_zmiennej(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeklaracja_zmiennej" ):
                return visitor.visitDeklaracja_zmiennej(self)
            else:
                return visitor.visitChildren(self)




    def deklaracja_zmiennej(self):

        localctx = SigmaScriptParser.Deklaracja_zmiennejContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_deklaracja_zmiennej)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.typ()
            self.state = 170
            self.match(SigmaScriptParser.IDENT)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 171
                self.match(SigmaScriptParser.PRZYPIS)
                self.state = 172
                self.wyrazenie_ogolne()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrzypisanieContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USTAW(self):
            return self.getToken(SigmaScriptParser.USTAW, 0)

        def odwolanie(self):
            return self.getTypedRuleContext(SigmaScriptParser.OdwolanieContext,0)


        def PRZYPIS(self):
            return self.getToken(SigmaScriptParser.PRZYPIS, 0)

        def wyrazenie_ogolne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_ogolneContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_przypisanie

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrzypisanie" ):
                listener.enterPrzypisanie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrzypisanie" ):
                listener.exitPrzypisanie(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrzypisanie" ):
                return visitor.visitPrzypisanie(self)
            else:
                return visitor.visitChildren(self)




    def przypisanie(self):

        localctx = SigmaScriptParser.PrzypisanieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_przypisanie)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(SigmaScriptParser.USTAW)
            self.state = 176
            self.odwolanie()
            self.state = 177
            self.match(SigmaScriptParser.PRZYPIS)
            self.state = 178
            self.wyrazenie_ogolne()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instrukcja_zwrotuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZWROC(self):
            return self.getToken(SigmaScriptParser.ZWROC, 0)

        def wyrazenie_ogolne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_ogolneContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_instrukcja_zwrotu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrukcja_zwrotu" ):
                listener.enterInstrukcja_zwrotu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrukcja_zwrotu" ):
                listener.exitInstrukcja_zwrotu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrukcja_zwrotu" ):
                return visitor.visitInstrukcja_zwrotu(self)
            else:
                return visitor.visitChildren(self)




    def instrukcja_zwrotu(self):

        localctx = SigmaScriptParser.Instrukcja_zwrotuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_instrukcja_zwrotu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(SigmaScriptParser.ZWROC)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 181
                self.wyrazenie_ogolne()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OdwolanieContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.IDENT)
            else:
                return self.getToken(SigmaScriptParser.IDENT, i)

        def L_KWADRAT(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.L_KWADRAT)
            else:
                return self.getToken(SigmaScriptParser.L_KWADRAT, i)

        def wyrazenie_arytmetyczne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Wyrazenie_arytmetyczneContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,i)


        def P_KWADRAT(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.P_KWADRAT)
            else:
                return self.getToken(SigmaScriptParser.P_KWADRAT, i)

        def KROPKA(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.KROPKA)
            else:
                return self.getToken(SigmaScriptParser.KROPKA, i)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_odwolanie

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOdwolanie" ):
                listener.enterOdwolanie(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOdwolanie" ):
                listener.exitOdwolanie(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOdwolanie" ):
                return visitor.visitOdwolanie(self)
            else:
                return visitor.visitChildren(self)




    def odwolanie(self):

        localctx = SigmaScriptParser.OdwolanieContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_odwolanie)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(SigmaScriptParser.IDENT)
            self.state = 193
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 191
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [39]:
                        self.state = 185
                        self.match(SigmaScriptParser.L_KWADRAT)
                        self.state = 186
                        self.wyrazenie_arytmetyczne(0)
                        self.state = 187
                        self.match(SigmaScriptParser.P_KWADRAT)
                        pass
                    elif token in [41]:
                        self.state = 189
                        self.match(SigmaScriptParser.KROPKA)
                        self.state = 190
                        self.match(SigmaScriptParser.IDENT)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 195
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wywolanie_funkcjiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(SigmaScriptParser.IDENT, 0)

        def L_NAWIAS(self):
            return self.getToken(SigmaScriptParser.L_NAWIAS, 0)

        def P_NAWIAS(self):
            return self.getToken(SigmaScriptParser.P_NAWIAS, 0)

        def argumenty(self):
            return self.getTypedRuleContext(SigmaScriptParser.ArgumentyContext,0)


        def L_KWADRAT(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.L_KWADRAT)
            else:
                return self.getToken(SigmaScriptParser.L_KWADRAT, i)

        def wyrazenie_arytmetyczne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Wyrazenie_arytmetyczneContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,i)


        def P_KWADRAT(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.P_KWADRAT)
            else:
                return self.getToken(SigmaScriptParser.P_KWADRAT, i)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_wywolanie_funkcji

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWywolanie_funkcji" ):
                listener.enterWywolanie_funkcji(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWywolanie_funkcji" ):
                listener.exitWywolanie_funkcji(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWywolanie_funkcji" ):
                return visitor.visitWywolanie_funkcji(self)
            else:
                return visitor.visitChildren(self)




    def wywolanie_funkcji(self):

        localctx = SigmaScriptParser.Wywolanie_funkcjiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_wywolanie_funkcji)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(SigmaScriptParser.IDENT)
            self.state = 197
            self.match(SigmaScriptParser.L_NAWIAS)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132525552829952) != 0):
                self.state = 198
                self.argumenty()


            self.state = 201
            self.match(SigmaScriptParser.P_NAWIAS)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 202
                    self.match(SigmaScriptParser.L_KWADRAT)
                    self.state = 203
                    self.wyrazenie_arytmetyczne(0)
                    self.state = 204
                    self.match(SigmaScriptParser.P_KWADRAT) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenie_ogolne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Wyrazenie_ogolneContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_ogolneContext,i)


        def PRZECINEK(self, i:int=None):
            if i is None:
                return self.getTokens(SigmaScriptParser.PRZECINEK)
            else:
                return self.getToken(SigmaScriptParser.PRZECINEK, i)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_argumenty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumenty" ):
                listener.enterArgumenty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumenty" ):
                listener.exitArgumenty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumenty" ):
                return visitor.visitArgumenty(self)
            else:
                return visitor.visitChildren(self)




    def argumenty(self):

        localctx = SigmaScriptParser.ArgumentyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_argumenty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.wyrazenie_ogolne()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 212
                self.match(SigmaScriptParser.PRZECINEK)
                self.state = 213
                self.wyrazenie_ogolne()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inicjalizacja_tablicyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_KWADRAT(self):
            return self.getToken(SigmaScriptParser.L_KWADRAT, 0)

        def P_KWADRAT(self):
            return self.getToken(SigmaScriptParser.P_KWADRAT, 0)

        def argumenty(self):
            return self.getTypedRuleContext(SigmaScriptParser.ArgumentyContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_inicjalizacja_tablicy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicjalizacja_tablicy" ):
                listener.enterInicjalizacja_tablicy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicjalizacja_tablicy" ):
                listener.exitInicjalizacja_tablicy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicjalizacja_tablicy" ):
                return visitor.visitInicjalizacja_tablicy(self)
            else:
                return visitor.visitChildren(self)




    def inicjalizacja_tablicy(self):

        localctx = SigmaScriptParser.Inicjalizacja_tablicyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_inicjalizacja_tablicy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(SigmaScriptParser.L_KWADRAT)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132525552829952) != 0):
                self.state = 220
                self.argumenty()


            self.state = 223
            self.match(SigmaScriptParser.P_KWADRAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wyrazenie_ogolneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wyrazenie_arytmetyczne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,0)


        def wyrazenie_logiczne(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_logiczneContext,0)


        def inicjalizacja_tablicy(self):
            return self.getTypedRuleContext(SigmaScriptParser.Inicjalizacja_tablicyContext,0)


        def getRuleIndex(self):
            return SigmaScriptParser.RULE_wyrazenie_ogolne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWyrazenie_ogolne" ):
                listener.enterWyrazenie_ogolne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWyrazenie_ogolne" ):
                listener.exitWyrazenie_ogolne(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazenie_ogolne" ):
                return visitor.visitWyrazenie_ogolne(self)
            else:
                return visitor.visitChildren(self)




    def wyrazenie_ogolne(self):

        localctx = SigmaScriptParser.Wyrazenie_ogolneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_wyrazenie_ogolne)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.wyrazenie_arytmetyczne(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.wyrazenie_logiczne(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.inicjalizacja_tablicy()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wyrazenie_logiczneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_NAWIAS(self):
            return self.getToken(SigmaScriptParser.L_NAWIAS, 0)

        def wyrazenie_logiczne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Wyrazenie_logiczneContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_logiczneContext,i)


        def P_NAWIAS(self):
            return self.getToken(SigmaScriptParser.P_NAWIAS, 0)

        def PRAWDA(self):
            return self.getToken(SigmaScriptParser.PRAWDA, 0)

        def FALSZ(self):
            return self.getToken(SigmaScriptParser.FALSZ, 0)

        def TEKST(self):
            return self.getToken(SigmaScriptParser.TEKST, 0)

        def wywolanie_funkcji(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wywolanie_funkcjiContext,0)


        def odwolanie(self):
            return self.getTypedRuleContext(SigmaScriptParser.OdwolanieContext,0)


        def wyrazenie_arytmetyczne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Wyrazenie_arytmetyczneContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,i)


        def operator_rel(self):
            return self.getTypedRuleContext(SigmaScriptParser.Operator_relContext,0)


        def NIE(self):
            return self.getToken(SigmaScriptParser.NIE, 0)

        def ROWNY(self):
            return self.getToken(SigmaScriptParser.ROWNY, 0)

        def ROZNY(self):
            return self.getToken(SigmaScriptParser.ROZNY, 0)

        def ORAZ(self):
            return self.getToken(SigmaScriptParser.ORAZ, 0)

        def LUB(self):
            return self.getToken(SigmaScriptParser.LUB, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_wyrazenie_logiczne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWyrazenie_logiczne" ):
                listener.enterWyrazenie_logiczne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWyrazenie_logiczne" ):
                listener.exitWyrazenie_logiczne(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazenie_logiczne" ):
                return visitor.visitWyrazenie_logiczne(self)
            else:
                return visitor.visitChildren(self)



    def wyrazenie_logiczne(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SigmaScriptParser.Wyrazenie_logiczneContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_wyrazenie_logiczne, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 231
                self.match(SigmaScriptParser.L_NAWIAS)
                self.state = 232
                self.wyrazenie_logiczne(0)
                self.state = 233
                self.match(SigmaScriptParser.P_NAWIAS)
                pass

            elif la_ == 2:
                self.state = 235
                self.match(SigmaScriptParser.PRAWDA)
                pass

            elif la_ == 3:
                self.state = 236
                self.match(SigmaScriptParser.FALSZ)
                pass

            elif la_ == 4:
                self.state = 237
                self.match(SigmaScriptParser.TEKST)
                pass

            elif la_ == 5:
                self.state = 238
                self.wywolanie_funkcji()
                pass

            elif la_ == 6:
                self.state = 239
                self.odwolanie()
                pass

            elif la_ == 7:
                self.state = 240
                self.wyrazenie_arytmetyczne(0)
                self.state = 241
                self.operator_rel()
                self.state = 242
                self.wyrazenie_arytmetyczne(0)
                pass

            elif la_ == 8:
                self.state = 244
                self.match(SigmaScriptParser.NIE)
                self.state = 245
                self.wyrazenie_logiczne(3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = SigmaScriptParser.Wyrazenie_logiczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenie_logiczne)
                        self.state = 248
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 249
                        _la = self._input.LA(1)
                        if not(_la==29 or _la==30):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 250
                        self.wyrazenie_logiczne(5)
                        pass

                    elif la_ == 2:
                        localctx = SigmaScriptParser.Wyrazenie_logiczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenie_logiczne)
                        self.state = 251
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 252
                        self.match(SigmaScriptParser.ORAZ)
                        self.state = 253
                        self.wyrazenie_logiczne(3)
                        pass

                    elif la_ == 3:
                        localctx = SigmaScriptParser.Wyrazenie_logiczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenie_logiczne)
                        self.state = 254
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 255
                        self.match(SigmaScriptParser.LUB)
                        self.state = 256
                        self.wyrazenie_logiczne(2)
                        pass

             
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Operator_relContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROWNY(self):
            return self.getToken(SigmaScriptParser.ROWNY, 0)

        def ROZNY(self):
            return self.getToken(SigmaScriptParser.ROZNY, 0)

        def MNIEJSZY(self):
            return self.getToken(SigmaScriptParser.MNIEJSZY, 0)

        def WIEKSZY(self):
            return self.getToken(SigmaScriptParser.WIEKSZY, 0)

        def MNIEJ_ROWN(self):
            return self.getToken(SigmaScriptParser.MNIEJ_ROWN, 0)

        def WIEC_ROWN(self):
            return self.getToken(SigmaScriptParser.WIEC_ROWN, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_operator_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator_rel" ):
                listener.enterOperator_rel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator_rel" ):
                listener.exitOperator_rel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator_rel" ):
                return visitor.visitOperator_rel(self)
            else:
                return visitor.visitChildren(self)




    def operator_rel(self):

        localctx = SigmaScriptParser.Operator_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_operator_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wyrazenie_arytmetyczneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_NAWIAS(self):
            return self.getToken(SigmaScriptParser.L_NAWIAS, 0)

        def wyrazenie_arytmetyczne(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SigmaScriptParser.Wyrazenie_arytmetyczneContext)
            else:
                return self.getTypedRuleContext(SigmaScriptParser.Wyrazenie_arytmetyczneContext,i)


        def P_NAWIAS(self):
            return self.getToken(SigmaScriptParser.P_NAWIAS, 0)

        def wywolanie_funkcji(self):
            return self.getTypedRuleContext(SigmaScriptParser.Wywolanie_funkcjiContext,0)


        def odwolanie(self):
            return self.getTypedRuleContext(SigmaScriptParser.OdwolanieContext,0)


        def LICZ_CALK(self):
            return self.getToken(SigmaScriptParser.LICZ_CALK, 0)

        def LICZ_RZECZ(self):
            return self.getToken(SigmaScriptParser.LICZ_RZECZ, 0)

        def MINUS(self):
            return self.getToken(SigmaScriptParser.MINUS, 0)

        def TEKST(self):
            return self.getToken(SigmaScriptParser.TEKST, 0)

        def RAZY(self):
            return self.getToken(SigmaScriptParser.RAZY, 0)

        def PRZEZ(self):
            return self.getToken(SigmaScriptParser.PRZEZ, 0)

        def PLUS(self):
            return self.getToken(SigmaScriptParser.PLUS, 0)

        def getRuleIndex(self):
            return SigmaScriptParser.RULE_wyrazenie_arytmetyczne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWyrazenie_arytmetyczne" ):
                listener.enterWyrazenie_arytmetyczne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWyrazenie_arytmetyczne" ):
                listener.exitWyrazenie_arytmetyczne(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWyrazenie_arytmetyczne" ):
                return visitor.visitWyrazenie_arytmetyczne(self)
            else:
                return visitor.visitChildren(self)



    def wyrazenie_arytmetyczne(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SigmaScriptParser.Wyrazenie_arytmetyczneContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_wyrazenie_arytmetyczne, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 265
                self.match(SigmaScriptParser.L_NAWIAS)
                self.state = 266
                self.wyrazenie_arytmetyczne(0)
                self.state = 267
                self.match(SigmaScriptParser.P_NAWIAS)
                pass

            elif la_ == 2:
                self.state = 269
                self.wywolanie_funkcji()
                pass

            elif la_ == 3:
                self.state = 270
                self.odwolanie()
                pass

            elif la_ == 4:
                self.state = 271
                self.match(SigmaScriptParser.LICZ_CALK)
                pass

            elif la_ == 5:
                self.state = 272
                self.match(SigmaScriptParser.LICZ_RZECZ)
                pass

            elif la_ == 6:
                self.state = 273
                self.match(SigmaScriptParser.MINUS)
                self.state = 274
                self.wyrazenie_arytmetyczne(4)
                pass

            elif la_ == 7:
                self.state = 275
                self.match(SigmaScriptParser.TEKST)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 284
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = SigmaScriptParser.Wyrazenie_arytmetyczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenie_arytmetyczne)
                        self.state = 278
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 279
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==27):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 280
                        self.wyrazenie_arytmetyczne(4)
                        pass

                    elif la_ == 2:
                        localctx = SigmaScriptParser.Wyrazenie_arytmetyczneContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_wyrazenie_arytmetyczne)
                        self.state = 281
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 282
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 283
                        self.wyrazenie_arytmetyczne(3)
                        pass

             
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.wyrazenie_logiczne_sempred
        self._predicates[28] = self.wyrazenie_arytmetyczne_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def wyrazenie_logiczne_sempred(self, localctx:Wyrazenie_logiczneContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def wyrazenie_arytmetyczne_sempred(self, localctx:Wyrazenie_arytmetyczneContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




