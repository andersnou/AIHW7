import pygame
from Ball import Ball
from Player import Player
from RandomAI import RandomAI
from TrackingAI import TrackingAI
from TrainingBot import TrainingBot
from AILabelled import AILabelled
import Variables

screen = pygame.display.set_mode(Variables.size)


class PingPong:
    def __init__(self, screen):
        self.ball = Ball(screen, Variables.SCREEN_WIDTH / 2, Variables.SCREEN_HEIGHT / 2)
        # self.player_one = Player(screen, 1)
        # self.player_two = Player(screen, SCREEN_WIDTH-10, START_HEIGHT)
        # self.player_one = RandomAI(screen, 1)
        self.player_one = TrainingBot(screen, 1, self.ball)
        # self.player_two = TrackingAI(screen, 2, self.ball)
        player_two = AILabelled(screen, Variables.SCREEN_WIDTH - 10, self.ball)
        self.player_two = player_two
        self.score = str(self.player_one.score) + ' : ' + str(self.player_two.score)
        self.last_winner = 0

    def is_game_over(self):
        if self.ball.x <= 0:
            self.player_two.score += 1
            self.last_winner = 2
            print("Player two wins")
            return True
        elif self.ball.x >= Variables.SCREEN_WIDTH:
            self.player_two.train()
            self.player_one.score += 1
            self.last_winner = 1
            print("Player one wins")
            return True
        else:
            return False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.KEYDOWN:
                if not self.player_one.ai:
                    if event.key == pygame.K_UP:
                        self.player_one.move(-Variables.MOVE_SIZE)
                    elif event.key == pygame.K_DOWN:
                        self.player_one.move(Variables.MOVE_SIZE)
                if not self.player_two.ai:
                    if event.key == pygame.K_w:
                        self.player_two.move(-Variables.MOVE_SIZE)
                    elif event.key == pygame.K_s:
                        self.player_two.move(Variables.MOVE_SIZE)
                elif event.key == pygame.K_r:
                    self.restart_game()

        return False

    def update_score(self):
        self.score = str(self.player_one.score) + ' : ' + str(self.player_two.score)

    def restart_game(self):
        self.player_one.reset(10, Variables.START_HEIGHT)
        self.player_two.reset(Variables.SCREEN_WIDTH - 10, Variables.START_HEIGHT)
        self.ball.reset(Variables.SCREEN_WIDTH / 2, Variables.SCREEN_HEIGHT / 2)
        self.update_score()

    def check_collision(self):
        if self.player_one.rect.colliderect(self.ball.rect) or self.player_two.rect.colliderect(self.ball.rect):
            self.ball.direction_x *= -1
        elif self.ball.y >= Variables.SCREEN_HEIGHT or self.ball.y <= 0:
            self.ball.direction_y *= -1
        else:
            return False

    def move_ball(self):
        self.check_collision()
        self.ball.move()

    def draw_sprites(self):
        self.player_one.draw(screen)
        self.player_two.draw(screen)
        self.ball.draw(screen)

    def draw_sprites(self):
        self.player_one.draw(screen)
        self.player_two.draw(screen)
        self.ball.draw(screen)

    def display_frame(self):
        screen.fill(Variables.WHITE)

        self.draw_sprites()
        self.move_ball()

        font = pygame.font.SysFont("serif", 25)
        text = font.render(self.score, True, Variables.BLACK)
        center_x = (Variables.SCREEN_WIDTH // 2) - (text.get_width() // 2)
        center_y = (Variables.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])

        pygame.display.flip()

    def move_ai(self):
        if self.player_one.ai:
            self.player_one.move(Variables.MOVE_SIZE)
        if self.player_two.ai:
            self.player_two.move(Variables.MOVE_SIZE)


def main():
    pygame.init()

    pygame.display.set_caption("Ping pong")
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()
    # player_two = ModelAI(screen, Variables.SCREEN_WIDTH-10)
    game = PingPong(screen)

    gameover = False

    while not gameover:

        gameover = game.process_events()
        game.move_ai()

        game.display_frame()

        clock.tick(Variables.GAME_SPEED)

        if game.is_game_over():
            game.restart_game()


main()
