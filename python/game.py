"""
Game Of Life
    See readme for environment setup

    Run with python run game.py
"""


import os

os.environ['KIVY_HOME'] = os.path.join(os.getcwd())

from render import GameApp, Logger

Logger.info('Status: Game Started')

if __name__ == "__main__":
    app = GameApp()
    app.run()