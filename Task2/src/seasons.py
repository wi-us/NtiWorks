seasonsArr = []

class Season:
    def __init__(self, name, description, interface, color):
        self.name = name
        self.description = description
        self.interface = interface
        self.color = color
        seasonsArr.append(self)
        