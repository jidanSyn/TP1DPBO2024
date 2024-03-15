class Character:
    def __init__(self, name="Lumine", gender='Female'):
        self.name = name
        self.gender = gender
    
    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for gender
    def get_gender(self):
        return self.gender

    # Setter method for gender
    def set_gender(self, gender):
        self.gender = gender

    def print_data(self):
        print(f"Name: {self.name} | Gender: {self.gender}")
