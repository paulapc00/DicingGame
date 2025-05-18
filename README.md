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
- 
Installation
No special installation required. Just download the script and run it with Python:
python dicing_game.py

Example Usage
======= MENÚ =======
1) Lanzar dados
2) Salir
Selecciona una opción (1/2): 1

=== PRIMER LANZAMIENTO ===
[3] [1] [4] [2] [6]

¿Qué dados vuelves a tirar? (posiciones 1-5 separadas por espacio/coma, Enter = ninguno): 1,2

=== LANZAMIENTO 2 ===
[5] [6] [4] [2] [6]

¿Qué dados vuelves a tirar? (posiciones 1-5 separadas por espacio/coma, Enter = ninguno): 4

=== LANZAMIENTO 3 ===
[5] [6] [4] [5] [6]

>>> Resultado final: [5] [6] [4] [5] [6]

License
This project is open source and available under the MIT License.
