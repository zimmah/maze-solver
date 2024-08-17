from graphics import Window
from maze import Maze

def main():
    window = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 50, 50, window)
    for i in len(maze._cells):
        for j in len(maze[i]):
            maze._draw_cell[i][j]
    window.wait_for_close()
    
    
main()git 