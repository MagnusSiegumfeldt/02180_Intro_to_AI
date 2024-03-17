from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from View import View

BOARD_WIDTH = 600
BOARD_HEIGHT = 600
GRID_SIZE = 9  # 9x9 grid
SQ_SIZE = BOARD_WIDTH // GRID_SIZE


class GuiView(View):
    def __init__(self):
        self.numberofclicks = 0
        self.swap = False
        self.done = False
        self.bricks = []
        self.surface = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
        self.sq_size = SQ_SIZE
        pygame.init()

    def update(self, move):
        self.bricks.append([move.col1, move.row1, move.col2, move.row2])

    def highlight(self, row, col):
        highlight = pygame.Color(154, 179, 109)
        pygame.draw.rect(
            self.surface,
            highlight,
            pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE),
        )
        pygame.display.flip()

    def remove_highlight(self, row, col):
        bg1 = pygame.Color(115, 130, 104)
        bg2 = pygame.Color(138, 150, 128)
        color = bg1 if (row + col) % 2 == 0 else bg2
        pygame.draw.rect(
            self.surface,
            color,
            pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE),
        )
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
                pygame.draw.rect(
                    self.surface,
                    color,
                    pygame.Rect(j * SQ_SIZE, i * SQ_SIZE, SQ_SIZE, SQ_SIZE),
                )

        # Form Bricks
        for brick in self.bricks:
            row1, col1, row2, col2 = brick
            if row1 == row2 and col1 < col2:
                pygame.draw.rect(
                    self.surface,
                    light_bg,
                    pygame.Rect(
                        col1 * SQ_SIZE + border_gap,
                        row1 * SQ_SIZE + border_gap,
                        (SQ_SIZE - border_gap),
                        (SQ_SIZE - 2 * border_gap),
                    ),
                    border_bottom_left_radius=border_radius,
                    border_top_left_radius=border_radius,
                )
                pygame.draw.rect(
                    self.surface,
                    dark_bg,
                    pygame.Rect(
                        col2 * SQ_SIZE,
                        row2 * SQ_SIZE + border_gap,
                        (SQ_SIZE - border_gap),
                        (SQ_SIZE - 2 * border_gap),
                    ),
                    border_top_right_radius=border_radius,
                    border_bottom_right_radius=border_radius,
                )
            elif row1 == row2 and col1 > col2:
                pygame.draw.rect(
                    self.surface,
                    light_bg,
                    pygame.Rect(
                        col1 * SQ_SIZE,
                        row1 * SQ_SIZE + border_gap,
                        (SQ_SIZE - border_gap),
                        (SQ_SIZE - 2 * border_gap),
                    ),
                    border_top_right_radius=border_radius,
                    border_bottom_right_radius=border_radius,
                )
                pygame.draw.rect(
                    self.surface,
                    dark_bg,
                    pygame.Rect(
                        col2 * SQ_SIZE + border_gap,
                        row2 * SQ_SIZE + border_gap,
                        (SQ_SIZE - border_gap),
                        (SQ_SIZE - 2 * border_gap),
                    ),
                    border_bottom_left_radius=border_radius,
                    border_top_left_radius=border_radius,
                )
            elif row1 > row2 and col1 == col2:
                pygame.draw.rect(
                    self.surface,
                    light_bg,
                    pygame.Rect(
                        col1 * SQ_SIZE + border_gap,
                        row1 * SQ_SIZE,
                        (SQ_SIZE - 2 * border_gap),
                        (SQ_SIZE - border_gap),
                    ),
                    border_bottom_left_radius=border_radius,
                    border_bottom_right_radius=border_radius,
                )
                pygame.draw.rect(
                    self.surface,
                    dark_bg,
                    pygame.Rect(
                        col2 * SQ_SIZE + border_gap,
                        row2 * SQ_SIZE + border_gap,
                        (SQ_SIZE - 2 * border_gap),
                        (SQ_SIZE - border_gap),
                    ),
                    border_top_left_radius=border_radius,
                    border_top_right_radius=border_radius,
                )
            elif row1 < row2 and col1 == col2:
                pygame.draw.rect(
                    self.surface,
                    light_bg,
                    pygame.Rect(
                        col1 * SQ_SIZE + border_gap,
                        row1 * SQ_SIZE + border_gap,
                        (SQ_SIZE - 2 * border_gap),
                        (SQ_SIZE - border_gap),
                    ),
                    border_top_left_radius=border_radius,
                    border_top_right_radius=border_radius,
                )
                pygame.draw.rect(
                    self.surface,
                    dark_bg,
                    pygame.Rect(
                        col2 * SQ_SIZE + border_gap,
                        row2 * SQ_SIZE,
                        (SQ_SIZE - 2 * border_gap),
                        (SQ_SIZE - border_gap),
                    ),
                    border_bottom_left_radius=border_radius,
                    border_bottom_right_radius=border_radius,
                )

        pygame.display.flip()

    def show(self, game):
        self.onlyshow(game)
