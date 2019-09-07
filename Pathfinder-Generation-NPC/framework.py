#this is meant to randomly generate a npc.  for now it is basic
#later i hope to incorporate class, either via input that can change the
#parameters of the stats in the first section, or for  assignment
#based on the stats generated, ex: str>=18 and dex<=8 leads to fighter
#and int>=16 leads to wizard, etc
#this could be incorporated with the random item generator to equip the
#generated npcs.  this would also allow for fewer inputs, like with the AC
#no longer having to be manually input
#i've commented out the to hit part for now

 

import random


def StatRoll():
  return(int(random.randint(1,4)+random.randint(1,4)+random.randint(1,4)+random.randint(1,4)+random.randint(1,4)))

def StatMod(n):
  return((n-10)//2)


Strength=int(StatRoll())
Dexterity=int(StatRoll())
Constitution=int(StatRoll())
Intelligence=int(StatRoll())
Wisdom=int(StatRoll())
Charisma=int(StatRoll())


StrMod=StatMod(Strength)
DexMod=StatMod(Dexterity)
ConMod=StatMod(Constitution)
IntMod=StatMod(Intelligence)
WisMod=StatMod(Wisdom)
ChaMod=StatMod(Charisma)

#now we figure out class.  i want this to be simpler, but its currently the
#best i could get.  i plan on moving the class that most needs a particular stat to
#the top of the list, i also want to figure out a way to contract this to be more
#elegant

 

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




#BarbarianInformation = {
#    'HPRoll':d12,
#    'SkillPointsPerLevel':4+IntMod,
#    'BaseAttackBonus':Level} 




#now we define level and HP

Level=input('Level: ',)
print('Level: ',Level)
HP=int(0)
HPRolls=int(0)

while HPRolls<int(Level):

  HPRolls=HPRolls+1

  HP=HP+random.randint(1,8)+ConMod

#the above 1d8 is a place holder for untill we get classes

#now the AC

#AC=10 + armor bonus + Shield bonus + Dexterity modifier + other modifiers

#this could be integrated with the item random generator if desired

Base_AC=int(10)

#Armor_AC_Bonus=input('Armor AC: ',)

Armor_AC_Bonus=0#this is temporary
Armor_AC_Bonus=int(Armor_AC_Bonus)
#Shield_AC_Bonus=input('Shield AC: ',)
Shield_AC_Bonus=0#this is temporary
Shield_AC_Bonus=int(Shield_AC_Bonus)
#Other_AC_Bonus=input('Other AC Bonus: ',)
Other_AC_Bonus=0#this is temporary
Other_AC_Bonus=int(Other_AC_Bonus)
Total_AC=int()
Total_AC=Base_AC+Armor_AC_Bonus+Shield_AC_Bonus+DexMod+Other_AC_Bonus

#making space
print()
#to hit
#im not including magic for now, and i'm leaving it as auto attacking to
#show the mechanism
Die_Roll=int(random.randint(1,20))
#attacktype=input("'Melee' or 'Ranged'", )
#if attacktype=='Melee':
#  print('to hit: ', Strength_Mod+Die_Roll)
#elif attacktype=='Ranged':
#  print('to hit: ', Dexterity_Mod+Die_Roll)
#else:
#  print('not understood')

 


#make some space

print()
print()

 

#skill entries

#for now i'm not doing anything for skills in this file, and have moved that to the next file over

 

 

 

#This is where i would put the items

 

#now to show the Character sheet for the randomly generated being

#printed HP and AC

print('HP: ',HP)

print('AC:', Total_AC)

print()

 

#printed base stats and modifiers

print('Str:',Strength,'Mod:', StrMod)

print('Dex:',Dexterity, 'Mod:', DexMod)

print('Con:', Constitution, 'Mod:', ConMod)

print('Int:', Intelligence, 'Mod:', IntMod)

print('Wis:', Wisdom, 'Mod:', WisMod)

print('Cha:', Charisma, 'Mod:', ChaMod)

print()

 

#printed hit bonus summary

#later this will include the weapon equipted and the modifiers from that, and also base attack bonus

print('Melee to hit bonus: ', StrMod)

print('Ranged to hit bonus: ', DexMod)

print()

 
