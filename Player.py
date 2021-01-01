import pygame
import Variables


class Player:
    def __init__(self, screen, player):
        if player == 1:
            self.x = 10
        else:
            self.x = Variables.SCREEN_WIDTH-10
        self.y = Variables.START_HEIGHT
        self.color = [0, 0, 0]
        self.length = 100
        self.width = 10
        self.score = 0
        self.player = player
        self.rect = pygame.draw.rect(screen, self.color, [self.x - 5, self.y, self.width, self.length])
        self.ai = False

    def move(self, move):
        move_size = self.get_move_size(move)
        self.move_paddle(move_size)

    def get_move_size(self, move):
        if self.y + self.length + move > Variables.SCREEN_HEIGHT:
            diff = Variables.SCREEN_HEIGHT - (self.y + self.length)
            return diff
        elif self.y + move < 0:
            diff = self.y
            return diff
        else:
            return move

    def move_paddle(self, move_size):
        self.y += move_size

    def reset(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, self.color, [self.x - 5, self.y, self.width, self.length])
