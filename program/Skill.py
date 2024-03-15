class Skill:
    def __init__(self, name, modifier=1, desc='', skill_type="physical", target_type="enemy", flavor_text=""):
        self._name = name
        self._desc = desc
        self._skill_type = skill_type  # physical, magical, healing, assume healing targets only allies
        self._modifier = modifier  #
        self._target_type = target_type
        self._flavor_text = flavor_text

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for desc
    def get_desc(self):
        return self._desc

    # Setter method for desc
    def set_desc(self, desc):
        self._desc = desc

    # Getter method for skill_type
    def get_skill_type(self):
        return self._skill_type

    # Setter method for skill_type
    def set_skill_type(self, skill_type):
        self._skill_type = skill_type

    # Getter method for modifier
    def get_modifier(self):
        return self._modifier

    # Setter method for modifier
    def set_modifier(self, modifier):
        self._modifier = modifier

    # Getter method for target_type
    def get_target_type(self):
        return self._target_type

    # Setter method for target_type
    def set_target_type(self, target_type):
        self._target_type = target_type

    # Getter method for flavor_text
    def get_flavor_text(self):
        return self._flavor_text

    # Setter method for flavor_text
    def set_flavor_text(self, flavor_text):
        self._flavor_text = flavor_text

    def calculate_value(self, source):
        if self._skill_type == "physical":
            main_stat = source.get_atk()
            weapon_stat = source.get_weapon().get_atk_mod()
        elif self._skill_type == "magical":
            main_stat = source.get_m_atk()
            weapon_stat = source.get_weapon().get_m_atk_mod()
        elif self._skill_type == "healing":
            main_stat = source.get_max_health()  # fk it for now its based on max hp (tank cleric lol?) idk should be INT or smth usually in games
            weapon_stat = source.get_weapon().get_heal_mod()

        return (main_stat + weapon_stat) * self._modifier
