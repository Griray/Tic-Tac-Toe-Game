import tkinter as tk
from tkinter import messagebox
from tkinter import *

from buttoncls import Button
from game import Game


class Gameboard:
    all_buttons = []
    gameboard_obj = None

    def __init__(self, main_window: tk.Tk, rows: int, columns: int):
        self.main_window = main_window
        self.rows = rows
        self.columns = columns
        Gameboard.gameboard_obj = self

    def create_gameboard_model(self):
        basic_button = Button(self.main_window, self.rows, self.columns)
        for row in range(self.rows):
            for column in range(self.columns):
                self.all_buttons.append(basic_button.generate_button(row, column))
        basic_button.create_new_game_button()
        return self.all_buttons

    def get_all_buttons(self):
        return self.all_buttons

    def attach_gameboard_to_window(self):
        self.create_gameboard_model()
        self.main_window.mainloop()

    def win_message(self, symbol):
        if symbol == 'X':
            messagebox.showinfo('Congratulations!', 'X won this round')
        elif symbol == 'O':
            messagebox.showinfo('Congratulations!', 'O won this round')

    def disable_all_buttons(self):
        board_model = self.get_all_buttons()
        for btn in board_model:
            btn.config(state=DISABLED)

    def check_vertical_line_combination(self, symbol):
        board_model = self.get_all_buttons()

        if board_model[0]['text'] == symbol and board_model[3]['text'] == symbol and board_model[6]['text'] == symbol:
            Game.win = True
            board_model[0].config(background='#5DA60A')
            board_model[3].config(background='#5DA60A')
            board_model[6].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

        elif board_model[1]['text'] == symbol and board_model[4]['text'] == symbol and board_model[7]['text'] == symbol:
            Game.win = True
            board_model[1].config(background='#5DA60A')
            board_model[4].config(background='#5DA60A')
            board_model[7].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

        elif board_model[2]['text'] == symbol and board_model[5]['text'] == symbol and board_model[8]['text'] == symbol:
            Game.win = True
            board_model[2].config(background='#5DA60A')
            board_model[5].config(background='#5DA60A')
            board_model[8].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

    def check_horizontal_line_combination(self, symbol):
        board_model = self.get_all_buttons()

        if board_model[0]['text'] == symbol and board_model[1]['text'] == symbol and board_model[2]['text'] == symbol:
            Game.win = True
            board_model[0].config(background='#5DA60A')
            board_model[1].config(background='#5DA60A')
            board_model[2].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

        elif board_model[3]['text'] == symbol and board_model[4]['text'] == symbol and board_model[5]['text'] == symbol:
            Game.win = True
            board_model[3].config(background='#5DA60A')
            board_model[4].config(background='#5DA60A')
            board_model[5].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

        elif board_model[6]['text'] == symbol and board_model[7]['text'] == symbol and board_model[8]['text'] == symbol:
            Game.win = True
            board_model[6].config(background='#5DA60A')
            board_model[7].config(background='#5DA60A')
            board_model[8].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

    def check_diagonal_line_combination(self, symbol):
        board_model = self.get_all_buttons()
        if board_model[0]['text'] == symbol and board_model[4]['text'] == symbol and board_model[8]['text'] == symbol:
            Game.win = True
            board_model[0].config(background='#5DA60A')
            board_model[4].config(background='#5DA60A')
            board_model[8].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

        elif board_model[2]['text'] == symbol and board_model[4]['text'] == symbol and board_model[6]['text'] == symbol:
            Game.win = True
            board_model[2].config(background='#5DA60A')
            board_model[4].config(background='#5DA60A')
            board_model[6].config(background='#5DA60A')
            self.win_message(symbol)
            self.disable_all_buttons()

    def check_global_win(self, symbol):
        self.check_vertical_line_combination(symbol)
        self.check_horizontal_line_combination(symbol)
        self.check_diagonal_line_combination(symbol)
