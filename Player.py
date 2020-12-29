import pygame as pygame


class Player:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.color = [0, 0, 0]
        self.length = 100
        self.width = 10
        self.score = 0
        self.rect = pygame.draw.rect(screen, self.color, [self.x - 5, self.y, self.width, self.length])

    def move(self, move_size, screen_height):
        if self.y + self.length + move_size > screen_height:
            diff = screen_height - (self.y + self.length)
            self.move_player(diff)
        elif self.y + move_size < 0:
            self.move_player(-self.y)
        else:
            self.move_player(move_size)

    def move_player(self, move_size):
        self.y += move_size

    def reset(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, self.color, [self.x - 5, self.y, self.width, self.length])
