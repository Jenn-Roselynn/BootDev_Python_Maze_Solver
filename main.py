from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)

    # Test drawing a line
    p1 = Point(10, 10)
    p2 = Point(790, 590)
    line = Line(p1, p2)
    win.draw_line(line, "red")

    # Test drawing a cell
    cell1 = Cell(win)
    cell1.draw(10, 10, 100, 100)

    cell2 = Cell(win)
    cell2.draw(100, 10, 190, 100)

    cell1.draw_right_wall(False)
    cell2.draw_left_wall(False)
    win.wait_for_close()

if __name__ == "__main__":
    main()