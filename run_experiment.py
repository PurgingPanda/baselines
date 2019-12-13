import math
import os
import subprocess
from multiprocessing.spawn import freeze_support

from baselines.run import main
freeze_support()
run = 1

if __name__ == "__main__":
    for run in range(1,6):
        baseParams = ['/home/niels/Repos/baselines-custom/baselines/run.py', '--alg=ppo2', '--env=BreakoutNoFrameskip-v4', '--num_timesteps=1e7', '--save_path=modelsBash/Breakout-run' + str(run) +'_1colors.pkl', '--log_path=logsBash/Breakout-run' + str(run) + "_1colors"]

        # Do base without loading a trained model
        # main(baseParams)
        file = open("run" + str(run) + ".sh", 'w')
        file.write("export BreakoutRandomBackground=1")
        file.write("\n")
        file.write("python run.py " + " ".join(baseParams[1:]))
        file.write("\n")
        baseParams.append('')

        for i in range(0,5):
            amtColors = int(math.pow(2,i))
            os.environ["BreakoutRandomBackground"] = str(amtColors)
            loadName = 'Breakout-run'+ str(run) + '_' + str(amtColors) + 'colors'
            saveName = 'Breakout-run'+ str(run) + '_' + str(amtColors*2) + 'colors'
            baseParams[4] = '--save_path=modelsBash/' + saveName + '.pkl'
            baseParams[6] = '--load_path=logsBash/' + loadName
            baseParams[5] = '--log_path=logsBash/' + saveName
            file.write("export BreakoutRandomBackground=" + str(amtColors*2))
            file.write("\n")
            file.write("python run.py " + " ".join(baseParams[1:]))
            file.write("\n")
            # main(baseParams)
        file.close()

