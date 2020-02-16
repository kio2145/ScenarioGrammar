# Generated from F:\ScenarioGrammar\ScenarioGrammar\Grammar.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser
 
from LanguagePart import LoadGrammar,LanguagePart
import re


# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#lis_of_scenario.
    def enterLis_of_scenario(self, ctx:GrammarParser.Lis_of_scenarioContext):
        pass

    # Exit a parse tree produced by GrammarParser#lis_of_scenario.
    def exitLis_of_scenario(self, ctx:GrammarParser.Lis_of_scenarioContext):
        pass


    # Enter a parse tree produced by GrammarParser#scenario.
    def enterScenario(self, ctx:GrammarParser.ScenarioContext):
        pass

    # Exit a parse tree produced by GrammarParser#scenario.
    def exitScenario(self, ctx:GrammarParser.ScenarioContext):
        pass


    # Enter a parse tree produced by GrammarParser#list_of_events.
    def enterList_of_events(self, ctx:GrammarParser.List_of_eventsContext):
        pass

    # Exit a parse tree produced by GrammarParser#list_of_events.
    def exitList_of_events(self, ctx:GrammarParser.List_of_eventsContext):
        pass


    # Enter a parse tree produced by GrammarParser#events.
    def enterEvents(self, ctx:GrammarParser.EventsContext):
        pass

    # Exit a parse tree produced by GrammarParser#events.
    def exitEvents(self, ctx:GrammarParser.EventsContext):
        pass


    # Enter a parse tree produced by GrammarParser#effect_of_the_factor.
    def enterEffect_of_the_factor(self, ctx:GrammarParser.Effect_of_the_factorContext):
        pass

    # Exit a parse tree produced by GrammarParser#effect_of_the_factor.
    def exitEffect_of_the_factor(self, ctx:GrammarParser.Effect_of_the_factorContext):
        pass


    # Enter a parse tree produced by GrammarParser#list_of_faktor.
    def enterList_of_faktor(self, ctx:GrammarParser.List_of_faktorContext):
        pass

    # Exit a parse tree produced by GrammarParser#list_of_faktor.
    def exitList_of_faktor(self, ctx:GrammarParser.List_of_faktorContext):
        pass


    # Enter a parse tree produced by GrammarParser#subjects_action.
    def enterSubjects_action(self, ctx:GrammarParser.Subjects_actionContext):
        pass

    # Exit a parse tree produced by GrammarParser#subjects_action.
    def exitSubjects_action(self, ctx:GrammarParser.Subjects_actionContext):
        pass


