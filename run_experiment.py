import math
import os
from multiprocessing.spawn import freeze_support

from baselines.run import main
freeze_support()
run = 1

if __name__ == "__main__":
    for run in range(1,4):
        baseParams = ['/home/niels/Repos/baselines-custom/baselines/run.py', '--alg=ppo2', '--env=BreakoutNoFrameskip-v4', '--num_timesteps=1e7', '--save_path=models/Breakout-run' + str(run) +'_1colors.pkl', '--log_path=logs/Breakout-run' + str(run)]

        # Do base without loading a trained model
        main(baseParams)
        baseParams.append('')

        for i in range(0,5):
            amtColors = int(math.pow(2,i))
            os.environ["BreakoutRandomBackground"] = amtColors
            loadName = 'Breakout-run'+ str(run) + '_' + str(amtColors) + 'colors'
            saveName = 'Breakout-run'+ str(run) + '_' + str(amtColors*2) + 'colors.pkl'
            baseParams[4] = '--save-path=' + saveName + '.pkl'
            baseParams[6] = '--load-path=' + loadName
            baseParams[5] = '--log-path=' + saveName
            print(i, loadName, saveName)
            main(baseParams)

