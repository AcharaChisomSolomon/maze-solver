from src.window import Window
from src.point import Point
from src.line import Line

def main():
    # Create a Window instance
    window = Window(800, 600)

    # Create Points for Lines
    p1 = Point(50, 50)
    p2 = Point(200, 50)
    p3 = Point(50, 200)
    p4 = Point(200, 200)

    # Create Lines
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)
    line3 = Line(p1, p3)

    # Draw Lines
    window.draw_line(line1, "blue")
    window.draw_line(line2, "red")
    window.draw_line(line3, "green")

    # Keep window open until closed
    window.wait_for_close()

main()