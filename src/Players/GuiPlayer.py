import pygame, sys
from Move import Move
from Player import Player

class GuiPlayer(Player):
    
    numberofclicks = 0
    swap = False
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
                    print ("x = {}, y = {}, numberofclicks = {}".format(pos[0], pos[1], self.numberofclicks))
                    posx = pos[0] // 100
                    posy = pos[1] // 100
                    if self.numberofclicks == 0:
                        self.view.highlight(posy, posx)
                        lastx = posx
                        lasty = posy 
                    elif self.numberofclicks == 1:
                        if lastx == posx and lasty == posy:
                            self.view.highlight(posy, posx)
                            self.swap = True
                        else: 
                            self.view.highlight(posy, posx)
                            self.done = True
                    else:
                        if self.swap: 
                            self.view.highlight(posy, posx)
                            self.done = True
                    

                    self.numberofclicks += 1
                    print ("numberofclicks = {}".format(self.numberofclicks))
                    if self.done:
                        self.numberofclicks = 0
                        self.done = False
                        move = None
                        if self.swap:
                            move = Move(posx, posy, lastx, lasty)
                        else:
                            move = Move(lastx, lasty, posx, posy)
                        
                        return move
