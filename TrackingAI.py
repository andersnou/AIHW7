from Player import Player


class TrackingAI(Player):
    def __init__(self, screen, player, ball):
        super().__init__(screen, player, ball)
        self.ai = True

    def move(self, move):
        direction = self.get_direction()
        move_size = self.get_move_size(direction*move)
        self.move_paddle(move_size)

    def get_direction(self):
        paddle_center = self.y + (self.length / 2)
        if self.ball.y > paddle_center:
            return 1
        elif self.ball.y < paddle_center:
            return -1
        return 0
