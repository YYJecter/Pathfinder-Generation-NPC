StrMod=0
DexMod=0
ConMod=0
IntMod=0
WisMod=0
ChaMod=0

Level = int(1)

def GoodSave():
  return 2+(Level//2)
  
def PoorSave():
  return 0+(Level//3)

def BAB(HighMediumLowBAB, Level):
  if HighMediumLowBAB=='High':
    return int(Level)
  elif HighMediumLowBAB=='Medium':
    return int(((.75*Level)//1))
  elif HighMediumLowBAB=='Low':
    return int(((.5*Level)//1))
  else:
    return('BAB ERROR')

'''
put in a dictionary for trained, and armor issue
make class work
'''

ClassList={'Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Wizard'}



  


#make this either pandas based or a list of lists or something, but right now this is too much, dictionary of list of lists?

#make each of the skill lists a function.  then make a function that combines them

skill_list={'Acrobatics':0,'Appraise':0,'Bluff':0,'Climb':0,'Craft':0,
'Diplomacy':0,'DisableDevice':0,'Disguise':0,'EscapeArtist':0,'Fly':0,
'HandleAnimal':0,'Heal':0,'Intimidate':0,'KnowledgeArcana':0,'KnowledgeDungeoneering':0,
'KnowledgeEngineering':0,'KnowledgeGeograpy':0,'KnowledgeHistory':0,
'KnowledgeLocal':0,'KnowledgeNature':0,'KnowledgeNobility':0,'KnowledgePlanes':0,
'KnowledgeReligion':0,'Linguistics':0,'Perception':0,'Perform':0,'Profession':0,
'Ride':0,'SenseMotive':0,'SleightofHand':0,'Spellcraft':0,'Stealth':0,
'Survival':0,'Swim':0,'Use Magic Device':0}

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

def skill_training_necessary(skill):
    if skill in ['DisableDevise', 'HandleAnimal', 'KnowledgeArcana', 'KnowledgeDungeoneering',
    'KnowledgeEngineering','KnowledgeGeograpy','KnowledgeHistory', 'KnowledgeLocal','KnowledgeNature', 
    'KnowledgeNobility','KnowledgePlanes','KnowledgeReligion','Linguistics']:
        return True
    else:
        return False



'''
armor check penalty is weather the armor has an adverse effect on how well the skill is done
as there are fewer things it effects than things it doesn't, ive noted it as, if it has a penalty, then yes,
if not, then no
'''

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

def armor_check_penalty(skill):
  if skill in ['Acrobatics', 'DisableDevice', 'EscapeArtist', 'Fly', 'Ride', 'SleightofHand', 'Stealth', 'Swim']:
    return True
  else:
    return False




skill_mods={'Acrobatics':DexMod,'Appraise':IntMod,'Bluff':ChaMod,
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


def stat_skill_mod(skill):
  if skill in ['Climb','Climb']:
    return StrMod
  elif skill in ['Acrobatics', 'DisableDevice', 'EscapeArtist','Fly','Ride','SleightofHand','Stealth']:
    return DexMod
  elif skill in ['Appraise','Craft','KnowledgeArcana','KnowledgeDungeoneering','KnowledgeEngineering',
  'KnowledgeGeography','KnowledgeHistory','KnowledgeLocal','KnowledgeNature','KnowledgeNobility','KnowledgePlanes',
  'KnowledgeReligion','Linguistics','Spellcraft']:
    return IntMod
  elif skill in ['Heal','Perception','Profession','SenseMotive','Survival']:
    return WisMod
  elif skill in ['Bluff','Diplomacy','Disguise','HandleAnimal','Intimidate','Perform','UseMagicDevice']:
    return ChaMod



#
#
#



#This is the function that shows the number of total skill points based on class, level, and IntMod
def total_skill_points(npc_class,Level,IntMod):
  return Level*(IntMod+npc_class)
  return npc_classs


def class_skill_point_allocation():
  for key in skill_list:
    if key in skill_list and key in char_class and skill_list[key]>0:
      skill_list[key]=skill_list[key]+3




class CharacterClass:

  def bab(self,Level,tier):
      if tier == 'high':
        return int(Level)
      elif tier == 'medium':
        return int(((.75*Level)//1))
      elif tier == 'low':
        return int(((.5*Level)//1))
      else: 
        return 'bab_error'

  def base_save(self,Level,goodness):
      if goodness == 'good':
        return 2+(Level//2)
      elif goodness == 'bad':
        return 0+(Level//3)

  def __init__(self):
    self.HP = Level*(ConMod+1)
    self.SkillPointsLevel = Level*(IntMod+1)
    self.Fortsave = self.base_save(Level,'bad')
    self.Reflexsave = self.base_save(Level,'bad')
    self.Willsave = self.base_save(Level,'bad')
    self.BAB = self.bab(Level,'low')
    self.class_skills=['Acrobatics','Appraise','Bluff','Climb',
    'Craft','Diplomacy','DisableDevice','Disguise','EscapeArtist',
    'Fly','HandleAnimal','Heal','Intimidate','KnowledgeArcana',
    'KnowledgeDungeoneering','KnowledgeEngineering','KnowledgeGeograpy',
    'KnowledgeHistory','KnowledgeLocal','KnowledgeNature','KnowledgeNobility',
    'KnowledgePlanes','KnowledgeReligion','Linguistics','Perception','Perform',
    'Profession','Ride','SenseMotive','SleightofHand','Spellcraft','Stealth',
    'Survival','Swim','Use Magic Device']

class Barbarian(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+12)
    self.SkillPointsLevel = Level*(IntMod+4)
    self.Fortsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'high')
    self.class_skills = ['Acrobatics','Climb','Craft','DisableDevice','HandleAnimal','Intimidate','KnowledgeNature','Perception','Ride','Survival']

class Bard(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+8)
    self.SkillPointsLevel = Level*(IntMod+6)
    self.ReflexSave = self.base_save(Level,'good')
    self.Willsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'medium')
    self.class_skills = ['Craft','Profession']

class Cleric(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+8)
    self.SkillPointsLevel = Level*(IntMod+2)
    self.Fortsave = self.base_save(Level,'good')
    self.Willsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'medium')
    self.class_skills = ['Appraise','Craft','Diplomacy','Heal','KnowledgeArcana','KnowledgeHistory',
    'KnowledgeNobility','KnowledgePlanes','KnowledgeReligion','Linguistics','Profession','SenseMotive','Spellcraft']

class Druid(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+8)
    self.SkillPointsLevel = Level*(IntMod+4)
    self.Fortsave = self.base_save(Level,'good')
    self.Willsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'medium')
    self.class_skills = ['Climb','Craft','Fly','HandleAnimal','Heal','KnowledgeGeography','KnowledgeNature','Perception',
    'Profession','SenseMotive','Spellcraft','Survival','Swim']

class Fighter(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+10)
    self.SkillPointsLevel = Level*(IntMod+2)
    self.Fortsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'high')
    self.class_skills = ['Climb','Craft','HandleAnimal','Intimidate','KnowledgeDungeoneering','KnowledgeEngingeering',
    'Profession','Ride','Survival','Swim']

class Monk(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+8)
    self.SkillPointsLevel = Level*(IntMod+4)
    self.Fortsave = self.base_save(Level,'good')
    self.Reflexsave = self.base_save(Level,'good')
    self.Willsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'medium')
    self.class_skills = ['Acrobatics','Climb','Craft','EscapeArtist','Intimidate','KnowledgeHistory',
    'KnowledgeReligion','Perception','Perform','Profession','Ride','SenseMotive','Stealth','Swim']

class Paladin(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+10)
    self.SkillPointsLevel = Level*(IntMod+2)
    self.Fortsave = self.base_save(Level,'good')
    self.Willsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'high')
    self.class_skills = ['Craft','Diplomacy','HandleAnimal','Heal','KnowledgeNobility','KnowledgeReligion',
    'Profession','Ride','SenseMotive','Spellcraft']

class Ranger(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+10)
    self.SkillPointsLevel = Level*(IntMod+6)
    self.Fortsave = self.base_save(Level,'good')
    self.Reflexsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'high')
    self.class_skills = ['Climb','Craft','HandleAnimal','Heal','Intimidate','KnowledgeDungeoneering','KnowledgeGeography',
    'KnowledgeNature','Perception','Profession','Ride','Spellcraft','Stealth','Survival','Swim']

class Rogue(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+8)
    self.SkillPointsLevel = Level*(IntMod+8)
    self.Reflexsave = self.base_save(Level,'good')
    self.BAB = self.bab(Level,'medium')
    self.class_skills = ['Acrobatics','Appraise','Bluff','Climb','Craft','Diplomacy','DisableDevice',
    'Disguise','EscapeArtist','Intimidate','KnowledgeLocal','Linguistics','Perception','Perform','Profession',
    'SenseMotive','SleightofHand','Stealth','Swim','UseMagicDevice']

class Sorcerer(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+6)
    self.SkillPointsLevel = Level*(IntMod+2)
    self.Willsave = self.base_save(Level,'good')
    self.class_skills = ['Appraise','Bluff','Craft','Fly','Intimidate','KnowledgeArcana','Profession','Spellcraft',
    'UseMagicDevice']

class Wizard(CharacterClass):
  def __init__(self):
    super().__init__()
    self.HP = Level*(ConMod+6)
    self.SkillPointsLevel = Level*(IntMod+2)
    self.Willsave = self.base_save(Level,'good')
    self.class_skills = ['Appraise','Craft','Fly','KnowledgeArcana','KnowledgeDungeoneering','KnowledgeEngingeering',
    'KnowledgeGeography','KnowledgeHistory','KnowledgeLocal','KnowledgeNature','KowledgeNobility','KnowledgePlanes',
    'KnowledgeReligion','Linguistics','Profession','Spellcraft']