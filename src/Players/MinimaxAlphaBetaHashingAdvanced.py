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
        self.visited = {}

    # Return the best move for the current gamestate
    def get_move(self, gamestate):
        turn_multiplier = 1 if self.color == 1 else -1
        self.visited = {}
        legal_moves = gamestate.get_legal_moves()
    
        eval, move = self.minimax_alpha_beta(gamestate, self.depth, turn_multiplier, float("-inf"), float("inf"), legal_moves)
        return move
    
    # Alphabeta search.
    def minimax_alpha_beta(self, gamestate, depth, turn_multiplier, alpha, beta, legal_moves):
        self.nodes_visited += 1

        # If state is hashed.
        if gamestate.tostring() in self.visited:
            return self.visited[gamestate.tostring()], None
        
        if depth == 0 or len(legal_moves) == 0:
            return turn_multiplier * MiniMaxAlphaBetaHashingAdvanced.eval(gamestate), None

        max_score = float("-inf")
        best_move = None

        legal_moves = gamestate.get_legal_moves_ordered()
        # Try out all moves
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
        
        # Save hash
        self.visited[gamestate.tostring()] = max_score
        return max_score, best_move
    
    # DFS through the colored area to find weighted size and boundary.
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
                if (0 <= nr < 9 and 0 <= nc < 9 and not visited[nr][nc] and gamestate.board[nr][nc] == color):
                    stack.append((nr, nc))
                    visited[nr][nc] = True
                elif (0 <= nr < 9 and 0 <= nc < 9 and not (nr, nc) in counted and gamestate.board[nr][nc] == 0):
                    boundary += 1
                    counted[(nr, nc)] = True

        return size, boundary


    # Eval board state by largest areas, boundaries and weighted board.
    def eval(gamestate):
        visited = [[False for _ in range(9)] for _ in range(9)]
        best = [[0, 0], [0, 0]]

        # For every square run dfs to find areas. Keep two largest for every color.
        for i in range(9):
            for j in range(9):
                current_color = gamestate.board[i][j]
                if current_color == 0:
                    continue
                idx = current_color - 1
                counted = {}
                size, boundary = MiniMaxAlphaBetaHashingAdvanced.dfs(gamestate, i, j, visited, counted, current_color)
                total = size + (boundary / 81)

                if best[idx][0] >= best[idx][1] and best[idx][1] < total:
                    best[idx][1] = total

                elif best[idx][0] <= best[idx][1] and best[idx][0] < total:
                    best[idx][0] = total

        return sum(best[0]) - sum(best[1])
