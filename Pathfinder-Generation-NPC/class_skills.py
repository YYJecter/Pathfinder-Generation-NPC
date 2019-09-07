

import class_selection
import class_of_classes as coc

print(class_selection.temp_character_class)

Temp = getattr(coc, 'Fighter')()
print(Temp.class_skills)


Temp = getattr(coc, class_selection.temp_character_class)()
print(Temp.HP)

'''
skill_total(skill) = skillmod + invested_points + class_bonus + armor_modifier

while total_skill_points > 0: 
  (sort skills by total_skill)
  for skills in skill list
    if skill == class skill and training_needed == True and invested_points = 0:
      invested_points +=1
      total skill points -=1
    elif skill == class skill and invested_points = 0: 
      invested_points +=1
      total_skill_points -=1
    elif skill training_needed == True and invested_points = 0:
      invested_points +=1
      total_skill_points -=1
    elif skill_total(skill) = fifth highest in value: 
      invested_points +=1
      total_skill_points -=1
sort skills alphabetical by name
print out skill chart

skill chart:
first the below as headers, then for each skill
  skill_total = skillmod + invested points + class bonus + armor_modifier
'''



'''
what do i need to do now?
1. assign class
2. skill point allocation
3. class selection
4. showing character information
5. ?feats?
6. ?
'''