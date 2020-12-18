"""This module contains code for Gameboard class. It has imports from buttoncls and game modules"""


import tkinter as tk
from tkinter import messagebox
from tkinter import *

from buttoncls import Button
from game import Game


class Gameboard:
    """Class Gameboard used for creating gui of playing area (game board)

        Basic use - create game board and contents all buttons information which are used in game board

        Attributes
        ----------
        all_buttons: list
            contains information about all buttons located on game board

        gameboard_obj: self
            contains self, needed for usage in other modules because of circular imports

        main_window: tk.Tk
            gui window where game board is located

        rows: int
            quantity of rows in game board construction

        columns: int
             quantity of columns in game board construction

        Methods
        -------
        create_gameboard_model()
            Create game board model and return all_buttons which are used for creation of gameboard

        get_all_buttons()
            additional method which return all_buttons used for creation of gameboard with whole information about them

        attach_gameboard_to_window()
            places the game board in the window

        win_message()
            return tk.messagebox with information about the winner of the game

        disable_all_buttons()
            deactivate buttons from all_buttons

        check_vertical_line_combination(symbol)
            check win for vertical lines combinations of symbol (X or O)

        check_horizontal_line_combination(symbol)
            check win for horizontal lines combinations of symbol (X or O)

        check_diagonal_line_combination(symbol)
            check win for diagonal lines combinations of symbol (X or O)

        check_global_win(symbol)
             verification of victory on all sides (vertical, horizontal, diagonal). Use check_diagonal_line_combination,
             check_horizontal_line_combination, check_vertical_line_combination methods

    """

    all_buttons = []
    gameboard_obj = None

    def __init__(self, main_window: tk.Tk, rows: int, columns: int):
        self.main_window = main_window
        self.rows = rows
        self.columns = columns
        Gameboard.gameboard_obj = self

    def create_gameboard_model(self):
        """Create Button class object, create and locate play buttons on game board based on number of rows, columns"""
        basic_button = Button(self.main_window, self.rows, self.columns)
        for row in range(self.rows):
            for column in range(self.columns):
                self.all_buttons.append(basic_button.generate_button(row, column))
        basic_button.create_new_game_button()
        return self.all_buttons

    def get_all_buttons(self):
        """Return list of all play buttons"""
        return self.all_buttons

    def attach_gameboard_to_window(self):
        """Place created game board in the window"""
        self.create_gameboard_model()
        self.main_window.mainloop()

    def win_message(self, symbol):
        """Return tk.messagebox with information about the winner of the game, depending on the symbol used"""
        if symbol == 'X':
            messagebox.showinfo('Congratulations!', 'X won this round')
        elif symbol == 'O':
            messagebox.showinfo('Congratulations!', 'O won this round')

    def disable_all_buttons(self):
        """Deactivate buttons from all_buttons. Used for button deactivation after win in the game"""
        board_model = self.get_all_buttons()
        for btn in board_model:
            btn.config(state=DISABLED)

    def check_vertical_line_combination(self, symbol):
        """Check vertical win line combinations. If win, deactivate all buttons and appear win message"""
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
        """Check horizontal win line combinations. If win, deactivate all buttons and appear win message"""
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
        """Check diagonal win line combinations. If win, deactivate all buttons and appear win message"""
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
        """Step-by-step verification of victory on all sides (vertical, horizontal, diagonal)"""
        self.check_vertical_line_combination(symbol)
        self.check_horizontal_line_combination(symbol)
        self.check_diagonal_line_combination(symbol)
