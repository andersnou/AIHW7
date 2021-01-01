import random
from Player import Player


class RandomAI(Player):
    def __init__(self, screen, player):
        super().__init__(screen, player)
        self.ai = True

    def move(self, move, screen_height):
        direction = self.get_direction()
        move_size = self.get_move_size(direction*move, screen_height)
        self.move_paddle(move_size)

    def get_direction(self):
        return random.randint(-1, 1)