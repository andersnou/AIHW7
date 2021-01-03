import random
from Player import Player


class RandomAI(Player):
    def __init__(self, screen, player, ball):
        super().__init__(screen, player, ball)
        self.ai = True

    def move(self, move):
        direction = self.get_direction()
        move_size = self.get_move_size(direction*move)
        self.move_paddle(move_size)

    def get_direction(self):
        return random.randint(-1, 1)
