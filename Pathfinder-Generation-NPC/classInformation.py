#Class List

def Die(n):
  import random
  return(random.randint(1,n))

Barbarian={'HP':Die(12),'SkillPointsLevel':4}

Bard={'HP':Die(8),'SkillPointsLevel':6}

Cleric={'HP':Die(8),'SkillPointsLevel':2}

Druid={'HP':Die(8),'SkillPointsLevel':4}

Fighter={'HP':Die(10),'SkillPointsLevel':2}

Monk={'HP':Die(8),'SkillPointsLevel':4}

Paladin={'HP':Die(10),'SkillPointsLevel':2}

Ranger={'HP':Die(10),'SkillPointsLevel':6}

Rogue={'HP':Die(8),'SkillPointsLevel':8}

Sorcerer={'HP':Die(6),'SkillPointsLevel':2}

Wizard={'HP':Die(6),'SkillPointsLevel':2}

print(Wizard)