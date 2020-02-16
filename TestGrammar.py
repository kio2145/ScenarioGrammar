# encoding: utf-8
import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from functools import singledispatch
from LanguagePart import LoadGrammar,LanguagePart
import time
def main(argv):
    Grammar=LoadGrammar()
    LP=Grammar.OpenFileGrammar()
    print(LP.GetFaktors())
    #input = FileStream("input.txt")
    while True:
        inputs= InputStream(input('Comand: '))
        if str(inputs)=="exit":
            print("Goodbye")
            break
        lexer = GrammarLexer(inputs)
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        parser.GetTok()
        tree = parser.lis_of_scenario()
        print("Output: ")
        #tree = parser.parseoperator()
        if parser.getNumberOfSyntaxErrors()==0 and parser.ErrorCh!=True:
            parser.GetQueri()
        elif parser.ErrorCh==True:
            print(parser.ErrorMSG)
if __name__ == '__main__':
    main(sys.argv)
