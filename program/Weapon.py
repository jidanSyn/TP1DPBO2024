from Item import Item

class Weapon(Item):
    def __init__(self, name, desc="", atk_mod=1, heal_mod=1, m_atk_mod=1, refinement=0):
        super().__init__(name, desc)
        self.atk_mod = atk_mod
        self.m_atk_mod = m_atk_mod
        self.heal_mod = heal_mod
        self.refinement = refinement

    # Getter method for atk_mod
    def get_atk_mod(self):
        return self.atk_mod

    # Setter method for atk_mod
    def set_atk_mod(self, atk_mod):
        self.atk_mod = atk_mod

    # Getter method for m_atk_mod
    def get_m_atk_mod(self):
        return self.m_atk_mod

    # Setter method for m_atk_mod
    def set_m_atk_mod(self, m_atk_mod):
        self.m_atk_mod = m_atk_mod

    # Getter method for heal_mod
    def get_heal_mod(self):
        return self.heal_mod

    # Setter method for heal_mod
    def set_heal_mod(self, heal_mod):
        self.heal_mod = heal_mod

    # Getter method for refinement
    def get_refinement(self):
        return self.refinement

    # Setter method for refinement
    def set_refinement(self, refinement):
        self.refinement = refinement
