import pygame

ROWS = 16
COLS = 8
RATIO = ROWS//COLS
WIDTH, HEIGHT = 320, 320 * RATIO
SIZE = WIDTH // COLS
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


color_map = {
    "BLUE": (0, 0, 255),
    "RED": (255, 0, 0),
    "YELLOW": (255, 255, 0)
}

pill_map = {
    1: "BLUE",
    2: "RED",
    3: "YELLOW"
}

rotation_map = {
    0: [0, 0, -1, 1],
    1: [1, 0, 0, -1],
    2: [-1, 1, 0, 0],
    3: [0, -1,  1,  0]
}

rotation_map2 = {
    0: [0, 1, -1, 0],
    1: [1, -1, 0, 0],
    2: [-1, 0, 0, 1],
    3: [0, 0, 1, -1]
}



fps = 60
