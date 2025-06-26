import tkinter as tk
from tkinter import messagebox

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def button_click(row, col):
    global current_player, board

    if board[row][col] == ' ':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        
        if check_winner(board, current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif board_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def reset_game():
    global current_player, board
    current_player = 'X'
    board = initialize_board()
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='')

root = tk.Tk()
root.title("Tic-Tac-Toe")

board = initialize_board()
current_player = 'X'

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                                      command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col)

reset_button = tk.Button(root, text="Reset Game", font=('normal', 20), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)
root.mainloop()