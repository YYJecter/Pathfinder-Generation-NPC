#Die

def Die(n):
  import random
  return(random.randint(1,n))

#Stat Roll

def StatRoll():
  return (Die(4)+Die(4)+Die(4)+Die(4)+Die(4))

#Stats

Strength=StatRoll()
Dexterity=StatRoll()
Constitution=StatRoll()
Intelligence=StatRoll()
Wisdom=StatRoll()
Charisma=StatRoll()



#Stat Mods

def StatMod(n):
  return((n-10)//2)

StrMod=StatMod(Strength)
DexMod=StatMod(Dexterity)
ConMod=StatMod(Constitution)
IntMod=StatMod(Intelligence)
WisMod=StatMod(Wisdom)
ChaMod=StatMod(Charisma)

def PrintStatsandMods():
  print('Str: ',Strength,'StrMod: ',StrMod)
  print('Dex: ',Dexterity,'DexMod: ',DexMod)
  print('Con: ',Constitution,'ConMod: ',ConMod)
  print('Int: ',Intelligence,'IntMod: ',IntMod)
  print('Wis: ',Wisdom,'WisMod: ',WisMod)
  print('Cha: ',Charisma,'ChaMod: ',ChaMod)


#make sure not to use the print command to print(PrintStatsandMods())


#
#AC stuff, with temp values, find out how to put in default values

def ACBase():
  return 10

#Temp Armor and shield ac and penalty

ArmorAC=0
ShieldAC=0
ArmorDexPen=0
ShieldDexPen=0


def DexACBonus():
  if DexMod-(ArmorDexPen+ShieldDexPen)<=0:
    return 0
  elif  DexMod-(ArmorDexPen+ShieldDexPen)>=0:
    return DexMod-(ArmorDexPen+ShieldDexPen)

def ACTotal():
  return (ACBase()+DexACBonus()+ArmorAC+ShieldAC)

###
#skill points, by level and total

def ClassBonus(n):
  return n

def SkillPointPerLevel(ClassBonus):
  return ClassBonus+IntMod

def TotalSkillPoints(Level):
  return SkillPointPerLevel*Level

#
#Base attack bonus goes by one of three routes, here they are

def HighBAB(Level):
  return int(Level)
def MediumBAB(Level):
  return int(((.75*Level)//1))
def LowBAB(Level):
  return int(((.5*Level)//1))

def MeleeAttackBonus(Level):
  if HighBAB==True:
    return HighBAB+StrMod
  elif MediumBAB==True:
    return MediumBAB+StrMod
  elif LowBAB==True:
    return LowBAB+StrMod





#
#Base saves have two types, good and bad

#this format was recommended by zach but didn't work, read up on it
'''
def base_save(is_good):
  if is_good:
    return 2+(Level//2)
  return 0+(Level//3)
'''

def GoodSave():
  return 2+(Level//2)
  
def PoorSave():
  return 0+(Level//3)

#
#Skill list and stat mods to skills

SkillList={'Acrobatics':0,'Appraise':0,'Bluff':0,
'Climb':0,'Craft':0,'Diplomacy':0,
'DisableDevice':0,'Disguise':0,
'EscapeArtist':0,'Fly':0,'HandleAnimal':0,
'Heal':0,'Intimidate':0,'KnowledgeArcana':0,
'KnowledgeDungeoneering':0,'KnowledgeEngineering':0,
'KnowledgeGeograpy':0,'KnowledgeHistory':0,
'KnowledgeLocal':0,'KnowledgeNature':0,
'KnowledgeNobility':0,'KnowledgePlanes':0,
'KnowledgeReligion':0,'Linguistics':0,'Perception':0,
'Perform':0,'Profession':0,'Ride':0,
'SenseMotive':0,'SleightofHand':0,'Spellcraft':0,
'Stealth':0,'Survival':0,'Swim':0,
'Use Magic Device':0}


SkillMods={'Acrobatics':DexMod,'Appraise':IntMod,'Bluff':ChaMod,
'Climb':StrMod,'Craft':IntMod,'Diplomacy':ChaMod,
'DisableDevice':DexMod,'Disguise':ChaMod,
'EscapeArtist':DexMod,'Fly':DexMod,'HandleAnimal':ChaMod,
'Heal':WisMod,'Intimidate':ChaMod,'KnowledgeArcana':IntMod,
'KnowledgeDungeoneering':IntMod,'KnowledgeEngineering':IntMod,
'KnowledgeGeograpy':IntMod,'KnowledgeHistory':IntMod,
'KnowledgeLocal':IntMod,'KnowledgeNature':IntMod,
'KnowledgeNobility':IntMod,'KnowledgePlanes':IntMod,
'KnowledgeReligion':IntMod,'Linguistics':IntMod,'Perception':WisMod,
'Perform':ChaMod,'Profession':WisMod,'Ride':DexMod,
'SenseMotive':WisMod,'SleightofHand':DexMod,'Spellcraft':IntMod,
'Stealth':DexMod,'Survival':WisMod,'Swim':StrMod,
'Use Magic Device':ChaMod}


#for next section, 0 means can be used untrained, 1 means must be trained
#think of it as, the number of invested points needed to use the skill
skill_training_necessary={'Acrobatics':0,'Appraise':0,'Bluff':0,
'Climb':0,'Craft':0,'Diplomacy':0,
'DisableDevice':1,'Disguise':0,
'EscapeArtist':0,'Fly':0,'HandleAnimal':1,
'Heal':0,'Intimidate':0,'KnowledgeArcana':1,
'KnowledgeDungeoneering':1,'KnowledgeEngineering':1,
'KnowledgeGeograpy':1,'KnowledgeHistory':1,
'KnowledgeLocal':1,'KnowledgeNature':1,
'KnowledgeNobility':1,'KnowledgePlanes':1,
'KnowledgeReligion':1,'Linguistics':1,'Perception':0,
'Perform':0,'Profession':1,'Ride':0,
'SenseMotive':0,'SleightofHand':1,'Spellcraft':1,
'Stealth':0,'Survival':0,'Swim':0,
'Use Magic Device':1}


#here again 0 means no, and 1 means yes.
skills_armor_check_penalty_relevent={'Acrobatics':1,'Appraise':0,'Bluff':0,
'Climb':1,'Craft':0,'Diplomacy':0,
'DisableDevice':1,'Disguise':0,
'EscapeArtist':1,'Fly':1,'HandleAnimal':0,
'Heal':0,'Intimidate':0,'KnowledgeArcana':0,
'KnowledgeDungeoneering':0,'KnowledgeEngineering':0,
'KnowledgeGeograpy':0,'KnowledgeHistory':0,
'KnowledgeLocal':0,'KnowledgeNature':0,
'KnowledgeNobility':0,'KnowledgePlanes':0,
'KnowledgeReligion':0,'Linguistics':0,'Perception':0,
'Perform':0,'Profession':0,'Ride':1,
'SenseMotive':0,'SleightofHand':1,'Spellcraft':0,
'Stealth':1,'Survival':0,'Swim':1,
'Use Magic Device':0}



#
#HP

def HPPerLevel(n):
  return ConMod+Die(n)

def HPTotal(Level):
  HPPerLevel()*Level


#make the below better, and a function
'''
Level=1
hproll=0
HP=int()
while hproll<Level:
  HP=HP+((HPPerLevel(8))+ConMod)
  hproll=hproll+1
  print('hproll',hproll)
  print('HP',HP)
  print()
'''
#this sucks make it work
'''
def totalHP(HPPerLevel,Level):
  count=0
  hproll=0
  HP=0
  while hproll<Level:
    HP=HP+HPPerLevel
    count=count+1
    print(HP)

totalHP(8,1)
'''



#
#ClassSkill






#
#Class Format

'''
Classname=[
  HPPerLevel(die rolled for hp),
  Fortitude Save,
  Reflex Save,
  Will Save,
  BAB,
  Skill points per level,
  ClassSkill_
  ]
'''



#
#Test Class



#here are the actual classes that i'm dealing with for now
NPCClass=str()
Barbarian=str('Barbarian')
Bard=str('Bard')
Cleric=str('Cleric')
Druid=str('Druid')
Fighter=str('Fighter')
Monk=str('Monk')
Paladin=str('Paladin')
Ranger=str('Ranger')
Rogue=str('Rogue')
Sorcerer=str('Sorcerer')
Wizard=str('Wizard')


def PrintStatsandMods():
  print('Str: ',Strength,'StrMod: ',StrMod)
  print('Dex: ',Dexterity,'DexMod: ',DexMod)
  print('Con: ',Constitution,'ConMod: ',ConMod)
  print('Int: ',Intelligence,'IntMod: ',IntMod)
  print('Wis: ',Wisdom,'WisMod: ',WisMod)
  print('Cha: ',Charisma,'ChaMod: ',ChaMod)


#
#Base attack bonus goes by one of three routes, here they are
#conditional argument could be used here(didn't work when i tried, to make it take level 1 as a conditional unless otherwise stated)

def BAB(HighMediumLowBAB, Level):
  if HighMediumLowBAB=='High':
    return int(Level)
  elif HighMediumLowBAB=='Medium':
    return int(((.75*Level)//1))
  elif HighMediumLowBAB=='Low':
    return int(((.5*Level)//1))
  else:
    return('BAB ERROR')



#
#maybe separate out MeleeRanged into a function?

def MeleeRanged(n):
  if n=='Melee':
    return StrMod
  elif n=='Ranged':
    return DexMod

#like so, and then integrate it into the situational attack bonus
#function below
#to allow cleaner code later


#this is currently terrible, but functional, it wont be functional
#outside of itself though, so make it better
#this has largely been replaced by the function "AttackString"
def SituationalAttackBonus(HighMediumLowBAB,Level,MeleeRanged):
  if HighMediumLowBAB=='High' and MeleeRanged=='Melee':
    return int(Level)+StrMod
  if HighMediumLowBAB=='High' and MeleeRanged=='Ranged':
    return int(Level)+DexMod    
  elif HighMediumLowBAB=='Medium' and MeleeRanged=='Melee':
    return int(((.75*Level)//1))+StrMod
  elif HighMediumLowBAB=='Medium' and MeleeRanged=='Ranged':
    return int(((.75*Level)//1))+DexMod    
  elif HighMediumLowBAB=='Low' and MeleeRanged=='Melee':
    return int(((.5*Level)//1))+StrMod
  elif HighMediumLowBAB=='Low' and MeleeRanged=='Ranged':
    return int(((.5*Level)//1))+DexMod



#this is currently terrible, but functional, it wont be functional
#outside of itself though, so make it better
#make MeleeRanged a separate function, and have it as a function here
#maybe make a while loop to automate the number of -5s so it has no upper
#limit. like the below
#While BAB >5 BAB0=BAB, BAB1=BAB, etc
#use a while loop and make the meleeranged thing a function again

def AttackString(BAB,MeleeRanged):
  if BAB<=5 and MeleeRanged=='Melee':
    return BAB+StrMod
  elif BAB<=5 and MeleeRanged=='Ranged':
    return BAB+DexMod
  elif 5<BAB<=10 and MeleeRanged=='Melee':
    return BAB+StrMod,BAB-5+StrMod
  elif 5<BAB<=10 and MeleeRanged=='Ranged':
    return BAB+DexMod,BAB-5+DexMod
  elif 10<BAB<=15 and MeleeRanged=='Melee':
    return BAB+StrMod,BAB-5+StrMod,BAB-10+StrMod
  elif 10<BAB<=15 and MeleeRanged=='Ranged':
    return BAB+DexMod,BAB-5+DexMod,BAB-10+DexMod
  elif 15<BAB<=20 and MeleeRanged=='Melee':
    return BAB+StrMod,BAB-5+StrMod,BAB-10+StrMod,BAB-15+StrMod
  elif 15<BAB<=20 and MeleeRanged=='Ranged':
    return BAB+DexMod,BAB-5+DexMod,BAB-10+DexMod,BAB-15+DexMod
  elif 20<BAB and MeleeRanged=='Melee':
    return BAB+StrMod,BAB-5+StrMod,BAB-10+StrMod,BAB-15+StrMod
  elif 20<BAB and MeleeRanged=='Ranged':
    return BAB+DexMod,BAB-5+DexMod,BAB-10+DexMod,BAB-15+DexMod
  else:
    return '?'

Level=1

#can't save functions in json files, so the hp,saves, and bab need to be different.  idea, use the function as a string, and have the 
#string inform the function
#hp should be a number, like the skill points level

Barbarian={'HP':12,'SkillPointsLevel':4,'Fortsave':'Good','ReflexSave':'Poor','WillSave':'Poor','BAB':'High',
'ClassSkills':['Acrobatics','Climb','Craft','DisableDevice','HandleAnimal','Intimidate','KnowledgeNature','Perception','Ride','Survival']}

Bard={'HP':8,'SkillPointsLevel':6,'Fortsave':'Poor','ReflexSave':'Good','WillSave':'Good','BAB':'Medium',
'ClassSkills':['Acrobatics','Appraise','Bluff','Climb','Craft','Diplomacy','Disguise','EscapeArtist','Intimidate','KnowledgeArcana',
'KnowledgeDungeoneering','KnowledgeEngingeering','KnowledgeGeography','KnowledgeHistory','KnowledgeLocal','KnowledgeNature',
'KnowledgeNobility','KnowledgePlanes','KnowledgeReligion','Linguistics','Perception','Perform','Profession','SenseMotive','SleightofHand',
'Spellcraft','Stealth','UseMagicDevice']}

Cleric={'HP':8,'SkillPointsLevel':2,'Fortsave':'Good','ReflexSave':'Poor','WillSave':'Good','BAB':'Medium',
'ClassSkills':['Appraise','Craft','Diplomacy','Heal','KnowledgeArcana','KnowledgeHistory','KnowledgeNobility','KnowledgePlanes',
'KnowledgeReligion','Linguistics','Profession','SenseMotive','Spellcraft']}

Druid={'HP':8,'SkillPointsLevel':4,'Fortsave':'Good','ReflexSave':'Poor','WillSave':'Good','BAB':'Medium',
'ClassSkills':['Climb','Craft','Fly','HandleAnimal','Heal','KnowledgeGeography','KnowledgeNature','Perception','Profession',
'SenseMotive','Spellcraft','Survival','Swim']}

Fighter={'HP':10,'SkillPointsLevel':2,'Fortsave':'Good','ReflexSave':'Poor','WillSave':'Poor','BAB':'High',
'ClassSkills':['Climb','Craft','HandleAnimal','Intimidate','KnowledgeDungeoneering','KnowledgeEngingeering','Profession',
'Ride','Survival','Swim']}

Monk={'HP':8,'SkillPointsLevel':4,'Fortsave':'Good','ReflexSave':'Good','WillSave':'Good','BAB':'Medium',
'ClassSkills':['Acrobatics','Climb','Craft','EscapeArtist','Intimidate','KnowledgeHistory','KnowledgeReligion','Perception',
'Perform','Profession','Ride','SenseMotive','Stealth','Swim']}

Paladin={'HP':10,'SkillPointsLevel':2,'Fortsave':'Good','ReflexSave':'Poor','WillSave':'Good','BAB':'High',
'ClassSkills':['Craft','Diplomacy','HandleAnimal','Heal','KnowledgeNobility','KnowledgeReligion','Profession',
'Ride','SenseMotive','Spellcraft']}

Ranger={'HP':10,'SkillPointsLevel':6,'Fortsave':'Good','ReflexSave':'Good','WillSave':'Poor','BAB':'High',
'ClassSkills':['Climb','Craft','HandleAnimal','Heal','Intimidate','KnowledgeDungeoneering','KnowledgeGeography','KnowledgeNature',
'Perception','Profession','Ride','Spellcraft','Stealth','Survival','Swim']}

Rogue={'HP':8,'SkillPointsLevel':8,'Fortsave':'Poor','ReflexSave':'Good','WillSave':'Poor','BAB':'Medium',
'ClassSkills':['Acrobatics','Appraise','Bluff','Climb','Craft','Diplomacy','DisableDevice','Disguise','EscapeArtist','Intimidate',
'KnowledgeLocal','Linguistics','Perception','Perform','Profession','SenseMotive','SleightofHand','Stealth','Swim','UseMagicDevice']}

Sorcerer={'HP':6,'SkillPointsLevel':2,'Fortsave':'Poor','ReflexSave':'Poor','WillSave':'Good','BAB':'Low',
'ClassSkills':['Appraise','Bluff','Craft','Fly','Intimidate','KnowledgeArcana','Profession','Spellcraft','UseMagicDevice']}

Wizard={'HP':6,'SkillPointsLevel':2,'Fortsave':'Poor','ReflexSave':'Poor','WillSave':'Good','BAB':'Low',
'ClassSkills':['Appraise','Craft','Fly','KnowledgeArcana','KnowledgeDungeoneering','KnowledgeEngingeering','KnowledgeGeography',
'KnowledgeHistory','KnowledgeLocal','KnowledgeNature','KowledgeNobility','KnowledgePlanes','KnowledgeReligion','Linguistics',
'Profession','Spellcraft']}

#consider using pandas to integrate all skills information, including the stuff about class skills

#learn pandas
#install pandas
