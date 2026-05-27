from point import Point
from line import Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self._win is None:
            return

        bg_color = "#d9d9d9"
        
        # Left wall
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, "black" if self.has_left_wall else bg_color)
        
        # Top wall
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, "black" if self.has_top_wall else bg_color)
        
        # Right wall
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_right_wall else bg_color)
        
        # Bottom wall
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_bottom_wall else bg_color)

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        fill_color = "gray" if undo else "red"

        # Calculate centers
        half_x1 = (self._x1 + self._x2) / 2
        half_y1 = (self._y1 + self._y2) / 2

        half_x2 = (to_cell._x1 + to_cell._x2) / 2
        half_y2 = (to_cell._y1 + to_cell._y2) / 2

        # Draw path from center to center
        self._win.draw_line(
            Line(Point(half_x1, half_y1), Point(half_x2, half_y2)), 
            fill_color
        )

    def draw_right_wall(self, has_wall):
        self.has_right_wall = has_wall
        if self._win is None:
            return
        color = "black" if self.has_right_wall else "white"
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), color)

    def draw_left_wall(self, has_wall):
        self.has_left_wall = has_wall
        if self._win is None:
            return
        color = "black" if self.has_left_wall else "white"
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), color)

    def draw_top_wall(self, has_wall):
        self.has_top_wall = has_wall
        if self._win is None:
            return
        color = "black" if self.has_top_wall else "white"
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), color)

    def draw_bottom_wall(self, has_wall):
        self.has_bottom_wall = has_wall
        if self._win is None:
            return
        color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), color)