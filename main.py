import sys
import pygame
from pygame.locals import *

from Board import Board
from Constants import fps, SCREEN
from Pill import Pill


pygame.init()

fpsClock = pygame.time.Clock()

board = Board()

# Game loop.
while True:
    SCREEN.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()

        # Check for specific key presses
        if keys[pygame.K_b]:
            print("-=-==-")
            board.applyPill()
            board.print()

    # Update.

    # Draw.
    board.drawBoard()
    board.drawGrid()

    pygame.display.flip()
    fpsClock.tick(fps)
