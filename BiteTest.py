from LanguagePart import LanguagePart 
import pickle
PartLanguage=LanguagePart()
with open('Language.pickle', 'rb') as f:
		PartLanguage = pickle.load(f)
print(PartLanguage.GetFaktors())
