from Player import Player


class MinimaxAlphaBeta(Player):
    def __init__(self, depth, color):
        self.depth = depth
        self.color = color
        self.name = "Minimax Alpha Beta"
        self.nodes_visited = 0


    def get_move(self, gamestate):
        self.nodes_visited = 0
        turn_multiplier = 1 if self.color == 1 else -1

        eval, best_move = self.minimax_alpha_beta(gamestate, self.depth, turn_multiplier, float("-inf"), float("inf"))
        return best_move

    def minimax_alpha_beta(self, gamestate, depth, turn_multiplier, alpha, beta):
        self.nodes_visited += 1

        moves = gamestate.get_legal_moves_ordered()
        if depth == 0 or len(moves) == 0:
            return turn_multiplier * self.eval(gamestate), None

        max_score = float("-inf")
        best_move = None
        for move in moves:
            gamestate.make_move(move)

            score = -self.minimax_alpha_beta(gamestate, depth - 1, -turn_multiplier, -beta, -alpha)[0]
            if score > max_score:
                max_score = score
                if depth == self.depth:
                    best_move = move
            gamestate.unmake_move()
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        return max_score, best_move

    def eval(self, gamestate):
        score = gamestate.score()
        return sum(score[0]) - sum(score[1])
