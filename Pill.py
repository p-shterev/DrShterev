import pygame.draw

from Constants import rotation_map, rotation_map2
from HalfPill import HalfPill


class Pill:

    def __init__(self):
        self.left = HalfPill(3, 5, color="BLUE")
        self.right = HalfPill(4, 5, color="RED")
        self.rot_count = 0
        self.rotation_maps = {
            0: [[0, 0, -1, 1], [0, 1, -1, 0]],
            1: [[1, 0, 0, -1], [1, -1, 0, 0]],
            2: [[-1, 1, 0, 0], [-1, 0, 0, 1]],
            3: [[0, -1, 1, 0], [0, 0, 1, -1]]
        }

    def rotate(self, dir):
        if dir > 0:
            self.left.x = self.left.x + rotation_map[self.rot_count][0]
            self.left.y = self.left.y + rotation_map[self.rot_count][1]
            self.right.x = self.right.x + rotation_map[self.rot_count][2]
            self.right.y = self.right.y + rotation_map[self.rot_count][3]

        else:
            self.left.x = self.left.x + rotation_map2[self.rot_count][0]
            self.left.y = self.left.y + rotation_map2[self.rot_count][1]
            self.right.x = self.right.x + rotation_map2[self.rot_count][2]
            self.right.y = self.right.y + rotation_map2[self.rot_count][3]

        self.rot_count = (self.rot_count + abs(dir)) % 4
        print(self.rot_count)
        print("-=-==-=-=-=")
        # rotation_map = self.rotation_maps[self.rot_count][dir > 0]
        # self.left.x += rotation_map[0]
        # self.left.y += rotation_map[1]
        # self.right.x += rotation_map[2]
        # self.right.y += rotation_map[3]
        # self.rot_count = (self.rot_count + abs(dir)) % 4
    def move(self, x, y):
        self.left.move(x, y)
        self.right.move(x, y)

    def draw_pill(self):
        self.left.draw()
        self.right.draw()