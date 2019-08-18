import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('sp.txt', sep=' ')
data.columns = ['mua', 'l']
plt.plot(data.mua, data.l, linewidth=0.5)
plt.plot([0, 1], [0, 0], linewidth=0.5)
plt.axis([0.94, 1, -0.002, 0.002])
plt.savefig('pipik.png', dpi=2000)