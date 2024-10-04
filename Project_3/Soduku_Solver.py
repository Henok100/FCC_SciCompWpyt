# Sudoku Solver
# This script defines a Sudoku solver using backtracking. It uses a `Board` class to represent the Sudoku board
# and provides methods to check if a number can be placed in a cell according to Sudoku rules (no duplicates in rows, 
# columns, or 3x3 subgrids). The solver function attempts to fill in the empty cells (represented as 0) until the puzzle is solved.

class Board:
    # The Board class is used to represent the Sudoku board and check the validity of numbers placed on the board.

    def __init__(self, board):
        # Initialize the board with the given 9x9 grid.
        self.board = board

    def __str__(self):
        # This method returns a string representation of the board for printing.
        board_str = ''
        # Loop through each row of the board.
        for row in self.board:
            # Replace zeros (empty cells) with '*' for readability.
            row_str = [str(i) if i else '*' for i in row]
            # Join the numbers in the row with spaces and add it to the board string.
            board_str += ' '.join(row_str)
            board_str += '\n'  # Add a newline after each row.
        return board_str

    def find_empty_cell(self):
        # This method finds the first empty cell (represented by 0) in the board.
        for row, contents in enumerate(self.board):
            # Try to find the first zero in the row.
            try:
                col = contents.index(0)  # Find the column index where 0 appears.
                return row, col  # Return the row and column of the empty cell.
            except ValueError:
                # If there is no 0 in the row, continue to the next row.
                pass
        return None  # If no empty cell is found, return None.

    def valid_in_row(self, row, num):
        # Check if a number `num` is valid in the specified row.
        return num not in self.board[row]  # Return True if `num` is not already in the row.

    def valid_in_col(self, col, num):
        # Check if a number `num` is valid in the specified column.
        return all(self.board[row][col] != num for row in range(9))  # Return True if `num` is not in the column.

    def valid_in_square(self, row, col, num):
        # Check if a number `num` is valid in the 3x3 subgrid where the specified cell is located.
        row_start = (row // 3) * 3  # Get the starting row of the 3x3 subgrid.
        col_start = (col // 3) * 3  # Get the starting column of the 3x3 subgrid.
        # Check all cells in the 3x3 subgrid.
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False  # Return False if `num` is found in the subgrid.
        return True  # Return True if `num` is not in the subgrid.

    def is_valid(self, empty, num):
        # This method checks if placing `num` in the empty cell is valid (according to Sudoku rules).
        row, col = empty  # Get the row and column of the empty cell.
        valid_in_row = self.valid_in_row(row, num)  # Check if `num` is valid in the row.
        valid_in_col = self.valid_in_col(col, num)  # Check if `num` is valid in the column.
        valid_in_square = self.valid_in_square(row, col, num)  # Check if `num` is valid in the 3x3 subgrid.
        # Return True if the number is valid in the row, column, and subgrid.
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # This is the recursive backtracking method that tries to solve the Sudoku puzzle.
        # It finds an empty cell and attempts to place a valid number in it.

        if (next_empty := self.find_empty_cell()) is None:
            # If no empty cell is found, the puzzle is solved, so return True.
            return True

        # Try placing numbers 1 through 9 in the empty cell.
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):  # Check if the current guess is valid.
                row, col = next_empty  # Get the row and column of the empty cell.
                self.board[row][col] = guess  # Place the guess in the empty cell.

                if self.solver():  # Recursively attempt to solve the rest of the puzzle.
                    return True  # If successful, return True.

                self.board[row][col] = 0  # If the guess doesn't lead to a solution, reset the cell to 0.

        return False  # If no valid number can be placed in the empty cell, return False.

def solve_sudoku(board):
    # This function takes a 9x9 Sudoku board, attempts to solve it using the `Board` class,
    # and prints the initial and solved states of the board.
    gameboard = Board(board)  # Create a Board object from the input board.
    print(f'Puzzle to solve:\n{gameboard}')  # Print the initial unsolved puzzle.
    
    if gameboard.solver():  # Try to solve the puzzle.
        print(f'Solved puzzle:\n{gameboard}')  # If successful, print the solved puzzle.
    else:
        print('The provided puzzle is unsolvable.')  # If unsuccessful, print an error message.
    
    return gameboard  # Return the final gameboard (solved or unsolved).

# Example Sudoku puzzle to solve.
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Attempt to solve the Sudoku puzzle.
solve_sudoku(puzzle)