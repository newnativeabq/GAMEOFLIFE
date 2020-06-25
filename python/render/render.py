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


class BoardGrid(GridLayout):

    def __init__(self, **kwargs):
        super(BoardGrid, self).__init__(**kwargs)

        blen = kwargs['cols']
        self.board = initializeGame(board_size=[blen, blen, 2])

        for i in range(blen**2):
            super().add_widget(Button(text=f'Cell {i}'))





class GameApp(App):

    def build(self):
        board = BoardGrid(cols=2)
        return board




if __name__ == "__main__":
    GameApp().run()