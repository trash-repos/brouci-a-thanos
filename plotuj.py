import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join



files = [fd for fd in ( join('data/', f) for f in listdir('data/') ) if isfile(fd)]

mu_all = []
A_all = []

for f in files:
    matrix = np.loadtxt(f, usecols=range(4))
    mu= matrix[:,0]
    L = matrix[:,1]
    P = matrix[:,2]
    A = matrix[:,3]

    mu_all.extend(mu)
    A_all.extend(A)


fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title...")
ax1.set_xlabel('your x label..')
ax1.set_ylabel('your y label...')

#ax1.plot(mu, A, c='b', label='the data')

ax1.scatter(mu_all, A_all, c='b', s=0.1, label='the data')

leg = ax1.legend()
plt.savefig("bifurcation600.pdf", dpi=600)
#plt.show()