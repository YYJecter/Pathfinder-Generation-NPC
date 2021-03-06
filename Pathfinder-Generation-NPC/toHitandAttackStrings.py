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


#
#Base attack bonus goes by one of three routes, here they are

def BAB(HighMediumLowBAB,Level):
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
  





Level=6

print(BAB('High',Level))
print(BAB('Medium',Level))
#print(DexMod)
print(SituationalAttackBonus('High',Level,'Ranged'))
print(SituationalAttackBonus('High',Level,'Melee'))

print('AttackString',AttackString(BAB('High',Level),'Melee'))
print('AttackString',AttackString(BAB('High',Level),'Ranged'))



TargetAC=10



#Find a way to separate out the tuples of the attack string
#so that each one can be evaluated against the Target AC
#how to turn tuple into list? or maybe temporarily store the tuple
#also, look into json things.