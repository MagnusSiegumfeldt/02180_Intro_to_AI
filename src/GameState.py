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

    def get_legal_moves_ordered(self):
        current_player = 1 if self.white_to_move else 2
        opponent_player = 2 if self.white_to_move else 1

        # Moves that:
        # - Add a neighboring piece of the same color as the current player's piece
        # - Do not introduce a neighbor of the opponent's color next to a piece of the same color
        first_rank_moves = []

        # Moves that:
        # - Add a neighboring piece of the same color as the current player's piece
        # - Also introduce a neighbor of the opponent's color next to a piece of the same color
        second_rank_moves = []

        # Moves that increase the surface area of the current player's color
        # third_rank_moves = [] TODO

        # Moves that decrease the surface area of the opponents player's color
        # fourth_rank_moves = [] TODO

        # Other moves
        last_rank_moves = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        for row_white in range(9):
            for col_white in range(9):
                # Check if the square is empty
                if self.board[row_white][col_white] == 0:
                    # Check if the square is adjacent to a black piece
                    for dr, dc in directions:
                        row_black, col_black = row_white + dr, col_white + dc
                        # Check if the black piece is within the board and the square is empty
                        if 0 <= row_black < 9 and 0 <= col_black < 9 and self.board[row_black][col_black] == 0:
                            new_move = Move(row_white, col_white, row_black, col_black)
                            
                            friendly_row, friendly_col = (row_white, col_white) if current_player == 1 else (row_black, col_black)
                            opponent_row, opponent_col = (row_black, col_black) if current_player == 1 else (row_white, col_white)

                            friendly_has_friendly_neighbors = self.has_friendly_neighbors(friendly_row, friendly_col, current_player)
                            opponent_has_friendly_neighbors = self.has_friendly_neighbors(opponent_row, opponent_col, opponent_player)

                            if friendly_has_friendly_neighbors:
                                if not opponent_has_friendly_neighbors:
                                    first_rank_moves.append(new_move)
                                else:
                                    second_rank_moves.append(new_move)
                            else:
                                last_rank_moves.append(new_move)
        return first_rank_moves + second_rank_moves + last_rank_moves

    def has_friendly_neighbors(self, row, col, player):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            row_adj, col_adj = row + dr, col + dc
            if 0 <= row_adj < 9 and 0 <= col_adj < 9 and self.board[row_adj][col_adj] == player:
                return True
        return False
    
    def finished(self):
        return len(self.get_legal_moves()) == 0