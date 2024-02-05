# Battling Knights Game Simulator

## Overview
This simulator processes a sequence of movements and actions for knights in a virtual game arena, determining their final states after all instructions have been executed. The game involves knights moving around a grid, picking up items to enhance their attack and defense, and battling each other according to specified rules.

## Requirements
- Python 3.x

## Files
- `main.py`: The main script that runs the game simulation.
- `knight.py`: Contains the `Knight` class definition.
- `item.py`: Contains the `Item` class definition.
- `moves.txt`: An input file with a list of moves and actions for the knights.
- `final_state.json`: The output file where the final states of the knights and items are saved.

## How to Run the Simulator
1. Ensure you have Python 3 installed on your system.
2. Place `main.py`, `knight.py`, `item.py`, and your `moves.txt` file in the same directory.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the files.
5. Run the command: `python main.py`
6. After execution, the final state of the game will be saved in `final_state.json` in the same directory.

## Using the Example Moves File

An example moves file is provided as `moves.txt.example`. To use it with the game simulator, you should rename this file to `moves.txt`. Here's how you can do it:

### Windows
- Open File Explorer and navigate to the directory containing `moves.txt.example`.
- Right-click on the file and select "Rename".
- Change the name to `moves.txt` and press Enter.

### macOS and Linux
- Open a Terminal.
- Navigate to the directory containing `moves.txt.example` using the `cd` command.
- Run the command `mv moves.txt.example moves.txt` to rename the file.

After renaming the file, follow the instructions in the "How to Run the Simulator" section to execute the game simulation using the example moves.

### Note on Customizing Moves
- You can edit `moves.txt` to simulate different sequences of actions. Ensure the file follows the specified format, starting with `GAME-START`, ending with `GAME-END`, and listing moves and actions for each knight in between. Invalid or malformed entries may cause the simulation to run incorrectly.


