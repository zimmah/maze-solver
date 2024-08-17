from graphics import Line, Point

class Cell:
    def __init__(self, _x1, _x2, _y1, _y2, _win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1 # left
        self._x2 = _x2 # right
        self._y1 = _y1 # top
        self._y2 = _y2 # bottom
        self._win = _win
    
    def draw(self):
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right))
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right))
        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left))
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right))

    def draw_move(self, to_cell, undo=False):
        draw_color = "red" if undo else "blue"
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        target_center_x = (to_cell._x1 + to_cell._x2) / 2
        target_center_y = (to_cell._y1 + to_cell._y2) / 2
        self._win.draw_line(Line(Point(center_x, center_y), Point(target_center_x, target_center_y)), draw_color)
        