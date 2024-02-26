from Player import Player
import pandas as pd

class GameState:
    def __init__(self, player1, player2):
        # Initial empty board 
        self.board = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ]
        self.player1 = player1
        self.player2 = player2
        self.white_to_move = True



    def make_move(self, move):
        self.board[move.row1][move.col1] = 1
        self.board[move.row2][move.col2] = 2

    def get_legal_moves(self):
        pass

    def finished(self):
        # TODO: Rmeove this
        return False



        if not self.get_legal_moves():
            return True
        else:
            return False