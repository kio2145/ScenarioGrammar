# Generated from F:\ScenarioGrammar\ScenarioGrammar\Grammar.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

 
from LanguagePart import LoadGrammar,LanguagePart
import re


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("[\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\6\5\34")
        buf.write("\n\5\r\5\16\5\35\3\5\7\5!\n\5\f\5\16\5$\13\5\3\6\6\6\'")
        buf.write("\n\6\r\6\16\6(\3\6\7\6,\n\6\f\6\16\6/\13\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\6\6\66\n\6\r\6\16\6\67\3\7\6\7;\n\7\r\7\16\7")
        buf.write("<\3\7\7\7@\n\7\f\7\16\7C\13\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\3\2\6\3\2\u0402\u0501\4\2\"\"\u0402\u0501\3\2\62;\5")
        buf.write("\2\13\f\17\17\"\"\2a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\3\23\3\2\2\2\5\25\3\2\2\2\7\30\3\2\2\2\t\33")
        buf.write("\3\2\2\2\13&\3\2\2\2\r:\3\2\2\2\17F\3\2\2\2\21W\3\2\2")
        buf.write("\2\23\24\7}\2\2\24\4\3\2\2\2\25\26\7\177\2\2\26\27\7=")
        buf.write("\2\2\27\6\3\2\2\2\30\31\7.\2\2\31\b\3\2\2\2\32\34\t\2")
        buf.write("\2\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3")
        buf.write("\2\2\2\36\"\3\2\2\2\37!\t\3\2\2 \37\3\2\2\2!$\3\2\2\2")
        buf.write("\" \3\2\2\2\"#\3\2\2\2#\n\3\2\2\2$\"\3\2\2\2%\'\t\2\2")
        buf.write("\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)-\3\2\2\2")
        buf.write("*,\t\3\2\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60")
        buf.write("\3\2\2\2/-\3\2\2\2\60\61\7\"\2\2\61\62\7?\2\2\62\63\7")
        buf.write("\"\2\2\63\65\3\2\2\2\64\66\t\4\2\2\65\64\3\2\2\2\66\67")
        buf.write("\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\f\3\2\2\29;\t\2\2")
        buf.write("\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=A\3\2\2\2>")
        buf.write("@\t\2\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2BD\3")
        buf.write("\2\2\2CA\3\2\2\2DE\7<\2\2E\16\3\2\2\2FG\7k\2\2GH\7p\2")
        buf.write("\2HI\7h\2\2IJ\7q\2\2JK\7t\2\2KL\7o\2\2LM\7\"\2\2MN\7v")
        buf.write("\2\2NO\7j\2\2OP\7g\2\2PQ\7\"\2\2QR\7O\2\2RS\7c\2\2ST\7")
        buf.write("{\2\2TU\7q\2\2UV\7t\2\2V\20\3\2\2\2WX\t\5\2\2XY\3\2\2")
        buf.write("\2YZ\b\t\2\2Z\22\3\2\2\2\n\2\35\"(-\67<A\3\2\3\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    SCENARIO_NAME = 4
    FACTOR = 5
    SUBJECT = 6
    ACTION = 7
    SPACES = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'};'", "','", "'inform the Mayor'" ]

    symbolicNames = [ "<INVALID>",
            "SCENARIO_NAME", "FACTOR", "SUBJECT", "ACTION", "SPACES" ]

    ruleNames = [ "T__0", "T__1", "T__2", "SCENARIO_NAME", "FACTOR", "SUBJECT", 
                  "ACTION", "SPACES" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    RealQueri=""
    scenarioName=[]
    scenarioEvent=[]
    scenarioIndex=0
    ErrorCh=False
    ErrorMSG=""
    def GetTok(self):
    	Grammar=LoadGrammar()
    	PartLanguage=Grammar.OpenFileGrammar()
    	#PartLanguage.ReadTok()
    	self.Faktors=PartLanguage.GetFaktors()
    	self.Subjekt=PartLanguage.GetSubject()
    	self.Action=PartLanguage.GetAction()
    def GetQueri(self):
    	print(self.scenarioName)
    	print(self.scenarioEvent)
    def RmSpace(self,s):
    	s = re.sub(" +", " ", s)
    	return s.strip()
    def ChToken(self,tok, tokName):
    	if tokName=="f":
    		for tmptok in tok.split(','):
    			if self.RmSpace(tmptok.split('=')[0]) not in self.Faktors:
    				self.ErrorCh=True
    				self.ErrorMSG="Фактору "+self.RmSpace(tmptok.split('=')[0])+" не існує"
    	if tokName=="s" and self.RmSpace(tok.split(':')[0]) not in self.Subjekt:
    		print(self.Subjekt)
    		print(tok)
    		self.ErrorCh=True
    		self.ErrorMSG="Об'экту  "+tok.split(':')[0]+" не існує"
    	if tokName=="a" and self.RmSpace(tok.strip()) not in self.Action:
    		self.ErrorCh=True
    		self.ErrorMSG="Дії  "+tok+" не існує"
    	self.scenarioEvent[self.scenarioIndex].append(self.RmSpace(tok.split(':')[0]))


