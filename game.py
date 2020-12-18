"""This module contains code for Game class"""


class Game:
    """Class Game used for game process features such us win status and move quantity either for player and AI

        Attributes
        ----------
        win: bool
            Status of the Game process. If win == True, game finishes, else game process continues.

        player_move_quantity: int
            Quantity of player move actions. It helps to to determine draw in the game

        computer_move_quantity: int
            Quantity of AI move actions. It helps to to determine draw in the game

    """

    win = False
    player_move_quantity = 0
    computer_move_quantity = 0

    def __init__(self):
        pass
