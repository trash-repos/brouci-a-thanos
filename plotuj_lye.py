import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ar = ["mua", "mua_f", "mul", "mul_f", "mup", "mup_f", "b"]

for fl in ar:
    data = pd.read_csv(fl + '.txt', sep=' ')
    data.columns = ['mua', 'l']
    plt.figure()
    plt.plot(data.mua, data.l, linewidth=0.5)
    plt.plot([0, 1], [0, 0], linewidth=0.5)
    plt.axis([np.min(data.mua), np.max(data.mua), -0.002, 0.002])
    plt.savefig(fl + '.png', dpi=500)
    plt.figure()
    plt.plot(data.mua, data.l, linewidth=0.5)
    plt.plot([0, 1], [0, 0], linewidth=0.5)
    plt.axis([np.min(data.mua), np.max(data.mua), -0.5, 0.5])
    plt.savefig(fl + '_wid.png', dpi=500)
