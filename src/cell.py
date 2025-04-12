from .point import Point
from .line import Line

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 0
        self._x2 = 0
        self._y1 = 0
        self._y2 = 0
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        # Left wall: black if exists, #d9d9d9 if not
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, "black" if self.has_left_wall else "#d9d9d9")
        
        # Right wall: black if exists, #d9d9d9 if not
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_right_wall else "#d9d9d9")
        
        # Top wall: black if exists, #d9d9d9 if not
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, "black" if self.has_top_wall else "#d9d9d9")
        
        # Bottom wall: black if exists, #d9d9d9 if not
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_bottom_wall else "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        # Calculate center of current cell
        self_center_x = (self._x1 + self._x2) / 2
        self_center_y = (self._y1 + self._y2) / 2

        # Calculate center of target cell
        to_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_center_y = (to_cell._y1 + to_cell._y2) / 2

        # Create line from self center to target center
        line = Line(Point(self_center_x, self_center_y),
                    Point(to_center_x, to_center_y))

        # Draw line: red for move, gray for undo
        color = "gray" if undo else "red"
        self._win.draw_line(line, color)