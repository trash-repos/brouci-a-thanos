import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('lyee.txt', sep=' ')
data.columns = ['mua', 'l']
plt.plot(data.mua, data.l)
plt.plot([0.9+, 1], [0, 0])
plt.savefig('pipik.png', dpi=1000)