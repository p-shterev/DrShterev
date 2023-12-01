import random

import pygame

from Constants import pill_map, SIZE, SCREEN


class HalfPill:
    def __init__(self, x, y, color=None):
        self.halfPill = random.choice(list(pill_map.keys()))
        self.x = x
        self.y = y
        self.color = color

    def move(self, x=0, y=0):
        self.x = self.x + x
        self.y = self.y + y

    def draw(self):
        if self.color is None:
            self.color = pill_map[self.halfPill]

        pygame.draw.rect(SCREEN, self.color, ((self.x * SIZE)+1, (self.y * SIZE)+1, SIZE-1, SIZE-1))

