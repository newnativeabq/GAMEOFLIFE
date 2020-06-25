"""
    Game Mechanics and buffering
"""
from grid import ConvolveSquare, Board



def initializeGame(board_size: list = [10,10,2]):
    return Board(*board_size)


def updateValue(board, coord, value):
    board.set_cell_value(coord, value)


def step(board, layers=None):
    board.advance(layers)