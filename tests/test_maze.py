import unittest
from unittest.mock import MagicMock
from src.maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        # Create a mock window for testing
        self.mock_win = MagicMock()
        
        # Create a small maze for testing (2x2)
        self.maze = Maze(0, 0, 2, 2, 10, 10, self.mock_win)
        
    def test_reset_cells_visited(self):
        # First, mark all cells as visited
        for i in range(2):
            for j in range(2):
                self.maze._cells[i][j].visited = True
                
        # Verify all cells are marked as visited
        for i in range(2):
            for j in range(2):
                self.assertTrue(self.maze._cells[i][j].visited)
                
        # Call the reset method
        self.maze._reset_cells_visited()
        
        # Verify all cells are now marked as not visited
        for i in range(2):
            for j in range(2):
                self.assertFalse(self.maze._cells[i][j].visited)
                
    def test_generate_maze_resets_visited(self):
        # Generate the maze
        self.maze.generate_maze()
        
        # Verify all cells are marked as not visited after maze generation
        for i in range(2):
            for j in range(2):
                self.assertFalse(self.maze._cells[i][j].visited)

if __name__ == '__main__':
    unittest.main() 