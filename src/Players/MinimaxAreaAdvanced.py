from Move import Move
from Player import Player


class MinimaxAreaAdvanced(Player):
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
        self.name = "Minimax Area Advanced"
        self.nodes_visited = 0

    # Gets input from the user, asserts that it is valid, and returns the Move object
    def get_move(self, gamestate):
        self.nodes_visited = 0
        # if white
        if self.color == 1:
            return self.minimax(gamestate, self.depth, True)[1]
        # if black
        else:
            return self.minimax(gamestate, self.depth, False)[1]

    # Returns a (Integer, Move) tuple describing the maximum outcome (assuming rational minimizing player 2)
    def minimax(self, gamestate, max_depth, is_max):
        self.nodes_visited += 1
        if max_depth == 0:
            return (MinimaxAreaAdvanced.eval(gamestate), None)

        moves = gamestate.get_legal_moves()
        if len(moves) == 0:

            return (MinimaxAreaAdvanced.eval(gamestate), None)

        # board
        infinity = -1000 if is_max else 1000
        current_best = (infinity, None)

        for m in moves:
            # Make the moves, recurse and clean up.
            gamestate.make_move(m)
            best_child = self.minimax(gamestate, max_depth - 1, not is_max)
            gamestate.unmake_move()
            if is_max and current_best[0] < best_child[0]:
                current_best = (best_child[0], m)
            elif not is_max and best_child[0] < current_best[0]:
                current_best = (best_child[0], m)
        return current_best

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
            size += 1 * MinimaxAreaAdvanced.field_values[r][c]

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
                size, boundary = MinimaxAreaAdvanced.dfs(
                    gamestate, i, j, visited, counted, current_color
                )
                total = size + (boundary / 4)

                if best[idx][0] >= best[idx][1] and best[idx][1] < total:
                    best[idx][1] = total

                elif best[idx][0] <= best[idx][1] and best[idx][0] < total:
                    best[idx][0] = total

        return sum(best[0]) - sum(best[1])
