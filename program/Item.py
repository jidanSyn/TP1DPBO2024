class Item:
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    # Getter method for name
    def get_name(self):
        return self.name

    # Setter method for name
    def set_name(self, name):
        self.name = name

    # Getter method for description
    def get_description(self):
        return self.description

    # Setter method for description
    def set_description(self, description):
        self.description = description
