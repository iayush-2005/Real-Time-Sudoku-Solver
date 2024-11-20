class SudokuSolver:
    @staticmethod
    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    @staticmethod
    def is_valid(board, num, pos):
        # Check row
        for j in range(9):
            if board[pos[0]][j] == num and pos[1] != j:
                return False

        # Check column
        for i in range(9):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        return True

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0
        return False