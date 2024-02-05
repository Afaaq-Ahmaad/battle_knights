import json
from knight import Knight
from item import Item



knights = {
    "R": Knight("R", (0, 0), "Red"),
    "B": Knight("B", (7, 0), "Blue"),
    "G": Knight("G", (7, 7), "Green"),
    "Y": Knight("Y", (0, 7), "Yellow"),
}

items = {
    "A": Item("A", (2, 2), "Axe", 2, 0),
    "D": Item("D", (2, 5), "Dagger", 1, 0),
    "M": Item("M", (5, 2), "MagicStaff", 1, 1),
    "H": Item("H", (5, 5), "Helmet", 0, 1),
}




def process_moves(file_path, knights, items):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        for line in lines[1:-1]:  # Skip GAME-START and GAME-END
            knight_name, direction = line.split(':')
            if knight_name in knights:
                knights[knight_name].move(direction, items, knights) 


            
def generate_final_state(knights, items, file_name='final_state.json'):
    final_state = {}
    
    # Iterate through knights to populate their final state
    for code, knight in knights.items():
        final_state[knight.full_name] = [
            list(knight.position) if knight.position else None,
            knight.status.upper(),
            knight.item if knight.item else None,
            knight.attack,
            knight.defence
        ]

    # Iterate through items to populate their final state
    for code, item in items.items():
        final_state[item.type] = [
            list(item.position) if item.position else None,
            item.equipped
        ]
    
    # Save the final state to a JSON file
    with open(file_name, 'w') as json_file:
        json.dump(final_state, json_file, indent=4)






if __name__ == "__main__":
    process_moves("moves.txt", knights, items)
    generate_final_state(knights, items)

