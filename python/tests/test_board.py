#test_board.py

import unittest


from mechanics import initializeGame
from kivy.logger import Logger


class TestMechanics(unittest.TestCase):
    
    def setUp(self):
        self.board = initializeGame()


    def test_board_creation(self):
        self.assertEqual(10, len(self.board.values[0]))


    def test_board_advance(self):
        def _log_board_info():
            Logger.info(f'Advancing board:\n {self.board.values[0]}')
            Logger.info(f'Board Neighbors:\n {self.board.neighbors[0]}')
        
        self.board.advance()
        _log_board_info()
        self.board.advance()
        _log_board_info()