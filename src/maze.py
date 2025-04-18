import time
import random

from .cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        # Set the random seed if provided
        if seed is not None:
            random.seed(seed)
            
        self._create_cells()
        self._break_entrance_and_exit()
        self.generate_maze()  # Generate the maze after creating cells and breaking entrance/exit

    def _create_cells(self):
        # Initialize _cells as a list of lists (columns of rows)
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        
        # Draw each cell
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # Calculate top-left and bottom-right coordinates
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        # Draw the cell
        self._cells[i][j].draw(x1, y1, x2, y2)
        
        # Animate the drawing
        self._animate()

    def _animate(self, default=0.05):
        self._win.redraw()
        time.sleep(default)

    def _break_entrance_and_exit(self):
        # Entrance: top-left cell (0, 0), remove top wall
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        # Exit: bottom-right cell (num_cols-1, num_rows-1), remove bottom wall
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
        
    def _break_walls_r(self, i, j):
        """
        Recursively break walls using depth-first traversal.
        
        Args:
            i: Column index of the current cell
            j: Row index of the current cell
        """
        # Mark the current cell as visited
        self._cells[i][j].visited = True
        
        while True:
            # Create a list to hold possible directions to move
            possible_directions = []
            
            # Check all four directions (up, right, down, left)
            # For each direction, check if the adjacent cell exists and hasn't been visited
            
            # Up (j-1)
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1, "up"))
                
            # Right (i+1)
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j, "right"))
                
            # Down (j+1)
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1, "down"))
                
            # Left (i-1)
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1, j, "left"))
            
            # If there are no possible directions, draw the current cell and return
            if not possible_directions:
                self._draw_cell(i, j)
                return
            
            # Pick a random direction
            next_i, next_j, direction = random.choice(possible_directions)
            
            # Break the walls between the current cell and the chosen cell
            if direction == "up":
                # Break the top wall of the current cell and the bottom wall of the cell above
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif direction == "right":
                # Break the right wall of the current cell and the left wall of the cell to the right
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            elif direction == "down":
                # Break the bottom wall of the current cell and the top wall of the cell below
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif direction == "left":
                # Break the left wall of the current cell and the right wall of the cell to the left
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            
            # Draw the current cell
            self._draw_cell(i, j)
            
            # Move to the chosen cell by recursively calling _break_walls_r
            self._break_walls_r(next_i, next_j)
            
    def _reset_cells_visited(self):
        """
        Reset the visited property of all cells in the maze to False.
        This allows the visited property to be reused for other algorithms,
        such as maze solving.
        """
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                
    def generate_maze(self):
        """
        Generate a maze by breaking walls using a depth-first traversal algorithm.
        This method resets all cells to unvisited and then starts the recursive process
        from the entrance cell (0, 0).
        """
        # Reset all cells to unvisited
        self._reset_cells_visited()
                
        # Start the recursive process from the entrance cell (0, 0)
        self._break_walls_r(0, 0)
        
        # Reset cells visited property after maze generation
        self._reset_cells_visited()
        
    def solve(self):
        """
        Solve the maze using a depth-first traversal algorithm.
        This method starts the recursive solving process from the entrance cell (0, 0).
        
        Returns:
            bool: True if the maze was solved, False otherwise.
        """
        # Reset all cells to unvisited
        self._reset_cells_visited()
        
        # Start the recursive solving process from the entrance cell (0, 0)
        return self._solve_r(0, 0)
        
    def _solve_r(self, i, j):
        """
        Recursively solve the maze using a depth-first traversal algorithm.
        
        Args:
            i: Column index of the current cell
            j: Row index of the current cell
            
        Returns:
            bool: True if the current cell is an end cell or leads to the end cell,
                  False if the current cell is a loser cell.
        """
        # Call the animate method to update the display
        self._animate(0.5)
        
        # Mark the current cell as visited
        self._cells[i][j].visited = True
        
        # If you are at the "end" cell (the goal) then return True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
            
        # For each direction (up, right, down, left)
        # Check if there is a cell in that direction, there is no wall blocking you, and that cell hasn't been visited
        
        # Up (j-1)
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            # Draw a move between the current cell and the cell above
            self._cells[i][j].draw_move(self._cells[i][j-1])
            
            # Call _solve_r recursively to move to that cell
            if self._solve_r(i, j-1):
                return True
                
            # Otherwise, draw an "undo" move between the current cell and the cell above
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
            
        # Right (i+1)
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            # Draw a move between the current cell and the cell to the right
            self._cells[i][j].draw_move(self._cells[i+1][j])
            
            # Call _solve_r recursively to move to that cell
            if self._solve_r(i+1, j):
                return True
                
            # Otherwise, draw an "undo" move between the current cell and the cell to the right
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
            
        # Down (j+1)
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            # Draw a move between the current cell and the cell below
            self._cells[i][j].draw_move(self._cells[i][j+1])
            
            # Call _solve_r recursively to move to that cell
            if self._solve_r(i, j+1):
                return True
                
            # Otherwise, draw an "undo" move between the current cell and the cell below
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
            
        # Left (i-1)
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            # Draw a move between the current cell and the cell to the left
            self._cells[i][j].draw_move(self._cells[i-1][j])
            
            # Call _solve_r recursively to move to that cell
            if self._solve_r(i-1, j):
                return True
                
            # Otherwise, draw an "undo" move between the current cell and the cell to the left
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
            
        # If none of the directions worked out, return False
        return False