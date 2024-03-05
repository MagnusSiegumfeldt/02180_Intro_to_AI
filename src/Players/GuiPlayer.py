import pygame, sys
from Move import Move
from Player import Player

class GuiPlayer(Player):
    numberofclicks = 0
    done = False
    def __init__(self,view):
        self.view = view
    def get_move(self, game):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    posx = pos[0] // self.view.sq_size
                    posy = pos[1] // self.view.sq_size

                    if self.numberofclicks == 0 and game.board[posx][posy] == 0:
                        self.view.highlight(posy, posx)
                        lastx = posx
                        lasty = posy 
                        self.numberofclicks = 1
                    elif self.numberofclicks == 1:
                        if (lastx == posx and lasty == posy) or not self.move_is_valid(lastx, lasty, posx, posy, game):
                            self.view.remove_highlight(posy, posx)
                            self.view.remove_highlight(lasty, lastx)
                            self.numberofclicks = 0
                        else: 
                            self.view.highlight(posy, posx)
                            self.done = True                    
                    if self.done:
                        self.numberofclicks = 0
                        self.done = False
                        return Move(lastx, lasty, posx, posy)
    
    def move_is_valid(self, row1, col1, row2, col2, gamestate):
        # Check if coordinates are adjacent (horizontally or vertically)
        if not (row1 == row2 and abs(col1 - col2) == 1) and not (col1 == col2 and abs(row1 - row2) == 1):
            print(f"Coordinates ({row1}, {col1}) and ({row2}, {col2}) are not adjacent.")
            return False
        # Check occupation
        elif gamestate.board[row1][col1] != 0 or gamestate.board[row2][col2] != 0:
            print("You cannot place a piece on an occupied square.")
            return False
        else:
            return True
