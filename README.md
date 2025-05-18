Dicing Game
A simple command-line dice game implemented in Python where you roll five dice and have opportunities to improve your hand.

Description
Dicing Game simulates rolling five six-sided dice. After an initial roll, you get two additional opportunities to re-roll any of the dice to try to achieve the best possible combination.

Features
- Roll five dice at once
- Select specific dice to re-roll on your second and third attempts
- Simple command-line interface
- Random dice values using Python's random module

How to Play
- Run the game
- Select option 1 to start a new game
- After the first roll, enter the positions of dice you want to re-roll (1-5)
- Separate positions by space or comma
- Press Enter to keep all dice
- After the second roll, you get one more chance to re-roll dice
- Your final hand is displayed

Requirements
- Python 3.x

Installation
No special installation required. Just download the script and run it with Python:
python dicing_game.py

Example usage:
==================================================================================================
======= MENU =======
1) Roll dice
2) Exit
Select an option (1/2): 1

=== FIRST ROLL ===
[3] [1] [4] [2] [6]

Which dice do you want to roll again? (positions 1-5 separated by space/comma, Enter = none): 1,2

=== SECOND ROLL ===
[5] [6] [4] [2] [6]

Which dice do you want to roll again? (positions 1-5 separated by space/comma, Enter = none): 4

=== THIRD ROLL ===
[5] [6] [4] [5] [6]

Final result: [5] [6] [4] [5] [6]
============================================================================================


Game Logic:

The game consists of:
- An initial roll of 5 dice
- Two opportunities to choose which dice to roll again
- Strategy to achieve the best possible combination


License
This project is open source and available under the MIT License.
