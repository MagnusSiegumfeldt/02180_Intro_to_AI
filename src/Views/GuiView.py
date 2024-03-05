import pygame, keyboard, sys, math
from View import View

red = (255,0,0)
white = (255,255,255)
green = (0,153,0)
black = (0,0,0)


class GuiView(View):
    def __init__(self):
        self.numberofclicks = 0
        self.swap = False
        self.done = False
        self.brick = [] 

        self.surface = pygame.display.set_mode((900,900))
        pygame.init()

        pass

    def update(self, x1,y1,x2,y2):
        self.brick.append([x1,y1,x2,y2])

    def onlyshow(self, game):
                # Draw background
        self.surface.fill(white)

        #Draving Grid
        i = 0
        for x in game.board:
            i = i + 1
            j = 0
            for y in x:
                j = j + 1
                pygame.draw.rect(self.surface, black, pygame.Rect((j-1)*100, (i-1)*100, 100, 100),2) 

        #Form Bricks
        for k in self.brick:
            if k[0] == k[2] :
                if k[1] < k[3] :
                    pygame.draw.rect(self.surface, green, pygame.Rect((k[0])*100+10, (k[1])*100+10, 80, 80+100)) 
                else :
                    pygame.draw.rect(self.surface, green, pygame.Rect((k[0])*100+10, (k[3])*100+10, 80, 80+100))  
            elif k[1] == k[3] :         
                if k[0] < k[2] :
                    pygame.draw.rect(self.surface, green, pygame.Rect((k[0])*100+10, (k[1])*100+10, 80 + 100, 80))
                else :
                    pygame.draw.rect(self.surface, green, pygame.Rect((k[2])*100+10, (k[1])*100+10, 80 + 100, 80))

        #Black and white
        i = 0
        for x in game.board:
            i = i + 1
            j = 0
            for y in x:
                j = j + 1
                if(y == 2) :
                    pygame.draw.rect(self.surface, black, pygame.Rect((j-1)*100+15, (i-1)*100+15, 70, 70))
                
                if(y == 1) :
                    pygame.draw.rect(self.surface, red, pygame.Rect((j-1)*100+15, (i-1)*100+15, 70, 70))
                
        pygame.display.flip()

    def show(self, game):
        
        self.onlyshow(game)