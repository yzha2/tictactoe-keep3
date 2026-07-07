# TicTacToe: Keep Three

A variation of Tic-Tac-Toe built with Python and pygame.

Instead of accumulating pieces throughout the game, each player may only keep **three pieces** on the board at any time. Once a player places a fourth piece, their oldest piece disappears. This simple rule creates a dynamic game that continues beyond the usual nine moves and requires players to constantly adapt their strategy.

## Features

- Classic two-player Tic-Tac-Toe gameplay with "Keep Three" game mechanic
- Click inside an empty grid to place a piece
- Before placing the fourth piece, the earliest piece changes to a lighter color as indication

## Controls

| Action | Input |
|--------|-------|
| Place a piece | Left Mouse Click |
| Restart the game | R |

## Installation

Clone the repository:

```bash
git clone https://github.com/yzha2/tictactoe-keep3.git
cd tictactoe-keep3
```

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

Install the required package:

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Future Ideas

Some possible improvements:

- Better graphics and UI
- AI opponent

---

Built as a personal project while learning **pygame**.
