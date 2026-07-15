# sliding_puzzle_game
# Tkinter Slide Puzzle (15-Puzzle)

A lightweight, classic 15-Puzzle game built entirely in Python using the standard `tkinter` library. The game features a 4x4 grid of numbered tiles where the objective is to arrange them in sequential order (1 through 15) by sliding tiles into the empty space.

---

## Key Features

*   **100% Solvable Boards:** Instead of pure random shuffling (which makes 50% of board states mathematically impossible to solve), this project shuffles by making 150 simulated legal moves backward from a solved state.
*   **Zero Dependencies:** Runs on standard Python library modules (`tkinter` and `random`). No external installations required.
*   **Move Counter:** Tracks the total number of moves taken to complete the puzzle.
*   **Intuitive Visual Controls:** The empty tile is automatically disabled and colored gray, highlighting the adjacent playable tiles.

---

## How to Play

1. Run the Python script to open the game window.
2. Click any tile directly adjacent (up, down, left, or right) to the gray empty tile to slide it into that space.
3. Arrange the tiles in order from 1 to 15, starting from the top-left corner.
4. Win the game by placing all numbers in order and pushing the empty slot to the bottom-right corner.

---

## Installation & Running

### Prerequisites
Make sure you have Python installed on your system. Tkinter comes pre-installed with most standard Python installations.
