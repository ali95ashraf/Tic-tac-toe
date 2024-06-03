from tkinter import *
import random

window = Tk()
window.title("Tic-tac-toe")

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(position):
    global currentPlayer, gameRunning
    if board[position] == "-" and gameRunning:
        board[position] = currentPlayer
        button_list[position].config(text=currentPlayer)
        switchPlayer()
        if checkWin() or checkTie():
            gameRunning = False
        if currentPlayer == "O" and gameRunning:
            computer()

def checkHorizontal():
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkVertical():
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkDiagonal():
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkWin():
    global winner
    if checkDiagonal() or checkHorizontal() or checkVertical():
        winner_label.config(text=f"The winner is {winner}!")
        return True
    return False

def checkTie():
    global gameRunning
    if "-" not in board:
        winner_label.config(text="It's a tie!")
        return True
    return False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    label.config(text=currentPlayer + "'s turn")

def restart_game():
    global board, currentPlayer, winner, gameRunning
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currentPlayer = "X"
    winner = None
    gameRunning = True
    for btn in button_list:
        btn.config(text="-")
    label.config(text=currentPlayer + "'s turn")
    winner_label.config(text="")

def computer():
    global currentPlayer
    if currentPlayer == "O":
        position = random.randint(0, 8)
        while board[position] != "-":
            position = random.randint(0, 8)
        board[position] = currentPlayer
        button_list[position].config(text=currentPlayer)
        switchPlayer()

button_list = []

for i in range(9):
    btn = Button(window, text="-", font=('consolas', 80), command=lambda idx=i: playerInput(idx))
    btn.grid(row=i // 3, column=i % 3, sticky="nsew")
    button_list.append(btn)

label = Label(window, text=currentPlayer + "'s turn", font=('consolas', 40))
label.grid(row=3, columnspan=3)

reset_button = Button(window, text="Restart", font=('consolas', 40), command=restart_game)
reset_button.grid(row=4, columnspan=3)

winner_label = Label(window, text="", font=('consolas', 40))
winner_label.grid(row=5, columnspan=3)

window.mainloop()
