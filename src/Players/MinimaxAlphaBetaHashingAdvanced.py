from Player import Player


class MiniMaxAlphaBetaHashingAdvanced(Player):
    field_values = [
        [0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90],
        [0.90, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.90],
        [0.90, 0.95, 1.00, 1.00, 1.00, 1.00, 1.00, 0.95, 0.90],
        [0.90, 0.95, 1.00, 1.05, 1.05, 1.05, 1.00, 0.95, 0.90],
        [0.90, 0.95, 1.00, 1.05, 1.10, 1.05, 1.00, 0.95, 0.90],
        [0.90, 0.95, 1.00, 1.05, 1.05, 1.05, 1.00, 0.95, 0.90],
        [0.90, 0.95, 1.00, 1.00, 1.00, 1.00, 1.00, 0.95, 0.90],
        [0.90, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.90],
        [0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90],
    ]

    def __init__(self, color, depth):
        self.color = color
        self.depth = depth
        self.name = "Minimax Alpha Beta Hashing Advanced"
        self.nodes_visited = 0

    def get_move(self, gamestate):
        global best_move
        self.nodes_visited = 0
        global visited
        visited = {}

        best_move = None
        turn_multiplier = 1 if self.color == 1 else -1
        self.minimax_alpha_beta(
            gamestate, self.depth, turn_multiplier, float("-inf"), float("inf")
        )
        print("Nodes visited:", self.nodes_visited)
        return best_move

    def minimax_alpha_beta(self, gamestate, depth, turn_multiplier, alpha, beta):
        global best_move
        global visited
        self.nodes_visited += 1

        if visited.__contains__(gamestate.tostring()):
            return -turn_multiplier * float("inf")
        moves = gamestate.get_legal_moves_ordered()
        if depth == 0 or len(moves) == 0:
            return turn_multiplier * MiniMaxAlphaBetaHashingAdvanced.eval(gamestate)

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
        visited[gamestate.tostring()] = True
        return max_score

    def dfs(gamestate, row, col, visited, counted, color):
        if visited[row][col] or gamestate.board[row][col] != color:
            return 0, 0

        stack = []
        stack.append((row, col))
        visited[row][col] = True

        size = 0
        boundary = 0

        while len(stack) > 0:
            r, c = stack.pop()
            size += 1 * MiniMaxAlphaBetaHashingAdvanced.field_values[r][c]

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
                elif (
                    0 <= nr < 9
                    and 0 <= nc < 9
                    and not counted[nr][nc]
                    and gamestate.board[nr][nc] == 0
                ):
                    boundary += 1
                    counted[nr][nc] = True

        return size, boundary

    def eval(gamestate):
        visited = [[False for _ in range(9)] for _ in range(9)]
        best = [[0, 0], [0, 0]]

        for i in range(9):
            for j in range(9):
                current_color = gamestate.board[i][j]
                if current_color == 0:
                    continue
                idx = current_color - 1
                counted = [[False for _ in range(9)] for _ in range(9)]
                size, boundary = MiniMaxAlphaBetaHashingAdvanced.dfs(
                    gamestate, i, j, visited, counted, current_color
                )
                total = size + (boundary / 32)

                if best[idx][0] >= best[idx][1] and best[idx][1] < total:
                    best[idx][1] = total

                elif best[idx][0] <= best[idx][1] and best[idx][0] < total:
                    best[idx][0] = total

        return sum(best[0]) - sum(best[1])
