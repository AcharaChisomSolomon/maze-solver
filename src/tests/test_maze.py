import unittest
from unittest.mock import MagicMock
from src.maze import Maze, Cell

class TestMaze(unittest.TestCase):
    def test_maze_initialization(self):
        """Test that a maze can be initialized with the correct dimensions."""
        win = MagicMock()
        maze = Maze(10, 20, 2, 3, 50, 50, win)
        
        # Verify the maze has the correct dimensions
        self.assertEqual(len(maze._cells), 3)  # 3 columns
        self.assertEqual(len(maze._cells[0]), 2)  # 2 rows
        
        # Verify all cells are properly initialized
        for col in maze._cells:
            for cell in col:
                self.assertIsInstance(cell, Cell)

    def test_maze_has_entrance_and_exit(self):
        """Test that the maze has an entrance at the top-left and an exit at the bottom-right."""
        win = MagicMock()
        maze = Maze(0, 0, 3, 3, 10, 10, win)
        
        # Test that the entrance cell (top-left) has no top wall
        self.assertFalse(maze._cells[0][0].has_top_wall)
        
        # Test that the exit cell (bottom-right) has no bottom wall
        self.assertFalse(maze._cells[2][2].has_bottom_wall)

    def test_maze_can_be_drawn(self):
        """Test that the maze can be drawn on the window."""
        win = MagicMock()
        maze = Maze(10, 20, 2, 3, 50, 50, win)
        
        # Verify that cells are drawn
        for col in maze._cells:
            for cell in col:
                # We don't care about the exact coordinates, just that draw was called
                self.assertTrue(hasattr(cell, '_x1'))
                self.assertTrue(hasattr(cell, '_y1'))
                self.assertTrue(hasattr(cell, '_x2'))
                self.assertTrue(hasattr(cell, '_y2'))

    def test_maze_can_be_animated(self):
        """Test that the maze can be animated."""
        win = MagicMock()
        maze = Maze(10, 20, 2, 3, 50, 50, win)
        
        # Call animate and verify the window was redrawn
        maze._animate()
        win.redraw.assert_called()

if __name__ == "__main__":
    unittest.main()