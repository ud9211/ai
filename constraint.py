def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    
    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = False
    
    return False

def n_queens(n):
    board = [[False] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")
n_queens(8)
