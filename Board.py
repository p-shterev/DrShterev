import pygame

from Constants import ROWS, SCREEN, SIZE, HEIGHT, COLS, WIDTH, pill_map
from Pill import Pill


class Board:
    fields = [[0]*COLS for i in range(ROWS)]

    def drawGrid(self):
        color = (144, 122, 9)
        for x in range(COLS):
            pygame.draw.line(SCREEN, color, (x * SIZE, 0), (x * SIZE, HEIGHT))
        for y in range(ROWS):
            pygame.draw.line(SCREEN, color, (0, y * SIZE), (WIDTH, y * SIZE))

    def drawBoard(self):
        for x in range(ROWS):
            for y in range(COLS):
                current = self.fields[x][y]
                if current != 0:
                    color = pill_map[current]
                    #print(color)
                else:
                    color = (255, 255, 255)
                pygame.draw.rect(SCREEN, color, (y * SIZE, x * SIZE, SIZE, SIZE))


    def applyPill(self, pill):
        self.fields[pill.left.y][pill.left.x] = pill.left.halfPill
        self.fields[pill.right.y][pill.right.x] = pill.right.halfPill



    def print(self):
        for rows in self.fields:
            for cols in rows:
                print(cols, end=" ")
            print()
