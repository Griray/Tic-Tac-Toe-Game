"""This module contains code for Button class. It has imports from game, ai and gameboardcls modules"""

import tkinter as tk
from tkinter import messagebox
from tkinter import *

from game import Game
from ai import Ai
import gameboardcls


class Button:
    """Class Button used for creation of play buttons and new game button also add functionality of click to buttons

        Basic use - creation of game buttons for game board

        Attributes
        ----------
        clickable: bool
            status of button, if True it is clickable, else not clickable

        main_window: tk.Tk
            gui window where play buttons is located

        rows: int
            quantity of rows in game board construction, needed for coordinates of buttons

        columns: int
             quantity of columns in game board construction, needed for coordinates of buttons

        Methods
        -------
        generate_button()
            create gui object: tk.Button with its features and command click

        click()
            contains game process logic and print symbol in button after clicking

        new_game_button_func()
            create functionality for new game game button, clear all buttons from symbol and activate them.
            Update all games parameters to defaults

        create_new_game_button()
            create gui object: tk.Button with its features and command new_game_button_func

    """
    clickable = True

    def __init__(self, main_window: tk.Tk, rows: int, columns: int):
        self.main_window = main_window
        self.rows = rows
        self.columns = columns

    def generate_button(self, row, column):
        """Create gui object: tk.Button with command click, grid this button on game board using row and column value"""
        play_btn = tk.Button(self.main_window, text=' ', font=('Typesauce', 20, 'bold'),
                             activebackground='#A17A37', background='#DFA43E',
                             foreground='#EBDFCB', width=8, height=4,
                             command=lambda: self.click(play_btn)
                             )
        play_btn.grid(row=row, column=column)
        return play_btn

    def click(self, button):
        """Print symbol in button. Create Ai object, leads the gameplay of player and ai, check wrong moves and draw."""
        intel = Ai()
        if button['text'] == ' ' and Button.clickable:
            if Game.computer_move_quantity < 4:
                button['text'] = 'X'
                Game.player_move_quantity += 1
                Button.clickable = False
                gameboardcls.Gameboard.gameboard_obj.check_global_win('X')
                if not Button.clickable:
                    if Game.player_move_quantity <= 4:
                        intel.move_to_win()
                        Game.computer_move_quantity += 1
                        Button.clickable = True
                        gameboardcls.Gameboard.gameboard_obj.check_global_win('O')
                    else:
                        messagebox.showinfo('Attention', 'It seems to be a draft\n Lets restart game')
                        self.new_game_button_func()
            else:
                messagebox.showinfo('Attention', 'It seems to be a draft\n Lets restart game')
                self.new_game_button_func()
        else:
            messagebox.showerror('Attention', 'Oops... This button has already been pushed\n Choose another one')

    def new_game_button_func(self):
        """Activate, clear and recolour buttons from all_buttons. Update all games parameters to defaults"""
        for btn in gameboardcls.Gameboard.gameboard_obj.get_all_buttons():
            btn['text'] = ' '
            btn.config(background='#DFA43E')
            btn.config(state=ACTIVE)
            Game.win = False
            self.clickable = True
            Game.player_move_quantity = 0
            Game.computer_move_quantity = 0

    def create_new_game_button(self):
        """Create gui object: tk.Button with its features and command new_game_button_func. Grid button on game board"""
        new_game_button = tk.Button(self.main_window, text='Start New Game', font='Typesauce',
                                    command=self.new_game_button_func
                                    )
        new_game_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
