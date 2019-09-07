skill_list={'Acrobatics':2, 'Bluff':0,'Knowledge_History':1,'Spellcraft':1}

char_class=('Acrobatics', 'Bluff', 'Spellcraft')



def class_skill_point_allocation():
  for key in skill_list:
    if key in skill_list and key in char_class and skill_list[key]>0:
      skill_list[key]=skill_list[key]+3


class_skill_point_allocation()

#print(skill_list)

print(skill_list)