import pygame
import Variables

BALL_SIZE = 5


class Ball:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.color = [0, 0, 0]
        self.size = BALL_SIZE
        self.direction_x = 1  # -1 on vasakule ja 1 on paremale
        self.direction_y = -1  # -1 on üles ja 1 on alla
        self.rect = pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
        self.moves_since_last_direction = 0

    def move(self):
        self.moves_since_last_direction += 1
        self.x += self.direction_x * Variables.BALL_SPEED
        self.y += self.direction_y * Variables.BALL_SPEED

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.direction_x = 1
        self.direction_y = -1

    def draw(self, screen):
        self.rect = pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def calculate_ball_hit_y(self):
        s_cord = (self.x, self.y)
        hit_cord = (0, 0)
        direction_x = self.direction_x
        direction_y = self.direction_y

        while True:
            dist_to_bottom_wall = Variables.SCREEN_HEIGHT - s_cord[1]
            dist_to_top_wall = s_cord[1]
            dist_to_left_wall = s_cord[0]
            dist_to_right_wall = Variables.SCREEN_WIDTH - s_cord[0]

            if direction_x == 1:
                # Liigub alla
                if direction_y == 1:
                    hit_cord = (s_cord[0]+dist_to_bottom_wall, s_cord[1]+dist_to_bottom_wall)
                # Liigub yles
                else:
                    hit_cord = (s_cord[0]+dist_to_top_wall, s_cord[1]-dist_to_top_wall)

                if hit_cord[0] >= Variables.SCREEN_WIDTH:
                    hit_cord = (Variables.SCREEN_WIDTH, hit_cord[1] - (hit_cord[0] - Variables.SCREEN_WIDTH))
                    break
                else:
                    direction_y *= -1
                    s_cord = hit_cord
            else:
                break
        return hit_cord
