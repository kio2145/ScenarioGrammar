#-*- coding: utf-8 -*-
import pickle
import json
import re
class LanguagePart():
    def __init__(self):
        self.Faktors=[]
        self.Subjekt=[]
        self.Action=[]
        self.LevelGoals=[]
        self.GoalsIndex=0
    def GetFaktors(self):
        return self.Faktors
    def GetSubject(self):
        return self.Subjekt
    def GetAction(self):
        return self.Action
    def GetGoalsLel(self):
        return self.LevelGoals
    def LevelGoalsInsert(self,str_Levels):
        #json_acceptable_string = s.replace("'", "\"")
        print(str_Levels)
        d = json.loads(str_Levels)
        self.LevelGoals.append(d)
    def ReadTok(self):
        f = open('Options.txt', 'r',  encoding="utf-8")
        for line in f:
            line=line.replace("\n","")
            if "Faktors=" in line:
                line=line.replace("Faktors=","")
                self.Faktors=line.split(";")
                continue
            if "Subjekt=" in line:
                line=line.replace("Subjekt=","")
                self.Subjekt=line.split(";")
                continue
            if "Action=" in line:
                line=line.replace("Action=","")
                self.Action=line.split(";")
                continue
            if re.match(r'Goals lvl \d+ :', line)!=None:
                line=re.sub(r'Goals lvl \d+ :', '', line)
                self.LevelGoalsInsert(line)
    def WriteSaveGrammar(self):
        with open('Language.pickle', 'wb') as f:
             pickle.dump(self, f)
    def OpenFileGrammar(self):
        with open('Language.pickle', 'rb') as f:
            self = pickle.load(f)
class LoadGrammar:
    def OpenFileGrammar(self):
        with open('Language.pickle', 'rb') as f:
            rez = pickle.load(f)
        return rez
if __name__ == '__main__':
    #Grammar=LoadGrammar()
    #LP=Grammar.OpenFileGrammar()
    LP=LanguagePart()
    LP.ReadTok()
    print(LP.GetGoalsLel())
    #LP.WriteSaveGrammar()
    #LP.OpenFileGrammar()
    #print(LP.GetFaktors())
#    print(LP.GetFaktors())
    #with open('Language.pickle', 'wb') as f:
        #pickle.dump(LP, f)
    #with open('Language.pickle', 'rb') as f:
        #entry = pickle.load(f) 
    #print(entry.GetFaktors())
