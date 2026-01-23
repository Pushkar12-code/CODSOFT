# Task 2: Tic Tac Toe AI (Minimax)
# CODSOFT AI Internship

import math

# Board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check winner
def check_winner(player):
    win_combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_ai):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_ai:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Game loop
print("🎮 Tic Tac Toe (You = X, AI = O)")
print("Enter positions 1-9")

while True:
    print_board()

    move = int(input("Your move (1-9): ")) - 1
    if board[move] != " ":
        print("Invalid move! Try again.")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("🎉 You win!")
        break

    if is_draw():
        print_board()
        print("🤝 It's a draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI wins!")
        break
