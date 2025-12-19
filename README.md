Here is a clear and professional **README.md** you can use for this code:

---

# 8-Puzzle Solver using A* Search Algorithm

## 📌 Overview

This project implements a solver for the classic **8-puzzle problem** using the **A*** search algorithm in Python. The goal is to transform an initial puzzle configuration into the goal state by sliding tiles, using an informed search strategy with the **Manhattan distance heuristic**.

The puzzle consists of a 3×3 grid with tiles numbered 1–8 and one blank space (represented as `0`).

---

## 🧠 Algorithm Used

* **A*** Search Algorithm
* **Heuristic**: Manhattan Distance
  (Sum of distances of each tile from its goal position)

The algorithm prioritizes nodes with the lowest:

```
f(n) = g(n) + h(n)
```

Where:

* `g(n)` = cost to reach the current node
* `h(n)` = heuristic estimate to reach the goal

---

## 🗂️ Code Structure

### `PuzzleNode` Class

Represents a puzzle state in the search tree.

**Attributes:**

* `state`: Current puzzle configuration
* `parent`: Reference to the previous state
* `move`: Move taken to reach this state (`U`, `D`, `L`, `R`)
* `cost`: Path cost from the initial state
* `heuristic`: Manhattan distance to the goal

**Methods:**

* `calculate_heuristic()` – Computes the Manhattan distance
* `__lt__()` – Enables priority queue comparison

---

### `get_neighbors(node)`

Generates all valid neighboring states by moving the blank tile:

* Up (`U`)
* Down (`D`)
* Left (`L`)
* Right (`R`)

---

### `solve_8_puzzle(initial_state)`

Solves the puzzle using A* search.

**Steps:**

1. Initialize a priority queue (open list)
2. Track visited states using a closed set
3. Expand the lowest-cost node
4. Stop when the goal state is reached

Returns the solution path if found, otherwise `None`.

---

### `reconstruct_path(node)`

Reconstructs the solution path by backtracking from the goal node to the initial node.

---

## ▶️ Example Usage

```python
initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
solution_path = solve_8_puzzle(initial_state)

if solution_path:
    print("Solution found!")
    for move, state in solution_path:
        print(f"Move: {move}, State: {state}")
else:
    print("No solution exists.")
```

---

## 🎯 Goal State

```python
[1, 2, 3,
 4, 5, 6,
 7, 8, 0]
```

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required (uses built-in `heapq`)

---

## ⚠️ Notes

* This implementation does **not** check if the puzzle is solvable before attempting to solve it.
* The algorithm may consume more memory for complex puzzle configurations.

---

## 🚀 Future Improvements

* Add solvability check
* Track and optimize path cost (`g(n)`)
* Improve performance with better state pruning
* Add visualization for puzzle moves

---

## 📜 License

This project is for educational purposes and is free to use and modify.

---

If you'd like, I can also:

* Add comments to the code
* Improve performance
* Convert this into a class-based solver
* Add a GUI or visualization 😊
