from Move import Move
from Player import Player


class MinimaxArea(Player):
    def __init__(self, color, depth):
        self.color = color
        self.depth = depth


    # Gets input from the user, asserts that it is valid, and returns the Move object     
    def get_move(self, gamestate):
        #if white
        if self.color == 1:
            return self.minimax(gamestate, self.depth, True)[1]
        #if black
        else:
            return self.minimax(gamestate, self.depth, False)[1]

            

    #Returns a (Integer, Move) tuple describing the maximum outcome (assuming rational minimizing player 2)
    def minimax(self, gamestate, max_depth, is_max):
        if max_depth == 0:  
            return (MinimaxArea.eval(gamestate), None)
        
        #TODO What if game ends?
        moves = gamestate.get_legal_moves()
        if len(moves) == 0:
            return (MinimaxArea.eval(gamestate), None)
        
        #board 
        infinity = -1000 if is_max else 1000
        current_best = (infinity, None)

        for m in moves:
            #Make the moves, recurse and clean up.
            gamestate.make_move(m)
            best_child = self.minimax(gamestate, max_depth - 1, not is_max)
            gamestate.unmake_move()

            if is_max:
                if current_best[0] < best_child[0]:
                    current_best = (best_child[0], m)
            else:
                #print("HERE", best_child[0], current_best[0])
                if best_child[0] < current_best[0]:
                    current_best = (best_child[0], m) 
        return current_best


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
                if 0 <= nr < 9 and 0 <= nc < 9 and not visited[nr][nc] and gamestate.board[nr][nc] == color: 
                    stack.append((nr, nc))
                    visited[nr][nc] = True
        return size

    def eval(gamestate): 
        # Todo: this is naive
        visited = [[False for _ in range(9)] for _ in range(9)]        
        best = [[0, 0],[0, 0]]
        for i in range(9):
            for j in range(9):
                current_color = gamestate.board[i][j]
                if current_color == 0: 
                    continue
                idx = current_color - 1
                size = MinimaxArea.dfs(gamestate, i, j, visited, current_color)
                if best[idx][0] >= best[idx][1] and best[idx][1] < size:
                    best[idx][1] = size
                elif best[idx][0] <= best[idx][1] and best[idx][0] < size:
                    best[idx][0] = size   
        
        return sum(best[0]) - sum(best[1])