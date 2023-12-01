import sys
import pygame
from pygame.locals import *

from Board import Board
from Constants import fps, SCREEN, ROWS, COLS
from Pill import Pill

pygame.init()
fpsClock = pygame.time.Clock()
current_pill = Pill()
board = Board()

GAME_DROP_PILL = pygame.USEREVENT + 1
pygame.time.set_timer(GAME_DROP_PILL, 1000)

CONTROL = pygame.USEREVENT + 2
pygame.time.set_timer(CONTROL, 100)

ROT = pygame.USEREVENT + 3
pygame.time.set_timer(ROT, 1000)

# Game loop.

def is_move_possible(x=0, y=0):
    curr_left_x = current_pill.left.x
    curr_left_y = current_pill.left.y

    curr_right_x = current_pill.right.x
    curr_right_y = current_pill.right.y

    # bottom check
    if max(curr_left_y, curr_right_y) + y == ROWS:
        return False

    # left wall check
    if min(curr_left_x, curr_right_x) + x < 0:
        return False

    # right wall
    if max(curr_left_x, curr_right_x) + x == COLS:
        return False

    # down pill
    if board.fields[curr_left_y + y][curr_left_x] != 0 or board.fields[curr_right_y + y][curr_right_x] != 0:
        return False

    # left/right pill
    if board.fields[curr_left_y][curr_left_x + x] != 0 or board.fields[curr_right_y][curr_right_x + x] != 0:
        return False

    return True


def applyPill():
    global current_pill

    board.applyPill(current_pill)
    current_pill = Pill()


def control_current_pill(mode=0):
    keys = pygame.key.get_pressed()
    x = 0
    y = 0
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if is_move_possible(y=1):
            y = 1
        else:
            applyPill()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if is_move_possible(x=-1):
            x = -1

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if is_move_possible(x=1):
            x = 1

    if keys[pygame.K_z]:
        current_pill.rotate(1)

    if keys[pygame.K_x]:
        current_pill.rotate(-1)

    current_pill.move(x, y)


while True:
    SCREEN.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == GAME_DROP_PILL:
            control_current_pill(1)
        elif event.type == CONTROL:
            control_current_pill()

            # Get the state of all keyboard keys
        # Update.

    # Draw.
    board.drawBoard()
    board.drawGrid()
    current_pill.draw_pill()
    pygame.display.flip()
    fpsClock.tick(fps)
