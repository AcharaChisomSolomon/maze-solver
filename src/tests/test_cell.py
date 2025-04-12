import unittest
from unittest.mock import MagicMock
from src.cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.win = MagicMock()
        self.cell = Cell(self.win)

    def test_cell_has_walls_by_default(self):
        """Test that a cell has all walls by default."""
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)

    def test_cell_can_be_drawn(self):
        """Test that a cell can be drawn on the window."""
        self.cell.draw(10, 20, 30, 40)
        # Verify that draw_line was called at least once
        self.win.draw_line.assert_called()

    def test_cell_without_walls_is_drawn_differently(self):
        """Test that a cell without walls is drawn with a different style."""
        # Remove all walls
        self.cell.has_left_wall = False
        self.cell.has_right_wall = False
        self.cell.has_top_wall = False
        self.cell.has_bottom_wall = False
        
        self.cell.draw(10, 20, 30, 40)
        
        # Verify that draw_line was called for each wall
        self.assertEqual(self.win.draw_line.call_count, 4)
        
        # Verify that all lines were drawn with the "no wall" color
        for call in self.win.draw_line.call_args_list:
            args = call[0]  # Get the positional arguments
            self.assertEqual(args[1], "#d9d9d9")  # Check the color is light gray

    def test_cell_can_draw_a_move_to_another_cell(self):
        """Test that a cell can draw a move to another cell."""
        cell2 = Cell(self.win)
        
        # Set up both cells
        self.cell.draw(10, 10, 20, 20)
        cell2.draw(20, 10, 30, 20)  # Adjacent cell to the right
        
        # Draw a move from cell1 to cell2
        self.cell.draw_move(cell2, undo=False)
        
        # Verify that a line was drawn with the correct color
        args = self.win.draw_line.call_args[0]
        color = args[1]
        self.assertEqual(color, "red")

    def test_cell_can_draw_an_undo_move(self):
        """Test that a cell can draw an undo move to another cell."""
        cell2 = Cell(self.win)
        
        # Set up both cells
        self.cell.draw(10, 10, 20, 20)
        cell2.draw(10, 20, 20, 30)  # Below cell1
        
        # Draw an undo move from cell1 to cell2
        self.cell.draw_move(cell2, undo=True)
        
        # Verify that a line was drawn with the correct color
        args = self.win.draw_line.call_args[0]
        color = args[1]
        self.assertEqual(color, "gray")

if __name__ == "__main__":
    unittest.main()