import random

from src.game.Game import Game
from src.model.Model import Model
from src.model.board.Board import Board
from src.ui.cui.ConsoleUI import ConsoleUI


class ConsoleApp:
    def __init__(self):
        self.model = Model()
        self.cui = ConsoleUI(self.model)
        self.game = Game(self.model)

    def restart(self):
        self.game.restart()

    def run(self):
        self.restart()
        while True:
            self.cui.render()
            action = input('press enter to continue, space to restart, anything else to quit')
            if action == '':
                self.game.make_random_move()
            elif action == ' ':
                self.restart()
            else:
                break
