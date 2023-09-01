import pygame

ROWS = 8
COLS = 16
RATIO = 2
WIDTH, HEIGHT = 300, 300 * RATIO
SIZE = WIDTH // ROWS
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
fps = 60
