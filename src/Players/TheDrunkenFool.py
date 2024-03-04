import random
from AI import AI

class TheDrunkenFool(AI):
    def get_move(self, gamestate):
        legal_moves = gamestate.get_legal_moves()
        return random.choice(legal_moves)