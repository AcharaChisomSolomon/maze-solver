import unittest
from unittest.mock import MagicMock
from .maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        # Create a mock window object
        self.mock_win = MagicMock()
        # Create a maze instance with 3x3 grid
        self.maze = Maze(0, 0, 3, 3, 10, 10, self.mock_win)

    def test_break_entrance_and_exit(self):
        # Test that the entrance cell (0,0) has no top wall
        self.assertFalse(self.maze._cells[0][0].has_top_wall)
        
        # Test that the exit cell (2,2) has no bottom wall
        self.assertFalse(self.maze._cells[2][2].has_bottom_wall)
        
        # Test that other cells still have their walls
        self.assertTrue(self.maze._cells[0][0].has_bottom_wall)  # Entrance cell should still have bottom wall
        self.assertTrue(self.maze._cells[2][2].has_top_wall)     # Exit cell should still have top wall
        
        # Test that the cells were redrawn
        self.assertEqual(self.mock_win.redraw.call_count, 2)  # Called once for each cell redraw

if __name__ == '__main__':
    unittest.main() 