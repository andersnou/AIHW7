from Player import Player


class TrackingAI(Player):
    def __init__(self, screen, player, ball):
        super().__init__(screen, player)
        self.ai = True
        self.ball = ball

    def move(self, move, screen_height):
        direction = self.get_direction()
        move_size = self.get_move_size(direction*move, screen_height)
        self.move_paddle(move_size)

    def get_direction(self):
        paddle_center = self.y + (self.length / 2)
        if self.ball.y > paddle_center:
            return 1
        return -1
