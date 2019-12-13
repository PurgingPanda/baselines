import gym
import numpy as np

class AddNoiseToObsWrapper(gym.Wrapper):
    def __init__(self, env):
        gym.Wrapper.__init__(self, env)
        # self.amount_of_random_colors = int(os.environ['BreakoutRandomBackground'])
        print("Adding random noise to observations")

    def reset(self):
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
        noise = np.random.rand(210,160,3) * 50.0
        # r = self.random_color[0]
        # g = self.random_color[1]
        # b = self.random_color[2]
        # added = np.stack((mask * r, mask * g, mask * b), axis=2)
        added = (img + noise).astype('uint8')
        added = np.clip(added, 0, 200)
        return added

        # return np.add(img, added).astype(np.uint8)