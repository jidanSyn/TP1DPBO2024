class Quest:
    def __init__(self, name, desc, location, target, min_rank):
        self.name = name
        self.desc = desc
        self.location = location
        self.target = target
        self.min_rank = min_rank
        # gold reward? store in party or PC inv idk shop not impl'd yet

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for desc
    def get_desc(self):
        return self.desc

    # Setter method for desc
    def set_desc(self, desc):
        self.desc = desc

    # Getter method for location
    def get_location(self):
        return self.location

    # Setter method for location
    def set_location(self, location):
        self.location = location

    # Getter method for target
    def get_target(self):
        return self.target

    # Setter method for target
    def set_target(self, target):
        self.target = target

    # Getter method for min_rank
    def get_min_rank(self):
        return self.min_rank

    # Setter method for min_rank
    def set_min_rank(self, min_rank):
        self.min_rank = min_rank

    def describe_quest(self):
        print(f"\"{self.name}\"")
        print(f"Description:{self.desc}")
        print(f"Location:{self.location}")
        print(f"Minimum Party Rank:{self.min_rank}")
