from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window

    def _create_cells(self):
        self._cells = [[Cell(self.x1 + i * self.cell_size_x, self.x1 + (i+1) * self.cell_size_x, self.y1 + j * self.cell_size_y, self.xy + (j+1) * self.cell_size_y, self.window) for j in range(self.num_cols)] for i in range(self.num_rows)]

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)