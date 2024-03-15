class Role:

    def __init__(self, name, atk_growth, m_atk_growth, health_growth, spd_growth, default_skills, default_weapon):
        self.name = name
        self.atk_growth = atk_growth
        self.m_atk_growth = m_atk_growth
        self.health_growth = health_growth
        self.spd_growth = spd_growth
        self.default_skills = default_skills
        self.default_weapon = default_weapon

    # Getter methods
    def get_name(self):
        return self.name

    def get_atk_growth(self):
        return self.atk_growth

    def get_m_atk_growth(self):
        return self.m_atk_growth

    def get_health_growth(self):
        return self.health_growth

    def get_spd_growth(self):
        return self.spd_growth

    def get_default_skills(self):
        return self.default_skills
    
    def get_default_weapon(self):
        return self.default_weapon

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_atk_growth(self, atk_growth):
        self.atk_growth = atk_growth

    def set_m_atk_growth(self, m_atk_growth):
        self.m_atk_growth = m_atk_growth

    def set_health_growth(self, health_growth):
        self.health_growth = health_growth

    def set_spd_growth(self, spd_growth):
        self.spd_growth = spd_growth

    def set_default_skills(self, default_skills):
        self.default_skills = default_skills

    def set_default_weapon(self, default_weapon):
        self.default_weapon = default_weapon
