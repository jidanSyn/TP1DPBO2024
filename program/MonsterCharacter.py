from Character import Character
from Combatant import Combatant

class MonsterCharacter(Character, Combatant):
    def __init__(self, name, gender, max_health = 5, atk = 1, defense = 1, spd = 1, m_atk = 1, m_defense = 1, role = None, skills = None,  weapon = None):
        Character.__init__(self, name, gender)
        Combatant.__init__(self, 1, atk, m_atk, defense, m_defense, max_health, spd, skills, weapon)
        self.role = role
        self.exp = 0
