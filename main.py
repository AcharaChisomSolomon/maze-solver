from src.window import Window
# from src.point import Point
# from src.line import Line
from src.cell import Cell

def main():
    # Create a Window instance
    window = Window(800, 600)

    # Create a Cell instance
    cell = Cell(window)

    # Draw the Cell
    cell.draw(50, 50, 200, 200)

    # Keep window open until closed
    window.wait_for_close()

main()