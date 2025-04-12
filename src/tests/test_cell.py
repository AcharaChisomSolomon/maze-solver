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

    def test_draw_move(self):
        win = MagicMock()
        cell1 = Cell(win)
        cell2 = Cell(win)
        
        # Set coordinates
        cell1.draw(10, 10, 20, 20)  # 10x10 cell at (10,10)
        cell2.draw(20, 10, 30, 20)  # Adjacent cell to the right
        
        cell1.draw_move(cell2, undo=False)
        
        # Verify draw_line called with correct line (centers: 15,15 to 25,15)
        args = win.draw_line.call_args[0]
        line = args[0]
        color = args[1]
        self.assertEqual(color, "red")
        self.assertEqual(line.point1.x, 15)  # Center of cell1
        self.assertEqual(line.point1.y, 15)
        self.assertEqual(line.point2.x, 25)  # Center of cell2
        self.assertEqual(line.point2.y, 15)

    def test_draw_move_undo(self):
        win = MagicMock()
        cell1 = Cell(win)
        cell2 = Cell(win)
        
        cell1.draw(10, 10, 20, 20)
        cell2.draw(10, 20, 20, 30)  # Below cell1
        
        cell1.draw_move(cell2, undo=True)
        
        args = win.draw_line.call_args[0]
        color = args[1]
        self.assertEqual(color, "gray")

if __name__ == "__main__":
    unittest.main()