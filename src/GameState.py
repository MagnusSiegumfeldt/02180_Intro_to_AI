from Player import Player
from Move import Move

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
        self.move_log = []


    def make_move(self, move):
        self.board[move.row1][move.col1] = 1
        self.board[move.row2][move.col2] = 2
        self.white_to_move = not self.white_to_move
        self.move_log.append(move)

    def get_legal_moves(self):
        legal_moves = []
        for row_white in range(9):
            for col_white in range(9):
                # Check if the square is empty
                if self.board[row_white][col_white] == 0:
                    # Check if the square is adjacent to a black piece
                    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    for dr, dc in directions:
                        row_black, col_black = row_white + dr, col_white + dc
                        # Check if the black piece is within the board and the square is empty
                        if 0 <= row_black < 9 and 0 <= col_black < 9 and self.board[row_black][col_black] == 0:
                            legal_moves.append(Move(row_white, col_white, row_black, col_black))
        return legal_moves

    def finished(self):
        return len(self.get_legal_moves()) == 0