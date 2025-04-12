import unittest
from unittest.mock import MagicMock
from src.line import Line
from src.point import Point

class TestLine(unittest.TestCase):
    def test_line_can_be_created_with_two_points(self):
        """Test that a line can be created with two points."""
        p1 = Point(10, 20)
        p2 = Point(30, 40)
        line = Line(p1, p2)
        
        # Verify the line has the correct points
        self.assertEqual(line.point1, p1)
        self.assertEqual(line.point2, p2)

    def test_line_can_be_drawn_on_canvas(self):
        """Test that a line can be drawn on a canvas with a specified color."""
        p1 = Point(10, 20)
        p2 = Point(30, 40)
        line = Line(p1, p2)
        
        # Mock the canvas
        mock_canvas = MagicMock()
        
        # Draw the line
        line.draw(mock_canvas, "red")
        
        # Verify the canvas was asked to draw the line
        mock_canvas.create_line.assert_called_once()

if __name__ == "__main__":
    unittest.main()