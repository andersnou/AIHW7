import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import LSTM, Dense, Flatten, Input, Conv2D
from keras.optimizers import Adam, SGD, RMSprop
from PingPong import PingPong
import Variables
import pygame
import numpy as np
import json

# https://gist.github.com/EderSantana/c7222daa328f0e885093

global_inputs = []


def main():

    epsilon = 0.5

    model = Sequential()
    model.add(Dense(32, input_shape=(None, 4), activation='relu'))
    model.add(Dense(16))
    model.add(Dense(8))
    model.add(Dense(4, activation='relu'))
    model.add(Dense(3))

    model.compile(RMSprop(), "mse")

    #model.load_weights("model.h5")
    screen = pygame.display.set_mode(Variables.size)
    env = PingPong(screen, "random ai", "reward ai")
    pygame.init()
    pygame.display.set_caption("Ping pong")
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    win_count = 0

    for i in range(100):
        env.restart_game()
        loss = 0.0
        gameover = False
        inputs = []
        targets = []
        input_t = np.zeros((1,4))
        input_t[0] = np.array([env.player_two.x, env.player_two.y, env.ball.x, env.ball.y])
        while not gameover:
            reward = 0
            input_tm1 = input_t
            gameover = env.process_events()

            # get ai move
            if np.random.rand() <= epsilon:
                action = np.random.randint(0, 3, size=1)[0]
            else:
                q = model.predict(input_tm1)
                print("Q:", q)
                action = np.argmax(q[0])  # 0, 1 voi 2
            env.process_events()
            env.player_one.move(Variables.MOVE_SIZE)
            env.player_two.move_action(action)
            #env.move_ball()
            env.display_frame()


            input_t = np.zeros((1, 4))
            input_t[0] = np.array([env.player_two.x, env.player_two.y, env.ball.x, env.ball.y])

            #print("Action:", action)

            clock.tick(Variables.GAME_SPEED)
            hit_cord = env.ball.calculate_ball_hit_y()
            if env.player_two.check_collision_with_ball():
                reward = 10
            elif env.player_two.y <= hit_cord[1] <= env.player_two.y + 100:
                reward = 1
            else:
                reward = -1

            if env.is_game_over():
                if env.last_winner == 2:
                    reward = 0
                    win_count += 1
                else:
                    reward = -10
                gameover = True
            targets.append(gameover)
            inputs.append(np.asarray([input_tm1, action, reward, input_t]))

        inputs, targets = get_targets_and_inputs(model, inputs, targets)

        training = model.train_on_batch(inputs, targets)

    model.save_weights("model.h5", overwrite=True)
    with open("model.json", "w") as file:
        json.dump(model.to_json(), file)


def get_targets_and_inputs(model, inputs, targets):
    discount = 0.9
    targs = np.zeros((np.asarray(inputs).shape[0], 3))
    ins = np.zeros((len(inputs), 4))

    for i in range(len(inputs)):
        state_t = inputs[i][0]
        action_t = inputs[i][1]
        reward_t = inputs[i][2]
        state_tp1 = inputs[i][3]
        game_over = targets[i]
        ins[i:i + 1] = state_t

        targs[i] = model.predict(state_t)[0]
        Q_sa = np.max(model.predict(state_tp1)[0])
        if game_over:  # if game_over is True
            targs[i, action_t] = reward_t
        else:
            # reward_t + gamma * max_a' Q(s', a')
            targs[i, action_t] = reward_t + discount * Q_sa

    return ins, targs


main()