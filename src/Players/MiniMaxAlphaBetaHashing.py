from Player import Player
import random


class MiniMaxAlphaBetaHashing(Player):
    def __init__(self, color, depth):
        self.color = color
        self.depth = depth
        self.name = "Minimax Alpha Beta Hashing"
        self.nodes_visited = 0
        self.visited = {}
        self.best_move = None

    def get_move(self, gamestate):
        turn_multiplier = 1 if self.color == 1 else -1
        self.visited = {}
        legal_moves = gamestate.get_legal_moves()
    
        eval, move = self.minimax_alpha_beta(gamestate, self.depth, turn_multiplier, float("-inf"), float("inf"), legal_moves)
        return move
    
    
    def filter_moves(self, moves, move, reinsert):
        for m in moves:
            if ((m.row1, m.col1) == (move.row1, move.col1) or (m.row1, m.col1) == (move.row2, move.col2) or
                    (m.row2, m.col2) == (move.row1, move.col1) or (m.row2, m.col2) == (move.row2, move.col2)):
                reinsert.append(m)
        for m in reinsert:
            moves.remove(m)
        return

    def minimax_alpha_beta(self, gamestate, depth, turn_multiplier, alpha, beta, legal_moves):
        self.nodes_visited += 1

        if gamestate.tostring() in self.visited:
            return self.visited[gamestate.tostring()], None
        
        if depth == 0 or len(legal_moves) == 0:
            return turn_multiplier * MiniMaxAlphaBetaHashing.eval(gamestate), None

        max_score = float("-inf")
        best_move = None
        legal_moves_copy = legal_moves.copy()

        for move in legal_moves_copy:          
            to_reinsert = []
            self.filter_moves(legal_moves, move, to_reinsert)
            gamestate.make_move(move)
            res =  self.minimax_alpha_beta(gamestate, depth - 1, -turn_multiplier, -beta, -alpha, legal_moves)
            score = -res[0]

            if score > max_score:
                max_score = score
                best_move = move

            for m in to_reinsert:
                legal_moves.append(m)

            gamestate.unmake_move()
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break

        self.visited[gamestate.tostring()] = max_score
        return max_score, best_move


    def eval(gamestate):
        score = gamestate.score()
        return sum(score[0]) - sum(score[1])
