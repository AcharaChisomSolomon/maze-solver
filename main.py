from src.window import Window
# from src.point import Point
# from src.line import Line
from src.cell import Cell

def main():
    # Create a Window instance
    window = Window(800, 600)

    # Create two Cell instances
    cell1 = Cell(window)
    cell2 = Cell(window)

    # Set walls to False before drawing cell1
    cell1.has_right_wall = False
    cell1.draw(50, 50, 100, 100)  # Left cell: 50x50 at (50,50)

    # Set walls to False before drawing cell2
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw(100, 50, 150, 100) # Right cell: 50x50 at (100,50)

    # Draw a forward move (red)
    cell1.draw_move(cell2, undo=False)

    # Create another cell for undo test
    cell3 = Cell(window)

    # Set walls to False before drawing cell3
    cell3.has_left_wall = False
    cell3.draw(150, 50, 200, 100) # Further right: 50x50 at (150,50)

    # Draw an undo move (gray)
    cell2.draw_move(cell3, undo=True)

    # Keep window open until closed
    window.wait_for_close()

main()