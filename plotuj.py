import matplotlib.pyplot as plt
import numpy as np

with open("pocitej_output.txt") as f:
    data = f.read().split(" ")


matrix = np.loadtxt('pocitej_output.txt', usecols=range(3))
L = matrix[:,0]
P = matrix[:,1]
A = matrix[:,2]
T = list(range(L.size))


fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title...")
ax1.set_xlabel('your x label..')
ax1.set_ylabel('your y label...')

ax1.plot(T, A, c='r', label='the data')

leg = ax1.legend()

plt.show()