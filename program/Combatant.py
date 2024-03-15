class Combatant:
    def __init__(self, level, atk, m_atk, defense, m_defense, max_health, spd, skills, weapon):
        self.level = level
        self.atk = atk
        self.m_atk = m_atk
        self.defense = defense
        self.m_defense = m_defense
        self.max_health = max_health
        self.current_health = self.max_health
        self.spd = spd
        self.skills = skills if skills else []
        self.weapon = weapon if weapon else []
        self.out_of_combat_status = False

    # Getter method for out_of_combat_status
    def get_out_of_combat_status(self):
        return self.out_of_combat_status

    # Setter method for out_of_combat_status
    def set_out_of_combat_status(self, out_of_combat_status):
        self.out_of_combat_status = out_of_combat_status


    # Getter method for level
    def get_level(self):
        return self.level

    # Setter method for level
    def set_level(self, level):
        self.level = level

    # Getter method for atk
    def get_atk(self):
        return self.atk

    # Setter method for atk
    def set_atk(self, atk):
        self.atk = atk

    # Getter method for m_atk
    def get_m_atk(self):
        return self.m_atk

    # Setter method for m_atk
    def set_m_atk(self, m_atk):
        self.m_atk = m_atk

    # Getter method for defense
    def get_defense(self):
        return self.defense

    # Setter method for defense
    def set_defense(self, defense):
        self.defense = defense

    # Getter method for m_defense
    def get_m_defense(self):
        return self.m_defense

    # Setter method for m_defense
    def set_m_defense(self, m_defense):
        self.m_defense = m_defense

    # Getter method for max_health
    def get_max_health(self):
        return self.max_health

    # Setter method for max_health
    def set_max_health(self, max_health):
        self.max_health = max_health
        # Ensure current health doesn't exceed new max health
        self.current_health = min(self.current_health, self.max_health)

    # Getter method for current_health
    def get_current_health(self):
        return self.current_health

    # Setter method for current_health
    def set_current_health(self, current_health):
        self.current_health = current_health

    # Getter method for spd
    def get_spd(self):
        return self.spd

    # Setter method for spd
    def set_spd(self, spd):
        self.spd = spd

    # Getter method for skills
    def get_skills(self):
        return self.skills

    # Setter method for skills
    def set_skills(self, skills):
        self.skills = skills

    # Getter method for weapon
    def get_weapon(self):
        return self.weapon

    # Setter method for weapon
    def set_weapon(self, weapon):
        self.weapon = weapon

    def take_damage(self, damage, skill_type):
        defense_modifier = self.defense if skill_type == "physical" else self.m_defense
        self.current_health = max(0, self.current_health - max(0, damage - defense_modifier))

    def restore_health(self, value):
        self.current_health = min(self.max_health, self.current_health + value)
