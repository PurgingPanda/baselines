import random

import numpy as np
import os
os.environ.setdefault('PATH', '')
from collections import deque
import gym

class BreakoutRandomBackgroundWrapper(gym.Wrapper):
    def __init__(self, env):
        gym.Wrapper.__init__(self, env)
        self.__set_random_color()

    def __set_random_color(self):
        colors = [(0, 0, 0), (5, 55, 55)]
        i = random.randint(0, 1)
        self.random_color = colors[i]

    def reset(self):
        self.__set_random_color()
        t = self.env.reset()
        t = self._modify_obs(t)
        return t

    def step(self, a):
        obs, b, c, d = self.env.step(a)
        obs =  self._modify_obs(obs)
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

