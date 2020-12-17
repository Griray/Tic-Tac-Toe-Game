import random

import gameboardcls


class Ai:
    symbol = 'O'

    def __init__(self):
        pass

    @staticmethod
    def can_win(btn1, btn2, btn3, symbol: str):
        chance = False
        if btn1['text'] == symbol and btn2['text'] == symbol and btn3['text'] == ' ':
            btn3['text'] = Ai.symbol
            chance = True
        elif btn1['text'] == symbol and btn2['text'] == ' ' and btn3['text'] == symbol:
            btn2['text'] = Ai.symbol
            chance = True
        elif btn1['text'] == ' ' and btn2['text'] == symbol and btn3['text'] == symbol:
            btn1['text'] = Ai.symbol
            chance = True
        return chance

    def move_to_win(self):

        board_model = gameboardcls.Gameboard.gameboard_obj.get_all_buttons()

        horizontal_win_combinations = [
            [board_model[0], board_model[1], board_model[2]],
            [board_model[3], board_model[4], board_model[5]],
            [board_model[6], board_model[7], board_model[8]]
        ]

        vertical_win_combination = [
            [board_model[0], board_model[3], board_model[6]],
            [board_model[1], board_model[4], board_model[7]],
            [board_model[2], board_model[5], board_model[8]]
        ]

        for digit in range(3):
            if self.can_win(horizontal_win_combinations[digit][0],
                            horizontal_win_combinations[digit][1],
                            horizontal_win_combinations[digit][2],
                            Ai.symbol
                            ):
                return
            elif self.can_win(vertical_win_combination[digit][0],
                              vertical_win_combination[digit][1],
                              vertical_win_combination[digit][2],
                              Ai.symbol
                              ):
                return
        if self.can_win(board_model[0],
                        board_model[4],
                        board_model[8],
                        Ai.symbol
                        ):
            return
        elif self.can_win(board_model[2],
                          board_model[4],
                          board_model[6],
                          Ai.symbol
                          ):
            return

        for digit in range(3):
            if self.can_win(horizontal_win_combinations[digit][0],
                            horizontal_win_combinations[digit][1],
                            horizontal_win_combinations[digit][2],
                            'X'
                            ):
                return
            elif self.can_win(vertical_win_combination[digit][0],
                              vertical_win_combination[digit][1],
                              vertical_win_combination[digit][2],
                              'X'
                              ):
                return
        if self.can_win(board_model[0],
                        board_model[4],
                        board_model[8],
                        'X'
                        ):
            return
        elif self.can_win(board_model[2],
                          board_model[4],
                          board_model[6],
                          'X'
                          ):
            return
        while True:
            btn = random.randint(0, 8)
            if board_model[btn]['text'] == ' ':
                board_model[btn]['text'] = 'O'
                break

