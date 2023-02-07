import random
from tkinter import *
from tkinter.font import *


def turn(row, column):
    global player
    fields[row][column].configure(text=player, state="disabled")

    if check_winner():
        return
    elif check_winner() is None:
        turn_label.configure(text="It's a tie!")
        return

    if player == players[0]:
        player = players[1]
    elif player == players[1]:
        player = players[0]

    turn_label.configure(text=f"{player} turn")


def check_winner():
    for row in range(3):
        if fields[row][0]["text"] == fields[row][1]["text"] == fields[row][2]["text"] != "":
            turn_label.configure(text=f"{player} won!")
            return True
        for column in range(3):
            if fields[0][column]["text"] == fields[1][column]["text"] == fields[2][column]["text"] != "":
                turn_label.configure(text=f"{player} won!")
                return True

        if (fields[0][0]["text"] == fields[1][1]["text"] == fields[2][2]["text"] != "") or (
                fields[0][2]["text"] == fields[1][1]["text"] == fields[2][0]["text"] != ""):
            turn_label.configure(text=f"{player} won!")
            return True

    free_spaces = 9
    for i in fields:
        for j in i:
            if j["text"] != "":
                free_spaces -= 1
    if free_spaces <= 0:
        return None

    return False


window = Tk()
window.title("TicTacToe by Jackstar")

font = Font(family="Consolas", size=20)

for i in range(0, 3):
    window.grid_columnconfigure(i, weight=1)
for i in range(0, 4):
    window.grid_rowconfigure(i, weight=1)

fields: Button = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
players = ["O", "X"]
player = random.choice(players)

turn_label = Label(window, text=f"{player} turn", font=font, anchor="center", width=30)
turn_label.grid(column=0, row=0, columnspan=3, rowspan=1, sticky="NSEW")

for row_idx in enumerate(fields):
    for col_idx in enumerate(row_idx[1]):
        fields[row_idx[0]][col_idx[0]] = Button(window, font=font, width=10, height=4,
                                                anchor="center",
                                                command=lambda row=row_idx[0], column=col_idx[0]: turn(row, column))
        fields[row_idx[0]][col_idx[0]].grid(column=col_idx[0], row=row_idx[0] + 1, sticky="NSEW")

window.mainloop()
