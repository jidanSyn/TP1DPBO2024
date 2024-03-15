

class Party:
    def __init__(self, members, name="", rank="F"):
        self.name = name
        self.rank = rank
        self.members = members
        self.completed_quests = 0

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for rank
    def get_rank(self):
        return self.rank

    # Setter method for rank
    def set_rank(self, rank):
        self.rank = rank

    # Getter method for members
    def get_members(self):
        return self.members

    # Setter method for members
    def set_members(self, members):
        self.members = members

    # Getter method for completed quests
    def get_completed_quests(self):
        return self.completed_quests

    # Setter method for completed quests
    def set_completed_quests(self, completed_quests):
        self.completed_quests = completed_quests

    def print_party_details(self):
        print(f"Party Name: {self.name}, Rank {self.rank}")
        print("Members:")
        for member in self.members:
            member.print_detail_pc()
