export function solveSudoku(board) {
  if (!board) return null;

  const findEmpty = (board) => {
    for (let i = 0; i < 9; i++) {
      for (let j = 0; j < 9; j++) {
        if (board[i][j] === 0) return [i, j];
      }
    }
    return null;
  };

  const isValid = (board, num, pos) => {
    // Check row
    for (let j = 0; j < 9; j++) {
      if (board[pos[0]][j] === num && pos[1] !== j) return false;
    }

    // Check column
    for (let i = 0; i < 9; i++) {
      if (board[i][pos[1]] === num && pos[0] !== i) return false;
    }

    // Check box
    const boxX = Math.floor(pos[1] / 3) * 3;
    const boxY = Math.floor(pos[0] / 3) * 3;

    for (let i = boxY; i < boxY + 3; i++) {
      for (let j = boxX; j < boxX + 3; j++) {
        if (board[i][j] === num && (i !== pos[0] || j !== pos[1])) return false;
      }
    }

    return true;
  };

  const solve = (board) => {
    const empty = findEmpty(board);
    if (!empty) return true;

    const [row, col] = empty;

    for (let num = 1; num <= 9; num++) {
      if (isValid(board, num, [row, col])) {
        board[row][col] = num;

        if (solve(board)) return true;

        board[row][col] = 0;
      }
    }

    return false;
  };

  const boardCopy = board.map(row => [...row]);
  return solve(boardCopy) ? boardCopy : null;
}