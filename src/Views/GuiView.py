import pygame
from View import View


class GuiView(View):
    def __init__(self):
        self.numberofclicks = 0
        self.swap = False
        self.done = False
        self.bricks = [] 
        self.surface = pygame.display.set_mode((900,900))
        pygame.init()

    def update(self, move):
        self.bricks.append([move.col1, move.row1, move.col2, move.row2])
    
    def highlight(self, row, col):
        print(row, col)
        highlight = pygame.Color(154, 179, 109)
        pygame.draw.rect(self.surface, highlight, pygame.Rect(col*100, row*100, 100, 100))
        pygame.display.flip()

    def onlyshow(self, game):
        # Colors
        bg1 = pygame.Color(115, 130, 104)
        bg2 = pygame.Color(138, 150, 128)
        dark_bg = pygame.Color(69, 69, 69)
        light_bg = pygame.Color(217, 217, 217)

        border_radius = 10
        border_gap = 5

        # Drawing Grid
        for i in range(len(game.board)):
            for j in range(len(game.board[i])):
                color = bg1 if (i + j) % 2 == 0 else bg2
                pygame.draw.rect(self.surface, color, pygame.Rect(j * 100, i * 100, 100, 100))

        # Form Bricks
        for brick in self.bricks:
            row1, col1, row2, col2 = brick
            if row1 == row2 and col1 < col2:
                pygame.draw.rect(self.surface, light_bg, pygame.Rect(col1 * 100 + border_gap, row1 * 100 + border_gap, (100 - border_gap), (100 - 2 * border_gap)), border_bottom_left_radius=border_radius, border_top_left_radius=border_radius)
                pygame.draw.rect(self.surface, dark_bg, pygame.Rect(col2 * 100, row2 * 100 + border_gap, (100 - border_gap), (100 - 2 * border_gap)), border_top_right_radius=border_radius, border_bottom_right_radius=border_radius)
            elif row1 == row2 and col1 > col2:
                pygame.draw.rect(self.surface, light_bg, pygame.Rect(col1 * 100, row1 * 100 + border_gap, (100 - border_gap), (100 - 2 * border_gap)), border_top_right_radius=border_radius, border_bottom_right_radius=border_radius)
                pygame.draw.rect(self.surface, dark_bg, pygame.Rect(col2 * 100 + border_gap, row2 * 100 + border_gap, (100 - border_gap), (100 - 2 * border_gap)), border_bottom_left_radius=border_radius, border_top_left_radius=border_radius)
            elif row1 > row2 and col1 == col2:
                pygame.draw.rect(self.surface, light_bg, pygame.Rect(col1 * 100 + border_gap, row1 * 100, (100 - 2 * border_gap), (100 - border_gap)), border_bottom_left_radius=border_radius, border_bottom_right_radius=border_radius)
                pygame.draw.rect(self.surface, dark_bg, pygame.Rect(col2 * 100 + border_gap, row2 * 100 + border_gap, (100 - 2 * border_gap), (100 - border_gap)), border_top_left_radius=border_radius, border_top_right_radius=border_radius)
            elif row1 < row2 and col1 == col2:
                pygame.draw.rect(self.surface, light_bg, pygame.Rect(col1 * 100 + border_gap, row1 * 100 + border_gap, (100 - 2 * border_gap), (100 - border_gap)), border_top_left_radius=border_radius, border_top_right_radius=border_radius)
                pygame.draw.rect(self.surface, dark_bg, pygame.Rect(col2 * 100 + border_gap, row2 * 100, (100 - 2 * border_gap), (100 - border_gap)), border_bottom_left_radius=border_radius, border_bottom_right_radius=border_radius)
            
        pygame.display.flip()

    def show(self, game):
        self.onlyshow(game)