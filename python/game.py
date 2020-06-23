import mechanics 
from mechanics import initializeGame, updateValue

board = initializeGame()

if __name__ == "__main__":
    print(board.values[0])
    updateValue(board=board, coord=[0,0,0], value=1)
    updateValue(board=board, coord=[2,2,0], value=1)
    print(board.values[0])