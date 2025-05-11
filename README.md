# 🧩 8-Puzzle Solver

This project implements a command-line 8-puzzle solver using two algorithms:

- **Breadth-First Search (BFS)**
- **A* Search (with Manhattan distance and linear conflict heuristic)**

---

## 📁 Files Overview

- `Tiles.py` — Entry point of the program. Parses input, runs both solvers, and prints results.
- `SolutionParts.py` — Defines the `SolutionParts` class representing the puzzle state and movement logic.
- `BFSolver.py` — Implements BFS for solving the puzzle.
- `ASolver.py` — Implements A* Search with a custom heuristic (Manhattan + linear conflict).

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.

2. Run the program with 9 integers representing the puzzle state in **row-major** order (0 represents the empty tile):

```bash
python Tiles.py 1 4 0 5 8 2 3 6 7
```

> Example Input:
```
1 4 0
5 8 2
3 6 7
```

---

## ✅ Output

The program will output:

- The initial state
- The solution path for **BFS** and **A\***
- Number of moves required
- Number of nodes expanded (A* only)

---

## 🧠 Heuristic Used in A*

A* uses the following cost function:

```
f(n) = g(n) + h(n)
```

Where:
- `g(n)` is the cost from the start node to current node (number of moves).
- `h(n)` is the sum of:
  - **Manhattan distance**
  - **2 × number of linear conflicts** (rows and columns)

---

## 🧩 Target State

The goal configuration is:

```
0 1 2
3 4 5
6 7 8
```

---

## 🔧 Dependencies

No external dependencies—only Python standard libraries are used.

