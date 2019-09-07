import random

def Die(n):
  import random
  return(random.randint(1,n))

def StatRoll():
  return (Die(4)+Die(4)+Die(4)+Die(4)+Die(4))

Strength=StatRoll()
Dexterity=StatRoll()
Constitution=StatRoll()
Intelligence=StatRoll()
Wisdom=StatRoll()
Charisma=StatRoll()

def StatMod(n):
  return((n-10)//2)

StrMod=StatMod(Strength)
DexMod=StatMod(Dexterity)
ConMod=StatMod(Constitution)
IntMod=StatMod(Intelligence)
WisMod=StatMod(Wisdom)
ChaMod=StatMod(Charisma)

'''
better idea for class selection.  choose order of important stats.  then divide value by number on list.  find a way to assign total value on the 
  list, then choose largest value, ex: wizard: (intelligence//1)+(dexterity//2)+(constitution//3)+(wisdom//4)+(charisma//5)+(strength//6)=sum and
  if that sum is higher than the sum for each other class, then wizard wins.
  find a way to 

'''
'''
class_selection_Wizard: intelligence,dexterity, constitution, wisdom, charisma, strength

'''

class_selection_barbarian = ((Strength//1)+(Dexterity//2)+(Constitution//3)+(Wisdom//4)+(Intelligence//5)+(Charisma//6),'Barbarian')
class_selection_bard = ((Charisma//1)+(Dexterity//2)+(Intelligence//3)+(Strength//4)+(Constitution//5)+(Wisdom//6),'Bard')
class_selection_cleric = ((Charisma//1)+(Constitution//2)+(Strength//3)+(Wisdom//4)+(Intelligence//5)+(Dexterity//6),'Cleric')
class_selection_druid = ((Wisdom//1)+(Dexterity//2)+(Constitution//3)+(Strength//4)+(Intelligence//5)+(Charisma//6),'Druid')
class_selection_fighter = ((Strength//1)+(Constitution//2)+(Dexterity//3)+(Wisdom//4)+(Intelligence//5)+(Charisma//6),'Fighter')
class_selection_monk = ((Wisdom//1)+(Strength//2)+(Dexterity//3)+(Constitution//4)+(Intelligence//5)+(Charisma//6),'Monk')
class_selection_paladin = ((Strength//1)+(Charisma//2)+(Constitution//3)+(Dexterity//4)+(Wisdom//5)+(Intelligence//6),'Paladin')
class_selection_ranger = ((Dexterity//1)+(Wisdom//2)+(Strength//3)+(Intelligence//4)+(Constitution//5)+(Charisma//6),'Ranger')
class_selection_rogue = ((Dexterity//1)+(Intelligence//2)+(Strength//3)+(Charisma//4)+(Wisdom//5)+(Constitution//6),'Rogue')
class_selection_sorcerer = ((Charisma//1)+(Dexterity//2)+(Constitution//3)+(Wisdom//4)+(Strength//5)+(Intelligence//6),'Sorcerer')
class_selection_wizard = ((Intelligence//1)+(Dexterity//2)+(Constitution//3)+(Wisdom//4)+(Charisma//5)+(Strength//6),'Wizard')

'''
print(Strength,Dexterity,Constitution,Intelligence,Wisdom,Charisma)

print(class_selection_barbarian,
class_selection_bard,
class_selection_cleric,
class_selection_druid,
class_selection_fighter,
class_selection_monk,
class_selection_paladin,
class_selection_ranger,
class_selection_rogue,
class_selection_sorcerer,
class_selection_wizard)
'''

class_selection_list=[class_selection_barbarian,class_selection_bard,class_selection_cleric,class_selection_druid,
  class_selection_fighter,class_selection_monk,class_selection_paladin,class_selection_ranger,class_selection_rogue,
  class_selection_sorcerer,class_selection_wizard]

class_selection_list.sort(reverse=True)
print(class_selection_list)
print()
#print(class_selection_list[0])

x=0
for _ in range(len(class_selection_list)-1):
  if (class_selection_list[0][0])==(class_selection_list[x+1][0]):
    x=x+1


print()
import random
temp=random.randint(0,x)
#print(temp)

temp_character_class=(class_selection_list[temp][1])
