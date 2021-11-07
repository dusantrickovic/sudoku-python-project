board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(x):
    for i in range(len(x)):
        if i % 3 == 0 and i != 0:
            print("----------------------------------")

        for j in range(len(x)):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(x[i][j])
            else:
                print(str(x[i][j]) + " ", end=" ")


def find_empty(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                # Returns the exact position of the column that is 0 in the form of (row, col) tuple
                return (i, j)
    return None


def valid(board, number, position):
    # Checking the row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Checking the column
    for j in range(len(board)):
        if board[j][position[1]] == number and position[0] != j:
            return False

    # Checking the sudoku box
    box_x = position[1] // 3
    box_y = position[0] // 3

    # Looping through the elements of the box
    for i in range(box_y * 3, (box_y * 3) + 3):
        for j in range(box_x * 3, (box_x * 3) + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def solve(board):
    find = find_empty(board)

    if not find:
        return True
    else:
        row, col = find

    # Recursively loops through all of the solutions; if correct - return True; if false - backtrack to the last value, reset it and return False
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
