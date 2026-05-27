from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    # The Maze constructor already calls create_cells, break_walls, etc.
    maze = Maze(10, 10, 12, 10, 50, 50, win)
    
    # Solve it
    maze.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()