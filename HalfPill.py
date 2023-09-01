import random

from Constants import pill_map


class HalfPill:
    def __init__(self):
        self.halfPill = random.choice(list(pill_map.keys()))
