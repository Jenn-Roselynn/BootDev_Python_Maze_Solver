from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    # Create a 10x12 maze starting at (10, 10)
    # The grid will be 12 rows tall and 10 columns wide
    maze = Maze(10, 10, 12, 10, 50, 50, win)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()