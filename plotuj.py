import matplotlib.pyplot as plt
import numpy as np

with open("pocitej_output.txt") as f:
    data = f.read().split(" ")


matrix = np.loadtxt('pocitej_output.txt', usecols=range(4))
mu= matrix[:,0]
L = matrix[:,1]
P = matrix[:,2]
A = matrix[:,3]


fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title...")
ax1.set_xlabel('your x label..')
ax1.set_ylabel('your y label...')

ax1.scatter(mu, A, c='b', s=1, label='the data')

leg = ax1.legend()

plt.show()