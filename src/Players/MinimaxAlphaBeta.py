from Player import Player
import time as t
import random


class MinimaxAlphaBeta(Player):
    def __init__(self, color, depth):
        self.color = color
        self.depth = depth

    def get_move(self, gamestate):
        global best_move
        global nodes_visited
        nodes_visited = 0

        start = t.time()
        best_move = None
        turn_multiplier = 1 if self.color == 1 else -1
        self.minimax_alpha_beta(
            gamestate, self.depth, turn_multiplier, float("-inf"), float("inf")
        )
        print("Time taken:", t.time() - start, "\nNodes visited:", nodes_visited)
        return best_move

    def minimax_alpha_beta(self, gamestate, depth, turn_multiplier, alpha, beta):
        global best_move
        global nodes_visited
        nodes_visited += 1

        moves = gamestate.get_legal_moves_ordered()
        if depth == 0 or len(moves) == 0:
            return turn_multiplier * gamestate.eval()

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

    def dfs(gamestate, row, col, visited, color):
        if visited[row][col] or gamestate.board[row][col] != color:
            return 0
        stack = []
        stack.append((row, col))
        visited[row][col] = True
        size = 0
        while len(stack) > 0:
            r, c = stack.pop()
            size += 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < 9
                    and 0 <= nc < 9
                    and not visited[nr][nc]
                    and gamestate.board[nr][nc] == color
                ):
                    stack.append((nr, nc))
                    visited[nr][nc] = True
        return size

    def eval(self, gamestate):
        # Todo: this is naive
        visited = [[False for _ in range(9)] for _ in range(9)]
        best = [[0, 0], [0, 0]]
        for i in range(9):
            for j in range(9):
                current_color = gamestate.board[i][j]
                if current_color == 0:
                    continue
                idx = current_color - 1
                size = MinimaxAlphaBeta.dfs(gamestate, i, j, visited, current_color)
                if best[idx][0] >= best[idx][1] and best[idx][1] < size:
                    best[idx][1] = size
                elif best[idx][0] <= best[idx][1] and best[idx][0] < size:
                    best[idx][0] = size
        return sum(best[0]) - sum(best[1])
