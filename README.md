This is the perfect way to wrap up your project. A well-crafted `README.md` acts as your portfolio piece, showing potential employers or collaborators exactly what you built and how it works.

Here is a structured, professional template for your `README.md`. You can copy and paste this directly into your project's root directory.

---

# Maze Solver in Python

This project is a visual maze generator and solver application built in Python. It utilizes recursive algorithms to construct a "perfect" maze and then applies a depth-first search (DFS) algorithm to navigate from the entrance to the exit, with real-time graphical animations.

## Features

* **Perfect Maze Generation**: Uses a **recursive backtracking** algorithm to ensure there is exactly one path between any two points in the grid.
* **Intelligent Pathfinding**: Implements a **depth-first search (DFS)** solver that explores paths and utilizes backtracking to handle dead ends.
* **Graphical Visualization**: Uses `Tkinter` to render the maze, animate the carving process, and highlight the solver's path in real-time.
* **Deterministic Testing**: Includes optional seeding for the random number generator to ensure consistent maze generation during debugging.

## How it Works

The application is built using an object-oriented approach:

1. **`Maze` Class**: Orchestrates the grid construction, manages cell states, and executes the generation and solving algorithms.
2. **`Cell` Class**: Represents individual nodes in the grid, tracking their walls (`top`, `bottom`, `left`, `right`) and visited status.
3. **Recursive Backtracking**: The generation logic moves through the grid, carving walls until every reachable cell has been visited.
4. **DFS Solver**: The solving logic attempts to traverse the maze, marking paths as red and backtracking (drawing gray) when it encounters a dead end.

## Installation & Usage

1. **Clone the repository**:
```bash
git clone https://github.com/Jenn-Roselynn/BootDev_Python_Maze_Solver.git
cd BootDev_Python_Maze_Solver

```


2. **Run the application**:
```bash
python3 main.py

```


3. **Run the test suite**:
```bash
python3 tests.py

```



## Technologies Used

* **Python**
* **Tkinter** (for GUI and animation)
* **Unit Testing** (for logic validation)

## Acknowledgements

This project was completed as part of the [Boot.dev "Build a Maze Solver in Python"](https://www.boot.dev/courses/build-maze-solver-python) guided curriculum.

---


<!--`![Maze Solver Animation](assets/your-screenshot-name.png)`-->

