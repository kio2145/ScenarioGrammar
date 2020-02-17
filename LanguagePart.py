#-*- coding: utf-8 -*-
import pickle
import json
import re
from RelationsConteiner import RelationsConteiner
class LanguagePart():
    def __init__(self):
        self.Faktors=[]
        self.Subjekt=[]
        self.Action=[]
        self.LevelGoals=[]
        #self.GoalsIndex=0
        self.RelationConteinr=[]
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
        d = json.loads(str_Levels)
        return d
        #self.LevelGoals.append(d)
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
            if re.match(r'Goals lvl \d+=', line)!=None:
                line=re.sub(r'Goals lvl \d+=', '', line)
                self.LevelGoals.append(line.split(";"))
                #self.LevelGoalsInsert(line)
                continue
            for LevelGoals in self.LevelGoals:
                for Goals in LevelGoals:
                    if Goals+"=" in line:
                        #print(Goals)
                        line=line.replace(Goals+"=","")
                        Rel=self.LevelGoalsInsert(line)
                        self.RelationConteinr.append(RelationsConteiner(Goals,Rel))
    def WriteSaveGrammar(self):
        with open('Language.pickle', 'wb') as f:
             pickle.dump(self, f)
    def OpenFileGrammar(self):
        with open('Language.pickle', 'rb') as f:
            self = pickle.load(f)
    def GetGoalsConteiner(self,name):
        for tmpGoals in self.RelationConteinr:
            if tmpGoals.GetValueName()==name:
                #print(tmpGoals.GetValueRelations())
                return tmpGoals.GetValueRelations()
        return None
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
    print(LP.GetGoalsConteiner("время ремонта"))
    #print(LP.GetGoalsLel())
    #LP.WriteSaveGrammar()
    #LP.OpenFileGrammar()
    #print(LP.GetFaktors())
#    print(LP.GetFaktors())
    #with open('Language.pickle', 'wb') as f:
        #pickle.dump(LP, f)
    #with open('Language.pickle', 'rb') as f:
        #entry = pickle.load(f) 
    #print(entry.GetFaktors())
