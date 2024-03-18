from abc import ABC, abstractmethod

""" Abstract player class that all players inherit from """
class Player(ABC):

    def __init__(self, color):
        self.color = color
        self.nodes_visited = 0

    @abstractmethod
    def get_move(self, gamestate):
        pass
