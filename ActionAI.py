from Player import Player
import Variables


class ActionAI(Player):
    def __init__(self, screen, player, ball):
        super().__init__(screen, player, ball)
        self.ai = True

    def move_action(self, action):
        # 0 - ei tee midagi
        # 1 - yles
        # 2 - alla
        if action == 1:
            move_size = self.get_move_size(Variables.MOVE_SIZE)
            self.move_paddle(move_size)
        elif action == 2:
            move_size = self.get_move_size(-Variables.MOVE_SIZE)
            self.move_paddle(move_size)
        else:
            pass

    def check_collision_with_ball(self):
        if self.rect.colliderect(self.ball.rect):
            return True
        return False

