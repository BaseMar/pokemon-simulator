class Move:
    def __init__(self, name, move_type, power):
        self.name = name
        self.move_type = move_type
        self.power = power

    def __str__(self):
        return f"{self.name} ({self.move_type}, Power: {self.power})"