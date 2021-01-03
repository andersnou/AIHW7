from Player import Player
import Variables
from keras.models import Sequential
from keras.layers import LSTM, Dense, Flatten, Input, Conv2D
from keras.optimizers import RMSprop
from PingPong import PingPong
import Variables
import pygame
import numpy as np
import json

class ActionAI(Player):
    def __init__(self, screen, player, ball):
        super().__init__(screen, player, ball)
        self.ai = True
        self.model = self.load_model()

    def load_model(self):
        model = Sequential()
        model.add(Dense(32, input_shape=(None, 4), activation='relu'))
        model.add(Dense(16))
        model.add(Dense(8))
        model.add(Dense(4, activation='relu'))
        model.add(Dense(3))

        model.compile(RMSprop(), "mse")

        model.load_weights("model.h5")
        return model

    def predict(self):
        input_t = np.zeros((1, 4))
        input_t[0] = np.array([self.x, self.y, self.ball.x, self.ball.y])

        q = self.model.predict(input_t)
        action = np.argmax(q[0])  # 0, 1 voi 2
        return action

    def move(self, move):
        # 0 - ei tee midagi
        # 1 - yles
        # 2 - alla
        action = self.predict()
        if action == 1:
            move_size = self.get_move_size(Variables.MOVE_SIZE)
            self.move_paddle(move_size)
        elif action == 2:
            move_size = self.get_move_size(-Variables.MOVE_SIZE)
            self.move_paddle(move_size)
        else:
            pass

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

