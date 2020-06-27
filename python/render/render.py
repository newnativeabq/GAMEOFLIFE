"""
Render Engine
"""


import kivy
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

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
        for i in range(blen):
            for j in range(blen):
                newcell = self._build_cell_button(text=f'{j},{i}')
                self.cells.append(newcell)
                super().add_widget(newcell)

        Logger.debug(f'STATUS: Created widget type {type(self.cells)} of size {len(self.cells)}')


    def _build_cell_button(self, text:str = None):
        newBtn = Button(
            text = text,
            id = text,
        )
        newBtn.bind(on_press = self._update_cell)
        return newBtn


    def _update_cell(self, instance):
        def _get_instance_index(instance):
            index = instance.id.split(',')
            return tuple(int(i) for i in index)

        def _flip_board_value(index):
            bcell = self.board._get_cell(coord=index)
            self.board.set_cell_value(index, int(not bcell.val))
            return bcell.val

        def _update_cell_color(instance, val):
            instance.background_color = self.cell_colors[val]

        index = _get_instance_index(instance)
        newVal = _flip_board_value(index)
        _update_cell_color(instance, newVal)
        self.board.analyze_board()


    def draw_cell_color(self):
        vals = self.board.values[0].flatten()
        # Logger.debug(f'STATUS: Board Values - {vals}')

        for i, cell in enumerate(self.cells):
            cell.background_color = self.cell_colors[vals[i]]


    def advance_game(self, dt):
        # Logger.debug(f'STATUS: Advancing: Board Values - {self.board.values[0]}')
        step(self.board, layers=None)
        self.draw_cell_color()








def initializeBoard(cols):
    board = BoardGrid(cols=cols)
    board.draw_cell_color()
    return board



class GameApp(App):
    def __init__(self, **kwargs):
        super(GameApp, self).__init__(**kwargs)
        self.title = 'Game of Life'
        self.boardsize = 10
        self.epoch = 0
        self.board = initializeBoard(self.boardsize)
        self.header = self._draw_header(
            BoxLayout(orientation='horizontal'))
        
        # Clock settings
        self.rate = 1
        self.active = False

    def _step(self, dt=None):
        self.board.advance_game(dt)
        self.epoch += 1
        self._update_header()


    def _draw_header(self, header=None):
        header.size_hint = (1, 0.125)
        
        self.startBtn = Button(
            text = "Start",
            size_hint = (1, 1),
            on_press = self._update_control_button
        )

        self.counter = Label(
            text = f'Epoch {self.epoch}',
            size_hint = (1, 1)
        )

        header.add_widget(self.startBtn)
        header.add_widget(self.counter)
        return header


    def _update_header(self):
        self.counter.text = f'Epoch {self.epoch}'


    
    def start(self):
        self.startBtn.text = 'Stop'
        self.active = True
        Clock.unschedule(self._step)
        Clock.schedule_interval(self._step, self.rate)

    def stop(self):
        self.startBtn.text = 'Start'
        self.active = False
        Clock.unschedule(self._step)

    def _update_control_button(self, dt):
        if self.active:
            self.stop()
        else:
            self.start()


    def build(self):
        gameWindow = BoxLayout(orientation='vertical')
        
        gameWindow.add_widget(self.header)
        gameWindow.add_widget(self.board)

        # Clock.schedule_interval(self._step, self.rate)
        # self.start()

        return gameWindow




if __name__ == "__main__":
    GameApp().run()