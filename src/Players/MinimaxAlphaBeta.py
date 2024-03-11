from Player import Player


class MinimaxAlphaBeta(Player):
    def __init__(self, depth, color):
        self.depth = depth
        self.color = color

    def get_move(self, gamestate):
        global best_move
        self.nodes_visited = 0

        best_move = None
        turn_multiplier = 1 if self.color == 1 else -1
        self.minimax_alpha_beta(
            gamestate, self.depth, turn_multiplier, float("-inf"), float("inf")
        )
        print("Nodes visited:", self.nodes_visited)
        return best_move

    def minimax_alpha_beta(self, gamestate, depth, turn_multiplier, alpha, beta):
        global best_move
        self.nodes_visited += 1

        moves = gamestate.get_legal_moves_ordered()
        if depth == 0 or len(moves) == 0:
            return turn_multiplier * self.eval(gamestate)

        max_score = float("-inf")
        for move in moves:
            gamestate.make_move(move)
            # next_moves = gamestate.get_legal_moves_ordered()
            score = -self.minimax_alpha_beta(
                gamestate, depth - 1, -turn_multiplier, -beta, -alpha
            )
            if score > max_score:
                max_score = score
                if depth == self.depth:
                    best_move = move
            gamestate.unmake_move()
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        return max_score

    def eval(self, gamestate):
        score = gamestate.score()
        return sum(score[0]) - sum(score[1])