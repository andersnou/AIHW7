from Player import Player
from tensorflow.keras import Input
from tensorflow.keras.layers import Conv1D, Conv2D, Dropout, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Model
from tensorflow.keras.models import Sequential
import numpy as np


class AILabelled(Player):
    def __init__(self, screen, player, ball):
        super().__init__(screen, player, ball)
        self.ai = True
        self.model = self.create_model()

    def create_model(self):
        model2 = Sequential()
        model2.add(Input(shape=(2,)))
        model2.add(Flatten())
        model2.add(Dense(24, activation="relu"))
        model2.add(Dense(24, activation="relu"))
        model2.add(Dense(1, activation="linear"))
        """
        input_layer = Input(shape=(2,))
        conv = Conv2D(filters=32, kernel_size=3, activation="relu")(input_layer)
        dropout = Dropout(0.2)(conv)
        flatten = Flatten()(dropout)
        dense_1 = Dense(units=32, activation="relu")(flatten)
        dense_2 = Dense(units=32, activation="relu")(dense_1)
        output = Dense(units=1, activation="linear", name="output")(dense_2)
        model = Model(inputs=input_layer, outputs=[output])
"""
        model2.compile(optimizer=Adam(lr=0.001),
                       loss="mse")
        return model2

    def train(self):
        paddle_center = self.y + (self.length / 2)
        action = 0
        if self.ball.y > paddle_center:
            action = 0.999
        elif self.ball.y < paddle_center:
            action = -0.999
        paddle_center = self.y + (self.length / 2)
        self.model.fit([[self.ball.y, paddle_center]], [[action]])

    def move(self, move):
        direction = self.get_direction()
        move_size = self.get_move_size(direction * move)
        self.move_paddle(move_size)

    def get_direction(self):
        paddle_center = self.y + (self.length / 2)
        # x = np.asarray([[self.ball.y, self.y]]).astype(np.float32)
        x = [[self.ball.y, paddle_center]]
        action = self.model.predict(x)
        if action[0][0] < 0:
            return -1
        else:
            return 1
