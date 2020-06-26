"""
Render Engine
"""


import kivy
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout


from kivy.uix.label import Label
from kivy.uix.button import Button


from mechanics import (
    initializeGame,
    updateValue,
    step
)

from kivy.logger import Logger
from kivy.clock import Clock



class BoardGrid(GridLayout):

    def __init__(self, **kwargs):
        super(BoardGrid, self).__init__(**kwargs)

        self.cell_colors = {
            0: [0, 1, 0, 1],
            1: [0, 0, 1, 1],
        }
        
        
        blen = kwargs['cols']
        self.board = initializeGame(board_size=[blen, blen, 2])

        self.cells = []
        for i in range(blen**2):
            newcell = Button(text=f'{i}')
            self.cells.append(newcell)
            super().add_widget(newcell)

        Logger.info(f'STATUS: Created widget type {type(self.cells)} of size {len(self.cells)}')


    def draw_cell_color(self):
        vals = self.board.values[0].flatten()
        Logger.debug(f'STATUS: Board Values - {vals}')

        for i, cell in enumerate(self.cells):
            cell.background_color = self.cell_colors[vals[i]]


    def advance_game(self, dt):
        Logger.debug(f'STATUS: Advancing: Board Values - {self.board.values}')
        step(self.board, layers=None)
        self.draw_cell_color()




class GameApp(App):
    def __init__(self, **kwargs):
        super(GameApp, self).__init__(**kwargs)
        self.boardsize = 25

    def build(self):
        board = BoardGrid(cols=self.boardsize)
        board.draw_cell_color()
        Clock.schedule_interval(board.advance_game, 60.0/60.0)
        return board




if __name__ == "__main__":
    GameApp().run()