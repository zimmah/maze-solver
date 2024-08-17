from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        if seed is not None:
            self.seed = random.seed(seed)

    def _create_cells(self):
        self._cells = [[Cell(self.x1 + i * self.cell_size_x, self.x1 + (i+1) * self.cell_size_x, self.y1 + j * self.cell_size_y, self.y1 + (j+1) * self.cell_size_y, self.window) for j in range(self.num_cols)] for i in range(self.num_rows)]

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate_fast()

    def _animate_fast(self):
        self.window.redraw()
        time.sleep(0.01)

    def _animate_slow(self):
        self.window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        if not self._cells:
            raise Exception("Create a maze first!")
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        entrance_cell.draw()
        exit_cell.draw()
        self._animate_fast()
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            can_move_left = i > 0 and self._cells[i-1][j].visited == False
            can_move_right = i+1 < len(self._cells) and self._cells[i+1][j].visited == False
            can_move_up = j > 0 and self._cells[i][j-1].visited == False
            can_move_down = j+1 < len(self._cells[i]) and self._cells[i][j+1].visited == False
            if can_move_left:
                to_visit.append((i-1, j, "left"))
            if can_move_right:
                to_visit.append((i+1, j, "right"))
            if can_move_up:
                to_visit.append((i, j-1, "up"))
            if can_move_down:
                to_visit.append((i, j+1, "down"))
            if not can_move_down and not can_move_left and not can_move_right and not can_move_up:
                self._draw_cell(i, j)
                return
            target_i, target_j, direction = to_visit[random.randrange(len(to_visit))]
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[target_i][target_j].has_right_wall = False
            if direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[target_i][target_j].has_left_wall = False
            if direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[target_i][target_j].has_bottom_wall = False
            if direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[target_i][target_j].has_top_wall = False
            self._draw_cell(i, j)
            self._draw_cell(target_i, target_j)
            self._break_walls_r(target_i, target_j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        # return True if it's and end cell or if it leads to an end cell
        self._animate_slow()
        cells = self._cells
        cur= cells[i][j]
        cur.visited = True
        if i == len(cells) - 1 and j == len(cells[i]) - 1:
            return True
        can_move_left = i > 0 and cur.has_left_wall == False and cells[i-1][j].visited == False
        can_move_right = i+1 < len(cells) and cur.has_right_wall == False and cells[i+1][j].visited == False
        can_move_up = j > 0 and cur.has_top_wall == False and cells[i][j-1].visited == False
        can_move_down = j+1 < len(cells[i]) and cur.has_bottom_wall == False and cells[i][j+1].visited == False
        if can_move_left:
            cur.draw_move(cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            cur.draw_move(cells[i-1][j], True)
        if can_move_right:
            cur.draw_move(cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            cur.draw_move(cells[i+1][j], True)
        if can_move_up:
            cur.draw_move(cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            cur.draw_move(cells[i][j-1], True)
        if can_move_down:
            cur.draw_move(cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            cur.draw_move(cells[i][j+1], True)
        return False

