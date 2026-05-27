from window import Window
from point import Point
from line import Line
from cell import Cell
import time

def main():
    win = Window(800, 600)

    # 1. Test drawing a line
    p1 = Point(10, 10)
    p2 = Point(790, 590)
    line = Line(p1, p2)
    win.draw_line(line, "red")

    # 2. Setup the cells
    cell1 = Cell(win)
    cell1.draw(10, 10, 100, 100)

    cell2 = Cell(win)
    cell2.draw(110, 10, 200, 100)

    # 3. Draw the move path
    cell1.draw_move(cell2)        # Draw red line
    cell2.draw_move(cell1, True)  # Draw gray "undo" line

    # 4. Demonstrate wall opening and closing animation
    # We loop to toggle the walls visibly
    for _ in range(5):
        # Open the walls
        cell1.draw_right_wall(False)
        cell2.draw_left_wall(False)
        win.redraw()
        time.sleep(0.25)
        
        # Close the walls
        cell1.draw_right_wall(True)
        cell2.draw_left_wall(True)
        win.redraw()
        time.sleep(0.25)

    win.wait_for_close()

if __name__ == "__main__":
    main()