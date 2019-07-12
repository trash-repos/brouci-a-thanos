import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join



files = [fd for fd in ( join('data/', f) for f in listdir('data/') ) if isfile(fd)]

mu_all = []
L_all = []
P_all = []
A_all = []
L0_all = []
P0_all = []
A0_all = []

for f in files:
    matrix = np.loadtxt(f, usecols=range(7))
    mu= matrix[:,0]
    L = matrix[:,1]
    P = matrix[:,2]
    A = matrix[:,3]
    L0 = matrix[:,4]
    P0 = matrix[:,5]
    A0 = matrix[:,6]

    mu_all.extend(mu)
    L_all.extend(L)
    P_all.extend(P)
    A_all.extend(A)
    L0_all.extend(L0)
    P0_all.extend(P0)
    A0_all.extend(A0)


count = len(mu_all)
indexRange = range(0, count)

total_all = [ L_all[i] + P_all[i] + A_all[i] for i in indexRange ]

fig = plt.figure()

ax1 = fig.add_subplot(211)

ax1.set_title("Bifurkační diagram")
ax1.set_xlabel('mua')
ax1.set_ylabel('populace')

#ax1.plot(mu, A, c='b', label='the data')

ax1.scatter(mu_all, A_all, c='black', s=1, label='A')
ax1.scatter(mu_all, P_all, c='r', s=1, label='P')
ax1.scatter(mu_all, L_all, c='b', s=1, label='L')
ax1.scatter(mu_all, total_all, c='purple', s=1, label='total')



A_mu1  = [A_all[i]  for i in indexRange if mu_all[i] > .9]
A0_mu1 = [A0_all[i] for i in indexRange if mu_all[i] > .9]

ax2 = fig.add_subplot(212)
ax2.set_title("Počáteční vs asymptotické A v mua > 0.9")
ax2.set_xlabel("A0")
ax2.set_title("A inf")
ax2.scatter(A0_mu1, A_mu1, s=1)

leg = ax1.legend()
plt.savefig("bifurcation.jpg", dpi=300)
plt.show()