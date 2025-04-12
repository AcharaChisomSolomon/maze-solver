import unittest
from unittest.mock import MagicMock
from src.cell import Cell

class TestCell(unittest.TestCase):
    def test_init(self):
        win = MagicMock()
        cell = Cell(win)
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._x2, 0)
        self.assertEqual(cell._y1, 0)
        self.assertEqual(cell._y2, 0)
        self.assertEqual(cell._win, win)

    def test_draw(self):
        win = MagicMock()
        cell = Cell(win)
        cell.draw(10, 20, 30, 40)
        
        # Verify coordinates updated
        self.assertEqual(cell._x1, 10)
        self.assertEqual(cell._y1, 20)
        self.assertEqual(cell._x2, 30)
        self.assertEqual(cell._y2, 40)
        
        # Verify draw_line calls (4 walls)
        self.assertEqual(win.draw_line.call_count, 4)

    def test_draw_no_walls(self):
        win = MagicMock()
        cell = Cell(win)
        cell.has_left_wall = False
        cell.has_right_wall = False
        cell.has_top_wall = False
        cell.has_bottom_wall = False
        cell.draw(10, 20, 30, 40)
        
        # Verify no lines drawn
        win.draw_line.assert_not_called()

if __name__ == "__main__":
    unittest.main()