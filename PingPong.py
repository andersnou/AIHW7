import pygame
from Ball import Ball
from Player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
MOVE_SIZE = 20
BALL_SPEED = 3
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
START_HEIGHT = SCREEN_HEIGHT / 2 - 50


class PingPong:
    def __init__(self, screen):
        self.player_one = Player(screen, 10, START_HEIGHT, True)
        self.player_two = Player(screen, SCREEN_WIDTH-10, START_HEIGHT, False)
        self.ball = Ball(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.score = str(self.player_one.score) + ' : ' + str(self.player_two.score)

    def is_game_over(self):
        if self.ball.x <= 0:
            self.player_two.score += 1
            return True
        elif self.ball.x >= SCREEN_WIDTH:
            self.player_one.score += 1
            return True
        else:
            return False

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.KEYDOWN:
                if self.player_one.human:
                    if event.key == pygame.K_UP:
                        self.player_one.move(-MOVE_SIZE, SCREEN_HEIGHT)
                    elif event.key == pygame.K_DOWN:
                        self.player_one.move(MOVE_SIZE, SCREEN_HEIGHT)
                if self.player_two.human:
                    if event.key == pygame.K_w:
                        self.player_two.move(-MOVE_SIZE, SCREEN_HEIGHT)
                    elif event.key == pygame.K_s:
                        self.player_two.move(MOVE_SIZE, SCREEN_HEIGHT)
                elif event.key == pygame.K_r:
                    self.restart_game()

        return False

    def update_score(self):
        self.score = str(self.player_one.score) + ' : ' + str(self.player_two.score)

    def restart_game(self):
        self.player_one.reset(10, START_HEIGHT)
        self.player_two.reset(SCREEN_WIDTH-10, START_HEIGHT)
        self.ball.reset(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.update_score()

    def check_collision(self):
        if self.player_one.rect.colliderect(self.ball.rect) or self.player_two.rect.colliderect(self.ball.rect):
            self.ball.direction_x *= -1
        elif self.ball.y >= SCREEN_HEIGHT or self.ball.y <= 0:
            self.ball.direction_y *= -1
        else:
            return False

    def move_ball(self):
        self.check_collision()
        self.ball.move(BALL_SPEED, BALL_SPEED)

    def draw_sprites(self):
        self.player_one.draw(screen)
        self.player_two.draw(screen)
        self.ball.draw(screen)

    def draw_sprites(self):
        self.player_one.draw(screen)
        self.player_two.draw(screen)
        self.ball.draw(screen)

    def display_frame(self):
        screen.fill(WHITE)

        self.draw_sprites()
        self.move_ball()

        font = pygame.font.SysFont("serif", 25)
        text = font.render(self.score, True, BLACK)
        center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
        center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
        screen.blit(text, [center_x, center_y])

        pygame.display.flip()

    def move_ai(self):
        if not self.player_one.human:
            self.player_one.move_ai(MOVE_SIZE)

        if not self.player_two.human:
            self.player_two.move_ai(MOVE_SIZE)


def main():
    pygame.init()

    pygame.display.set_caption("Ping pong")
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    game = PingPong(screen)

    gameover = False

    while not gameover:

        gameover = game.process_events()
        game.move_ai()

        game.display_frame()

        clock.tick(60)

        if game.is_game_over():
            game.restart_game()

main()
