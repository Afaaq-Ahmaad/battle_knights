
directions = {
    "N": (-1, 0), 
    "S": (1, 0), 
    "E": (0, 1), 
    "W": (0, -1)
    }


class Knight:
    def __init__(self, name, position, full_name):
        self.name = name
        self.full_name = full_name  
        self.position = position
        self.status = "LIVE"
        self.item = None  
        self.attack = 1
        self.defence = 1

    def move(self, direction, items, knights, board_size=8):
        if self.status != "LIVE":
            return False

        dx, dy = directions[direction]
        x, y = self.position
        new_position = (x + dx, y + dy)

        # Check for board boundaries
        if 0 <= new_position[0] < board_size and 0 <= new_position[1] < board_size:
            self.position = new_position
            self.check_item_pickup(items)
            self.check_for_battle(knights)  # Pass knights dict directly
            return True
        else:
            self.drown()
            return False



    def check_for_battle(self, knights):
        for opponent in knights.values():  # This is where you iterate over the knights
            if opponent != self and opponent.position == self.position and opponent.status == "LIVE":
                self.fight(opponent)


    def fight(self, opponent):
        if self.attack + 0.5 > opponent.defence:  # Attacker has advantage
            opponent.die()
        else:
            self.die()  # Defender wins in a tie or has higher defence

    def drown(self):
        self.status = "DROWNED"
        self.attack = 0
        self.defence = 0
        self.drop_item()

    def die(self):
        self.status = "DEAD"
        self.drop_item()

    def check_item_pickup(self, items):
        for item in items.values():
            if self.position == item.position and not item.equipped:
                self.equip_item(item)
                item.equip()
                break  

    def equip_item(self, item):
        self.item = item.type
        self.attack += item.attack_bonus
        self.defence += item.defence_bonus

    def drop_item(self):
        global items  #items is a global dictionary of Item instances
        if self.item:
            for item in items.values():
                if item.type == self.item:
                    item.drop(self.position if self.status == "DEAD" else None)
                    break
            self.item = None
            self.attack = 1  # Reset to base attack
            self.defence = 1  # Reset to base defence

    def __repr__(self):
        return f"{self.name} at {self.position} with {self.item}, ATK: {self.attack}, DEF: {self.defence}"

