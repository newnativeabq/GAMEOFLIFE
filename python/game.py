"""
Game Of Life
    See readme for environment setup

    Run with python run game.py
"""



from render import GameApp


import logging 
import os

logpath = os.path.join(
    os.getcwd(), 'game.log'
)

if __name__ == "__main__":
    logging.basicConfig(
        filename=logpath,
        level = logging.DEBUG
    )
    rootlogger = logging.getLogger(__name__)
    rootlogger.info('Game Started')
    print('log check')
    # GameApp().run()