import pygame, keyboard, sys, math
from Move import Move
from Player import Player

class GuiPlayer(Player):
    
    numberofclicks = 0
    swap = False
    done = False
    def __init__(self,view):
        self.view = view
    def get_move(self, game):
        #self.onlyshow(game)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    btn=pygame.mouse
                    print ("x = {}, y = {}, numberofclicks = {}".format(pos[0], pos[1], self.numberofclicks))
                    x = pos[0]/100
                    posx = math.trunc(x)
                    y = pos[1]/100
                    posy = math.trunc(y)
                    if self.numberofclicks == 0 :
                        game.board[posy][posx] = 2
                        lastx = posx
                        lasty = posy 
                    elif self.numberofclicks == 1 :
                        if lastx == posx and lasty == posy :
                            game.board[posy][posx] = 1
                            self.swap = True
                        else : 
                            game.board[posy][posx] = 1
                            self.done = True
                    else :
                        if self.swap : 
                            game.board[posy][posx] = 2
                            self.done = True
                    
                    if self.done :
                        self.view.brick.append([lastx,lasty,posx,posy])
                        print ("x1 = {}, y1 = {}, x2 = {}, y2 = {}".format(lastx, lasty , posx, posy))
                    
                    self.view.onlyshow(game)
                    self.numberofclicks = self.numberofclicks + 1
                    print ("numberofclicks = {}".format(self.numberofclicks))
                    if self.done :
                        self.numberofclicks = 0
                        self.done = False
                        if self.swap :
                            return Move(lasty, lastx, posy, posx)
                        else :
                            return Move(posy, posx, lasty, lastx)
