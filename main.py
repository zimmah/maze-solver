from graphics import Window
from maze import Maze

def main():
    window = Window(800, 600)
    maze = Maze(150, 50, 10, 10, 50, 50, window, 1337)
    maze._create_cells()
    for i in range(len(maze._cells)):
        for j in range(len(maze._cells[i])):
            maze._draw_cell(i, j)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()
    window.wait_for_close()
    
main()