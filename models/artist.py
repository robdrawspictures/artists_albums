class Artist:
    def __init__(self, name, id = None):
        self.name = name
        self.id = id

    def rebrand(self, new_name):
        self.name = new_name