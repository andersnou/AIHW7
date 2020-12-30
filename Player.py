import pygame as pygame
import random

SCREEN_HEIGHT = 500


class Player:
    def __init__(self, screen, x, y, human):
        self.x = x
        self.y = y
        self.color = [0, 0, 0]
        self.length = 100
        self.width = 10
        self.score = 0
        self.rect = pygame.draw.rect(screen, self.color, [self.x - 5, self.y, self.width, self.length])
        self.human = human

    def move_ai(self, move_size):
        direction = random.randint(-1, 1)
        self.move(direction*move_size, SCREEN_HEIGHT)

    def move(self, move_size, screen_height):
        if self.y + self.length + move_size > screen_height:
            diff = screen_height - (self.y + self.length)
            self.move_paddle(diff)
        elif self.y + move_size < 0:
            self.move_paddle(-self.y)
        else:
            self.move_paddle(move_size)

    def move_paddle(self, move_size):
        self.y += move_size

    def reset(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, self.color, [self.x - 5, self.y, self.width, self.length])
