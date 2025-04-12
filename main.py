from src.window import Window
# from src.point import Point
# from src.line import Line
# from src.cell import Cell
from src.maze import Maze

def main():
    # Create a Window instance
    window = Window(800, 600)

    # Create a Maze instance
    maze = Maze(
        x1=50,           # Start 50 pixels from left
        y1=50,           # Start 50 pixels from top
        num_rows=5,      # 5 rows
        num_cols=5,      # 5 columns
        cell_size_x=50,  # 50 pixels wide
        cell_size_y=50,  # 50 pixels tall
        win=window
    )

    # Keep window open until closed
    window.wait_for_close()

main()