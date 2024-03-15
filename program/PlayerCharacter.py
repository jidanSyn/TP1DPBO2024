from Character import Character
from Combatant import Combatant

class PlayerCharacter(Character, Combatant):
    def __init__(self, name, gender, max_health = 5, atk = 1, defense = 1, spd = 1, m_atk = 1, m_defense = 1, role = None, skills = None,  weapon = None):
        Character.__init__(self, name, gender)
        Combatant.__init__(self, 1, atk, m_atk, defense, m_defense, max_health, spd, skills, weapon)
        self.role = role
        self.exp = 0

        if role:
            self.skills.extend(role.default_skills)
            if not weapon:
                self.weapon = role.get_default_weapon()
        

        
    
    def display_skills(self):
        final_index = None
        for index, skill in enumerate(self.skills):
            print(f"{index + 1}. {skill.get_name()}")
            final_index = index
        return final_index

    def level_up(self):
        self.atk += self.role.get_atk_growth()
        self.m_atk += self.role.get_m_atk_growth()
        self.max_health += self.role.get_health_growth()
        self.spd += self.role.get_spd_growth()
        self.level += 1
        self.exp = 0
        print(f"{self.name} has leveled up to Lv.{self.level}!")

    def print_detail_pc(self):
        self.print_data()
        print(f"Status\nLevel: {self.level}\nAttack: {self.atk}\nMagic Attack: {self.m_atk}")
        print(f"Max Health: {self.max_health}")
        print(f"Speed: {self.spd}")
        print(f"Role: {self.role.name}")
        print("Skills:")
        for skill in self.skills:
            print(f" - {skill.get_name()}")
        print("Weapon:")
        print(f" - Name: {self.weapon.get_name()}")
        print(f" - Description: {self.weapon.get_description()}")
        print(f" - Attack Modifier: {self.weapon.get_atk_mod()}")
        print(f" - Magic Attack Modifier: {self.weapon.get_m_atk_mod()}")
        print(f" - Healing Modifier: {self.weapon.get_heal_mod()}")
