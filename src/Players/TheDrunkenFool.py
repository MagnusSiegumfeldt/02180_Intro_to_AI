import random
from Players import Player

class TheDrunkenFool(Player):
    def get_move(self, gamestate):
        legal_moves = gamestate.get_legal_moves()
        return random.choice(legal_moves)