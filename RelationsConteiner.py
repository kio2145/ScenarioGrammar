class RelationsConteiner:
    def __init__(self,name,relations):
        self.ValueName=name
        self.ValueRelations=relations
    def GetValueName(self):
        return self.ValueName
    def GetValueRelations(self):
        return self.ValueRelations
    def SetValueName(self,name):
        self.ValueName=name
    def SetValueRelations(self):
        self.ValueRelations=relations