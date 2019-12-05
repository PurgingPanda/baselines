import random

import numpy as np
import os

os.environ.setdefault('PATH', '')
from collections import deque
import gym


class BreakoutRandomBackgroundWrapper(gym.Wrapper):
    def __init__(self, env):
        gym.Wrapper.__init__(self, env)
        self.amount_of_random_colors = int(os.environ['BreakoutRandomBackground'])
        print("Started with amt of random colors", self.amount_of_random_colors)
        self.__set_random_color()

    def __set_random_color(self):
        colors = [(0, 0, 0)
            , (113, 252, 60)
            , (149, 182, 247)
            , (123, 20, 251)
            , (104, 93, 230)
            , (125, 29, 236)
            , (59, 134, 59)
            , (103, 15, 144)
            , (109, 100, 249)
            , (242, 228, 232)
            , (128, 130, 237)
            , (69, 20, 173)
            , (13, 21, 251)
            , (137, 20, 165)
            , (193, 54, 50)
            , (176, 225, 7)
            , (228, 248, 55)
            , (155, 208, 227)
            , (212, 11, 147)
            , (218, 52, 137)
            , (232, 2, 25)
            , (21, 13, 225)
            , (147, 130, 215)
            , (95, 110, 154)
            , (135, 113, 18)
            , (5, 38, 2)
            , (71, 63, 154)
            , (202, 193, 32)
            , (108, 254, 93)
            , (232, 129, 128)
            , (115, 131, 223)
            , (58, 173, 238)
            , (53, 123, 239)
            , (101, 216, 49)
            , (129, 18, 226)
            , (88, 232, 199)
            , (45, 170, 139)
            , (237, 118, 14)
            , (8, 52, 64)
            , (243, 204, 181)
            , (79, 246, 92)
            , (118, 234, 198)
            , (40, 155, 55)
            , (149, 214, 231)
            , (131, 31, 171)
            , (205, 21, 7)
            , (119, 181, 219)
            , (113, 217, 53)
            , (179, 147, 207)
            , (87, 55, 199)
            , (223, 140, 59)
            , (235, 207, 40)
            , (50, 122, 224)
            , (43, 125, 229)
            , (173, 152, 65)
            , (166, 212, 5)
            , (178, 11, 186)
            , (157, 221, 127)
            , (33, 132, 65)
            , (103, 160, 57)
            , (221, 18, 196)
            , (197, 72, 44)
            , (83, 28, 203)
            , (119, 39, 174)
            , (167, 171, 134)
            , (4, 207, 94)
            , (147, 120, 14)
            , (242, 1, 41)
            , (146, 90, 204)
            , (12, 236, 113)
            , (10, 69, 192)
            , (118, 157, 187)
            , (222, 229, 223)
            , (163, 149, 144)
            , (12, 57, 55)
            , (162, 194, 39)
            , (22, 208, 90)
            , (137, 194, 38)
            , (79, 180, 17)
            , (161, 135, 231)
            , (217, 114, 85)
            , (224, 69, 154)
            , (107, 11, 207)
            , (14, 55, 223)
            , (124, 224, 178)
            , (222, 192, 62)
            , (227, 175, 71)
            , (106, 186, 234)
            , (143, 98, 223)
            , (0, 30, 46)
            , (142, 216, 229)
            , (122, 95, 40)
            , (68, 39, 42)
            , (220, 2, 215)]
        i = random.randint(0, self.amount_of_random_colors-1)
        self.random_color = colors[i]

    def reset(self):
        self.__set_random_color()
        t = self.env.reset()
        t = self._modify_obs(t)
        return t

    def step(self, a):
        obs, b, c, d = self.env.step(a)
        obs = self._modify_obs(obs)
        return obs, b, c, d

    def render(self, mode='human', **kwargs):
        img = self.env.render(mode, **kwargs)
        return self._modify_obs(img)

    def _modify_obs(self, img):
        mask = (np.sum(img, (2)) < 1).astype(int)
        r = self.random_color[0]
        g = self.random_color[1]
        b = self.random_color[2]
        added = np.stack((mask * r, mask * g, mask * b), axis=2)

        return np.add(img, added).astype(np.uint8)
