import tkinter as tk

from gameboardcls import Gameboard

window = tk.Tk()
window.geometry('462x595+550+50')
window.maxsize(462, 595)
window.resizable(False, False)
window.title('Tic Tac Toe')
icon = tk.PhotoImage(file='tic-tac-toe.png')
window.iconphoto(False, icon)

gameboard = Gameboard(window, 3, 3)
gameboard.attach_gameboard_to_window()
