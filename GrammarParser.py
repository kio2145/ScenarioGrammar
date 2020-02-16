# Generated from F:\test\Grammar.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

 
from LanguagePart import LanguagePart 

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5)\n\5\3\6\3\6\3\6\3\7\3\7\3\7\7\7\61\n\7\f\7\16")
        buf.write("\7\64\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\bA\n\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2@\2\21\3\2\2\2")
        buf.write("\4\25\3\2\2\2\6\34\3\2\2\2\b(\3\2\2\2\n*\3\2\2\2\f-\3")
        buf.write("\2\2\2\16@\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2\2\22\23\3")
        buf.write("\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\26")
        buf.write("\7\6\2\2\26\27\b\3\1\2\27\30\7\3\2\2\30\31\5\6\4\2\31")
        buf.write("\32\7\4\2\2\32\33\b\3\1\2\33\5\3\2\2\2\34!\5\b\5\2\35")
        buf.write("\36\7\5\2\2\36 \5\b\5\2\37\35\3\2\2\2 #\3\2\2\2!\37\3")
        buf.write("\2\2\2!\"\3\2\2\2\"\7\3\2\2\2#!\3\2\2\2$%\b\5\1\2%)\5")
        buf.write("\n\6\2&\'\b\5\1\2\')\5\16\b\2($\3\2\2\2(&\3\2\2\2)\t\3")
        buf.write("\2\2\2*+\5\f\7\2+,\b\6\1\2,\13\3\2\2\2-\62\7\7\2\2./\7")
        buf.write("\5\2\2/\61\7\7\2\2\60.\3\2\2\2\61\64\3\2\2\2\62\60\3\2")
        buf.write("\2\2\62\63\3\2\2\2\63\r\3\2\2\2\64\62\3\2\2\2\65\66\7")
        buf.write("\b\2\2\66\67\b\b\1\2\678\5\f\7\289\b\b\1\29:\7\6\2\2:")
        buf.write(";\b\b\1\2;A\3\2\2\2<=\7\b\2\2=>\b\b\1\2>?\7\6\2\2?A\b")
        buf.write("\b\1\2@\65\3\2\2\2@<\3\2\2\2A\17\3\2\2\2\7\23!(\62@")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'};'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'inform the Mayor'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SCENARIO_NAME", "FACTOR", "SUBJECT", "ACTION", "SPACES" ]

    RULE_lis_of_scenario = 0
    RULE_scenario = 1
    RULE_list_of_events = 2
    RULE_events = 3
    RULE_effect_of_the_factor = 4
    RULE_list_of_faktor = 5
    RULE_subjects_action = 6

    ruleNames =  [ "lis_of_scenario", "scenario", "list_of_events", "events", 
                   "effect_of_the_factor", "list_of_faktor", "subjects_action" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SCENARIO_NAME=4
    FACTOR=5
    SUBJECT=6
    ACTION=7
    SPACES=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    RealQueri=""
    scenarioName=[]
    scenarioEvent=[]
    scenarioIndex=0
    ErrorCh=False
    ErrorMSG=""
    def GetTok(self):
    	PartLanguage = LanguagePart()
    	PartLanguage.ReadTok()
    	self.Faktors=PartLanguage.GetFaktors()
    	self.Subjekt=PartLanguage.GetSubject()
    	self.Action=PartLanguage.GetAction()
    def GetQueri(self):
    	print(self.scenarioName)
    	print(self.scenarioEvent)
    def ChToken(self,tok, tokName):
    	if tokName=="f":
    		for tmptok in tok.split(','):
    			if tmptok.split('=')[0] not in self.Faktors:
    				self.ErrorCh=True
    				self.ErrorMSG="Фактору "+tmptok.split('=')[0]+" не існує"
    	if tokName=="s" and tok.split(':')[0] not in self.Subjekt:
    		print(self.Subjekt)
    		print(tok)
    		self.ErrorCh=True
    		self.ErrorMSG="Об'экту  "+tok.split(':')[0]+" не існує"
    	if tokName=="a" and tok not in self.Action:
    		self.ErrorCh=True
    		self.ErrorMSG="Дії  "+tok+" не існує"
    	self.scenarioEvent[self.scenarioIndex].append(tok)


    class Lis_of_scenarioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scenario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ScenarioContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ScenarioContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_lis_of_scenario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLis_of_scenario" ):
                listener.enterLis_of_scenario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLis_of_scenario" ):
                listener.exitLis_of_scenario(self)




    def lis_of_scenario(self):

        localctx = GrammarParser.Lis_of_scenarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lis_of_scenario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.scenario()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GrammarParser.SCENARIO_NAME):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ScenarioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._SCENARIO_NAME = None # Token

        def SCENARIO_NAME(self):
            return self.getToken(GrammarParser.SCENARIO_NAME, 0)

        def list_of_events(self):
            return self.getTypedRuleContext(GrammarParser.List_of_eventsContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_scenario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScenario" ):
                listener.enterScenario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScenario" ):
                listener.exitScenario(self)




    def scenario(self):

        localctx = GrammarParser.ScenarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_scenario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            localctx._SCENARIO_NAME = self.match(GrammarParser.SCENARIO_NAME)
            self.scenarioName.append((None if localctx._SCENARIO_NAME is None else localctx._SCENARIO_NAME.text))
            self.state = 21
            self.match(GrammarParser.T__0)
            self.state = 22
            self.list_of_events()
            self.state = 23
            self.match(GrammarParser.T__1)
            self.scenarioIndex+=1
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_of_eventsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def events(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.EventsContext)
            else:
                return self.getTypedRuleContext(GrammarParser.EventsContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_list_of_events

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_of_events" ):
                listener.enterList_of_events(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_of_events" ):
                listener.exitList_of_events(self)




    def list_of_events(self):

        localctx = GrammarParser.List_of_eventsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_of_events)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.events()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__2:
                self.state = 27
                self.match(GrammarParser.T__2)
                self.state = 28
                self.events()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EventsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def effect_of_the_factor(self):
            return self.getTypedRuleContext(GrammarParser.Effect_of_the_factorContext,0)


        def subjects_action(self):
            return self.getTypedRuleContext(GrammarParser.Subjects_actionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_events

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvents" ):
                listener.enterEvents(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvents" ):
                listener.exitEvents(self)




    def events(self):

        localctx = GrammarParser.EventsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_events)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GrammarParser.FACTOR]:
                self.enterOuterAlt(localctx, 1)
                self.scenarioEvent.append([])
                self.state = 35
                self.effect_of_the_factor()
                pass
            elif token in [GrammarParser.SUBJECT]:
                self.enterOuterAlt(localctx, 2)
                self.scenarioEvent.append([])
                self.state = 37
                self.subjects_action()
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

    class Effect_of_the_factorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._list_of_faktor = None # List_of_faktorContext

        def list_of_faktor(self):
            return self.getTypedRuleContext(GrammarParser.List_of_faktorContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_effect_of_the_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEffect_of_the_factor" ):
                listener.enterEffect_of_the_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEffect_of_the_factor" ):
                listener.exitEffect_of_the_factor(self)




    def effect_of_the_factor(self):

        localctx = GrammarParser.Effect_of_the_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_effect_of_the_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            localctx._list_of_faktor = self.list_of_faktor()
            self.scenarioEvent[self.scenarioIndex].append((None if localctx._list_of_faktor is None else self._input.getText((localctx._list_of_faktor.start,localctx._list_of_faktor.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_of_faktorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FACTOR(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.FACTOR)
            else:
                return self.getToken(GrammarParser.FACTOR, i)

        def getRuleIndex(self):
            return GrammarParser.RULE_list_of_faktor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_of_faktor" ):
                listener.enterList_of_faktor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_of_faktor" ):
                listener.exitList_of_faktor(self)




    def list_of_faktor(self):

        localctx = GrammarParser.List_of_faktorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list_of_faktor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(GrammarParser.FACTOR)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self.match(GrammarParser.T__2)
                    self.state = 45
                    self.match(GrammarParser.FACTOR) 
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Subjects_actionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._SUBJECT = None # Token
            self._list_of_faktor = None # List_of_faktorContext
            self._SCENARIO_NAME = None # Token

        def SUBJECT(self):
            return self.getToken(GrammarParser.SUBJECT, 0)

        def list_of_faktor(self):
            return self.getTypedRuleContext(GrammarParser.List_of_faktorContext,0)


        def SCENARIO_NAME(self):
            return self.getToken(GrammarParser.SCENARIO_NAME, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_subjects_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubjects_action" ):
                listener.enterSubjects_action(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubjects_action" ):
                listener.exitSubjects_action(self)




    def subjects_action(self):

        localctx = GrammarParser.Subjects_actionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subjects_action)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                localctx._SUBJECT = self.match(GrammarParser.SUBJECT)
                self.ChToken((None if localctx._SUBJECT is None else localctx._SUBJECT.text),'s')
                self.state = 53
                localctx._list_of_faktor = self.list_of_faktor()
                self.ChToken((None if localctx._list_of_faktor is None else self._input.getText((localctx._list_of_faktor.start,localctx._list_of_faktor.stop))),'f')
                self.state = 55
                localctx._SCENARIO_NAME = self.match(GrammarParser.SCENARIO_NAME)
                self.ChToken((None if localctx._SCENARIO_NAME is None else localctx._SCENARIO_NAME.text), 'a')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                localctx._SUBJECT = self.match(GrammarParser.SUBJECT)
                self.scenarioEvent[self.scenarioIndex].append((None if localctx._SUBJECT is None else localctx._SUBJECT.text))
                self.state = 60
                localctx._SCENARIO_NAME = self.match(GrammarParser.SCENARIO_NAME)
                self.scenarioEvent[self.scenarioIndex].append((None if localctx._SCENARIO_NAME is None else localctx._SCENARIO_NAME.text))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





