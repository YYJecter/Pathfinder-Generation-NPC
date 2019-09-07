#this is to figure out skill point allocation

class Character_class:
  def __init__(self, HP, SkillPointsLevel, Fortsave, Reflexsave, Willsave, BAB, ClassSkills):
    self.HP=HP
    self.SkillPointsLevel=SkillPointsLevel
    self.Fortsave=Fortsave
    self.Reflexsave=Reflexsave
    self.Willsave=Willsave
    self.BAB=BAB
    self.ClassSkills=ClassSkills

Barbarian=Character_class(12,4,GoodSave(),PoorSave(),PoorSave(),BAB('High',Level),ClassSkills=('Acrobatics',
'Climb','Craft','DisableDevice','HandleAnimal','Intimidate','KnowledgeNature','Perception','Ride','Survival'))

skill_list={'Acrobatics':0,'Appraise':0,'Bluff':0,'Climb':0,'Craft':0,
'Diplomacy':0,'DisableDevice':0,'Disguise':0,'EscapeArtist':0,'Fly':0,
'HandleAnimal':0,'Heal':0,'Intimidate':0,'KnowledgeArcana':0,'KnowledgeDungeoneering':0,
'KnowledgeEngineering':0,'KnowledgeGeograpy':0,'KnowledgeHistory':0,
'KnowledgeLocal':0,'KnowledgeNature':0,'KnowledgeNobility':0,'KnowledgePlanes':0,
'KnowledgeReligion':0,'Linguistics':0,'Perception':0,'Perform':0,'Profession':0,
'Ride':0,'SenseMotive':0,'SleightofHand':0,'Spellcraft':0,'Stealth':0,
'Survival':0,'Swim':0,'Use Magic Device':0}

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




def armor_check_penalty(skill):
  if skill in ['Acrobatics', 'DisableDevice', 'EscapeArtist', 'Fly', 'Ride', 'SleightofHand', 'Stealth', 'Swim']:
    return True
  else:
    return False


def stat_skill_mod(skill):
  if skill in ['Climb','Climb']:
    return StrMod
  elif skill in ['Acrobatics', 'DisableDevice', 'EscapeArtist','Fly','Ride','SleightofHand','Stealth']:
    return DexMod
  elif skill in ['Appraise','Craft','KnowledgeArcana','KnowledgeDungeoneering','KnowledgeEngineering','KnowledgeGeography','KnowledgeHistory','KnowledgeLocal','KnowledgeNature','KnowledgeNobility','KnowledgePlanes','KnowledgeReligion','Linguistics','Spellcraft']:
    return IntMod
  elif skill in ['Heal','Perception','Profession','SenseMotive','Survival']:
    return WisMod
  elif skill in ['Bluff','Diplomacy','Disguise','HandleAnimal','Intimidate','Perform','UseMagicDevice']:
    return ChaMod