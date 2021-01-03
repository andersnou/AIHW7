from Player import Player


class TrainingBot(Player):
    def __init__(self, screen, player, ball):
        super().__init__(screen, player, ball)
        self.ai = True
        self.ball = ball

    def move(self, move):
        direction = self.get_direction()
        move_size = self.get_move_size(direction*move)
        self.move_paddle(move_size)

    def get_direction(self):
        ball_y = self.ball.y
        if ball_y > self.y:
            return 1
        else:
            return -1
