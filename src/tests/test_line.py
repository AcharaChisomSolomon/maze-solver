import unittest
from unittest.mock import MagicMock
from src.line import Line
from src.point import Point

class TestLine(unittest.TestCase):
    def test_line_creation(self):
        p1 = Point(10, 20)
        p2 = Point(30, 40)
        line = Line(p1, p2)
        self.assertEqual(line.point1, p1)
        self.assertEqual(line.point2, p2)

    def test_draw(self):
        p1 = Point(10, 20)
        p2 = Point(30, 40)
        line = Line(p1, p2)
        
        # Mock the canvas
        mock_canvas = MagicMock()
        line.draw(mock_canvas, "red")
        
        # Verify create_line was called with correct arguments
        mock_canvas.create_line.assert_called_once_with(
            10, 20, 30, 40, fill="red", width=2
        )

if __name__ == "__main__":
    unittest.main()