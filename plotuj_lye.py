import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('sp.txt', sep=' ')
data.columns = ['mua', 'l']
plt.plot(data.mua, data.l, linewidth=2)
plt.plot([0, 1], [0, 0], linewidth=2)
plt.axis([0.8, 1, -0.02, 0.02])
plt.savefig('pipik.png', dpi=2000)