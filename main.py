from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(50, 100, 50, 100, win)
    cell1.has_right_wall = False
    cell2 = Cell(100, 150, 50, 100, win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell3 = Cell(100, 150, 100, 150, win)
    cell3.has_top_wall = False
    cell3.has_right_wall = False
    cell4 = Cell(150, 200, 100, 150, win)
    cell4.has_left_wall = False
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    cell3.draw_move(cell4, True)
    win.wait_for_close()
    
main()