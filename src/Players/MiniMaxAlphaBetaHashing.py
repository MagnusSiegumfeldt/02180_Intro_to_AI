from Player import Player
import random


class MiniMaxAlphaBetaHashing(Player):
    def __init__(self, color, depth):
        self.color = color
        self.depth = depth
        self.name = "Minimax Alpha Beta Hashing"
        self.nodes_visited = 0
        self.visited = {}

    # Return best move.
    def get_move(self, gamestate):
        turn_multiplier = 1 if self.color == 1 else -1
        self.visited = {}
        legal_moves = gamestate.get_legal_moves()
    
        eval, move = self.minimax_alpha_beta(gamestate, self.depth, turn_multiplier, float("-inf"), float("inf"), legal_moves)
        return move
    

    def minimax_alpha_beta(self, gamestate, depth, turn_multiplier, alpha, beta, legal_moves):
        self.nodes_visited += 1

        # If state is hashed return it.
        if gamestate.tostring() in self.visited:
            return self.visited[gamestate.tostring()], None
        
        # If depth is 0 or no legal moves
        if depth == 0 or len(legal_moves) == 0:
            return turn_multiplier * MiniMaxAlphaBetaHashing.eval(gamestate), None

        max_score = float("-inf")
        best_move = None
        legal_moves = gamestate.get_legal_moves_ordered()
        # Try every move
        for move in legal_moves:          
            # Make move, try it, unmake it.
            gamestate.make_move(move)
            score =  -self.minimax_alpha_beta(gamestate, depth - 1, -turn_multiplier, -beta, -alpha, legal_moves)[0]
            
            if score > max_score:
                max_score = score
                best_move = move

            gamestate.unmake_move()

            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        # Hash score
        self.visited[gamestate.tostring()] = max_score
        return max_score, best_move


    def eval(gamestate):
        score = gamestate.score()
        return sum(score[0]) - sum(score[1])
