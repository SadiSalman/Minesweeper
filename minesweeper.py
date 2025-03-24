import random

def create_board(size, mines):
    board = [[" " for _ in range(size)] for _ in range(size)]
    mine_positions = set()

    while len(mine_positions) < mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        mine_positions.add((row, col))

    for row, col in mine_positions:
        board[row][col] = "M"

    return board, mine_positions

def print_board(board, revealed):
    size = len(board)
    print("   " + " ".join(str(i) for i in range(size)))
    for i in range(size):
        row = []
        for j in range(size):
            if revealed[i][j]:
                row.append(board[i][j])
            else:
                row.append("*")
        print(f"{i:2} {' '.join(row)}")

def get_neighbors(row, col, size):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_row, new_col = row + i, col + j
            if 0 <= new_row < size and 0 <= new_col < size:
                neighbors.append((new_row, new_col))
    return neighbors

def calculate_numbers(board, mine_positions):
    size = len(board)
    for row, col in mine_positions:
        for neighbor in get_neighbors(row, col, size):
            r, c = neighbor
            if board[r][c] != "M":
                if board[r][c] == " ":
                    board[r][c] = "1"
                else:
                    board[r][c] = str(int(board[r][c]) + 1)

def reveal(board, revealed, row, col):
    if revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == " ":
        for neighbor in get_neighbors(row, col, len(board)):
            reveal(board, revealed, neighbor[0], neighbor[1])

def play_minesweeper(size, mines):
    board, mine_positions = create_board(size, mines)
    calculate_numbers(board, mine_positions)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    
    while True:
        print_board(board, revealed)
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if (row, col) in mine_positions:
                print("Boom! You hit a mine. Game over!")
                break
            reveal(board, revealed, row, col)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        if all(revealed[r][c] or (r, c) in mine_positions for r in range(size) for c in range(size)):
            print("Congratulations! You cleared the board!")
            break

# Play the game
board_size = 5  # Set grid size
num_mines = 5   # Set number of mines
play_minesweeper(board_size, num_mines)
