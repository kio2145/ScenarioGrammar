#-*- coding: utf-8 -*-
import pickle
class LanguagePart():
    def __init__(self):
        self.Faktors=[]
        self.Subjekt=[]
        self.Action=[]
    def GetFaktors(self):
        return self.Faktors
    def GetSubject(self):
        return self.Subjekt
    def GetAction(self):
        return self.Action
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
#if __name__ == '__main__':
#    LP=LanguagePart()
#    LP.ReadTok()
#    print(LP.GetFaktors())
    #with open('Language.pickle', 'wb') as f:
        #pickle.dump(LP, f)
    #with open('Language.pickle', 'rb') as f:
        #entry = pickle.load(f) 
    #print(entry.GetFaktors())
