from Move import Move
from Player import Player

class MinimaxArea(Player):
    def __init__(self, color, depth):
        self.color = color
        self.depth = depth


    # Gets input from the user, asserts that it is valid, and returns the Move object     
    def get_move(self, gamestate):
        global nodes_visited
        nodes_visited = 0

        #if white
        if self.color == 1:
            move = self.minimax(gamestate, self.depth, True)[1]
            print("Nodes visited:", nodes_visited)
            return move
        #if black
        else:
            move = self.minimax(gamestate, self.depth, False)[1]
            print("Nodes visited:", nodes_visited)
            return move

            

    #Returns a (Integer, Move) tuple describing the maximum outcome (assuming rational minimizing player 2)
    def minimax(self, gamestate, max_depth, is_max):
        global nodes_visited
        nodes_visited += 1
        if max_depth == 0:  
            return (self.eval(gamestate), None)
        
        moves = gamestate.get_legal_moves()
        if len(moves) == 0:
            return (self.eval(gamestate), None)
        
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
                if best_child[0] < current_best[0]:
                    current_best = (best_child[0], m) 
        return current_best

    def eval(self, gamestate):
        score = gamestate.score()
        return sum(score[0]) - sum(score[1])
