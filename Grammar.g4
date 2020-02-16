grammar Grammar;
@header { 
from LanguagePart import LanguagePart 
}
@members {
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
}
lis_of_scenario:
	 scenario+;
scenario:
	SCENARIO_NAME {self.scenarioName.append($SCENARIO_NAME.text)} '{' list_of_events '};'{self.scenarioIndex+=1};
list_of_events:
	events(',' events)*;
events:
	{self.scenarioEvent.append([])}effect_of_the_factor|
	{self.scenarioEvent.append([])}subjects_action;
effect_of_the_factor:
	list_of_faktor {self.scenarioEvent[self.scenarioIndex].append($list_of_faktor.text)};
list_of_faktor:
	FACTOR (',' FACTOR)*;
subjects_action:
	SUBJECT{self.ChToken($SUBJECT.text,'s')} list_of_faktor{self.ChToken($list_of_faktor.text,'f')} SCENARIO_NAME{self.ChToken($SCENARIO_NAME.text, 'a')}|
	SUBJECT{self.scenarioEvent[self.scenarioIndex].append($SUBJECT.text)} SCENARIO_NAME{self.scenarioEvent[self.scenarioIndex].append($SCENARIO_NAME.text)};
SCENARIO_NAME:
	[\u0400-\u04FF]+([\u0020\u0400-\u04FF])*;
FACTOR:
	[\u0400-\u04FF]+([\u0020\u0400-\u04FF])* ' = '[0-9]+;
SUBJECT:
	[\u0400-\u04FF]+([\u0400-\u04FF])*':';
ACTION:
	'inform the Mayor';
SPACES
 : 
 [ \t\r\n] -> channel(HIDDEN);
