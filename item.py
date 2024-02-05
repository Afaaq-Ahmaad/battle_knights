class Item:
    def __init__(self, code, position, item_type, attack_bonus, defence_bonus):
        self.code = code
        self.position = position
        self.type = item_type
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.equipped = False

    def equip(self):
        self.equipped = True

    def drop(self, position):
        self.equipped = False
        self.position = position

    def __repr__(self):
        return f"{self.type} at {self.position}, Equipped: {self.equipped}"


