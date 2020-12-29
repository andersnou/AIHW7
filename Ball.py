import pygame


BALL_SIZE = 5


class Ball():
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.color = [0, 0, 0]
        self.size = BALL_SIZE
        self.direction_x = -1
        self.direction_y = -1
        self.rect = pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def move(self, move_x, move_y):
        self.x += self.direction_x * move_x
        self.y += self.direction_y * move_y

    def reset(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        self.rect = pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
